# 2. MVVM、ViewModelLocator、DelegateCommand、CompositeCommand、IActiveAware

> 片段来自 Prism-Samples-Wpf（08/09/10/11/12/13）。

## 2.1 属性通知（BindableBase）

所有 ViewModel 继承 `BindableBase`，用 `SetProperty(ref field, value)` 触发 `INotifyPropertyChanged`：

```csharp
public class MainWindowViewModel : BindableBase
{
    private string _title = "Prism Unity Application";
    public string Title
    {
        get => _title;
        set => SetProperty(ref _title, value);   // 值变化自动通知 UI
    }

    // 集合属性同样用 SetProperty 包装
    private ObservableCollection<string> _messages;
    public ObservableCollection<string> Messages
    {
        get => _messages;
        set => SetProperty(ref _messages, value);
    }
}
```

> 示例源码用「私有字段 + 属性」写法。若项目用 C# 13 可改用分部属性 `[ObservableProperty]` 写法（按用户项目约定），或 CommunityToolkit.Mvvm 的 `ObservableObject`。Prism 的 `BindableBase` 与 CommunityToolkit 可并存，但同一 VM 不要混用两套通知机制。

## 2.2 ViewModelLocator（VM 自动绑定）

在 View 根元素加一行，按「View 名 → ViewModel 名」约定注入 `DataContext`（示例 08）：

```xml
<Window x:Class="ViewModelLocator.Views.MainWindow"
        xmlns:prism="http://prismlibrary.com/"
        prism:ViewModelLocator.AutoWireViewModel="True"
        Title="{Binding Title}">
    <Grid>
        <ContentControl prism:RegionManager.RegionName="ContentRegion" />
    </Grid>
</Window>
```

**默认约定**：`Views.MainWindow` → `ViewModels.MainWindowViewModel`

**自定义约定（示例 09）：重写 `ConfigureViewModelLocator`**

```csharp
protected override void ConfigureViewModelLocator()
{
    base.ConfigureViewModelLocator();
    ViewModelLocationProvider.SetDefaultViewTypeToViewModelTypeResolver((viewType) =>
    {
        var viewName = viewType.FullName;                       // 如 Views.MainWindow
        var asm = viewType.GetTypeInfo().Assembly.FullName;
        var vmName = $"{viewName}ViewModel, {asm}";             // 改成你的命名规则
        return Type.GetType(vmName);
    });
}
```

**手动注册特定 View（示例 10）**

```csharp
protected override void ConfigureViewModelLocator()
{
    base.ConfigureViewModelLocator();
    // 类型 / 类型
    ViewModelLocationProvider.Register<MainWindow, CustomViewModel>();
    // 或 类型 / 工厂（走容器解析，可注入依赖）
    // ViewModelLocationProvider.Register<MainWindow>(() => Container.Resolve<CustomViewModel>());
}
```

> 自定义 ViewModel 示例（示例 10）：`CustomViewModel : BindableBase`，`Title="Custom View Model Application"`。运行时 MainWindow 的 DataContext 即为此 VM。

## 2.3 DelegateCommand 命令

把按钮等 UI 行为绑定到 VM 方法（示例 11）：

```csharp
public class MainWindowViewModel : BindableBase
{
    private bool _isEnabled;
    public bool IsEnabled
    {
        get => _isEnabled;
        set { SetProperty(ref _isEnabled, value);
              ExecuteDelegateCommand.RaiseCanExecuteChanged(); }   // 手动通知 CanExecute 变化
    }

    public DelegateCommand ExecuteDelegateCommand { get; private set; }
    public DelegateCommand<string> ExecuteGenericDelegateCommand { get; private set; }
    public DelegateCommand DelegateCommandObservesCanExecute { get; private set; }

    public MainWindowViewModel()
    {
        // 标准：execute + canExecute
        ExecuteDelegateCommand = new DelegateCommand(Execute, CanExecute);

        // 监听某属性变化 → 自动重算 CanExecute（无需手动 RaiseCanExecuteChanged）
        DelegateCommandObservesProperty = new DelegateCommand(Execute, CanExecute)
                                            .ObservesProperty(() => IsEnabled);

        // 直接用表达式作为 CanExecute
        DelegateCommandObservesCanExecute = new DelegateCommand(Execute)
                                            .ObservesCanExecute(() => IsEnabled);

        // 泛型命令 + 监听
        ExecuteGenericDelegateCommand = new DelegateCommand<string>(ExecuteGeneric)
                                            .ObservesCanExecute(() => IsEnabled);
    }
    private void Execute() => UpdateText = $"Updated: {DateTime.Now}";
    private void ExecuteGeneric(string p) => UpdateText = p;
    private bool CanExecute() => IsEnabled;
}
```

```xml
<!-- XAML 绑定示例（示例 11） -->
<CheckBox IsChecked="{Binding IsEnabled}" Content="Can Execute Command"/>
<Button Command="{Binding ExecuteDelegateCommand}" Content="DelegateCommand"/>
<Button Command="{Binding ExecuteGenericDelegateCommand}" CommandParameter="Passed Parameter"
        Content="DelegateCommand Generic"/>
```

| 写法 | 说明 |
|---|---|
| `new DelegateCommand(Execute, CanExecute)` | 带可执行条件；条件变时手动 `RaiseCanExecuteChanged()` |
| `.ObservesProperty(() => Prop)` | 指定属性变化时自动重算 CanExecute |
| `.ObservesCanExecute(() => boolExpr)` | 直接用表达式作为 CanExecute（推荐） |
| `DelegateCommand<T>` | `CommandParameter` 自动转为 T |

## 2.4 CompositeCommand 复合命令

把多个子命令聚合成一个“全局命令”（如工具栏「全部保存」），执行时逐个触发（示例 12）。

```csharp
// 共享契约（放在 Core 项目）
public interface IApplicationCommands { CompositeCommand SaveCommand { get; } }
public class ApplicationCommands : IApplicationCommands
{
    private readonly CompositeCommand _saveCommand = new();
    public CompositeCommand SaveCommand => _saveCommand;
}

// 子 VM 中：把自身命令注册进全局复合命令
public class TabViewModel : BindableBase
{
    public DelegateCommand SaveCommand { get; }
    public TabViewModel(IApplicationCommands appCommands)
    {
        SaveCommand = new DelegateCommand(Save);
        appCommands.SaveCommand.RegisterCommand(SaveCommand);   // 注册
        // appCommands.SaveCommand.UnregisterCommand(SaveCommand); // 销毁时反注册
    }
    private void Save() { /* ... */ }
}
```

> 把 `ApplicationCommands` 注册为单例（`RegisterSingleton` 或容器解析），各模块共享同一实例。配合 **IActiveAware**（示例 13）：子命令实现 `IActiveAware`，复合命令执行时**只调用当前“活动”视图**的命令，避免误保存未激活页。
