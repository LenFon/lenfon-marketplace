# 5. Region Navigation 区域导航（深度）

> 基于 Prism-Samples-Wpf 官方示例 17–24 真实源码整理。所有片段来自仓库原文。

## 5.1 概念与术语

Prism 的「区域导航」是一套**基于 URI 的视图切换机制**：给一个 Region 发一个目标标识（视图名或 Uri），Prism 负责解析视图、创建/复用实例、调用生命周期钩子、并维护前进/后退历史。

| 类型 / 接口 | 作用 | 示例 |
|---|---|---|
| `IRegionManager` | 发起导航 `RequestNavigate`、获取 Region、`RegisterForNavigation` 的注册入口 | 17/18/21 |
| `IRegionNavigationService` | 真正执行一次导航请求，持有 `Journal` | 24 |
| `NavigationParameters` | 键值对参数容器，随导航传递 | 21 |
| `NavigationContext` | 传给各生命周期方法的上下文：含 `Parameters`、`NavigationService`、`Uri`、`Region` | 20/21/24 |
| `INavigationAware` | 目标视图/VM 参与：`OnNavigatedTo` / `IsNavigationTarget` / `OnNavigatedFrom` | 20/21/24 |
| `IConfirmNavigationRequest` | `INavigationAware` 扩展，离开前确认/取消 | 22 |
| `IRegionMemberLifetime` | `KeepAlive` 控制离开后视图是否被回收 | 23 |
| `IRegionNavigationJournal` | 前进/后退历史：`GoBack`/`GoForward`/`CanGoBack`/`CanGoForward` | 24 |
| `NavigationResult` | 回调结果：`Success` / `Exception` / `Context` | 18 |

## 5.2 视图注册：RegisterForNavigation

没有被注册的视图无法作为导航目标。在模块的 `RegisterTypes` 中注册（示例 18 的 `ModuleAModule`）：

```csharp
public void RegisterTypes(IContainerRegistry containerRegistry)
{
    containerRegistry.RegisterForNavigation<ViewA>();
    containerRegistry.RegisterForNavigation<ViewB>();
}
```

**四种重载（Prism 9 实测可用）**

| 重载 | URI / 解析名 | 说明 |
|---|---|---|
| `RegisterForNavigation<TView>()` | 视图类型短名，如 `"ViewA"` | View 与同名 VM 按 ViewModelLocator 约定自动绑定 |
| `RegisterForNavigation<TView,TViewModel>()` | 视图类型短名 | 显式指定 VM，不依赖约定 |
| `RegisterForNavigation<TView>(string name)` | 自定义名 `name` | 用别名导航，如 `"Home"` |
| `RegisterForNavigation<TView,TViewModel>(string name)` | 自定义名 `name` | 别名 + 显式 VM |

> 导航的「Uri」默认就是视图类型的**短名**（去掉命名空间）。示例 17 中按钮传 `CommandParameter="ViewA"`，正好对应 `RegisterForNavigation<ViewA>()` 注册出的 URI。可用命名空间限定名或别名避免冲突。

## 5.3 发起导航：RequestNavigate 三种形态

壳层 ViewModel 注入 `IRegionManager`，在命令里调用 `RequestNavigate`。

### 3.1 最简形式（示例 17）

```csharp
private readonly IRegionManager _regionManager;
public DelegateCommand<string> NavigateCommand { get; private set; }

public MainWindowViewModel(IRegionManager regionManager)
{
    _regionManager = regionManager;
    NavigateCommand = new DelegateCommand<string>(Navigate);
}

private void Navigate(string navigatePath)
{
    if (navigatePath != null)
        _regionManager.RequestNavigate("ContentRegion", navigatePath);
}
```

```xml
<!-- 示例 17 MainWindow.xaml -->
<Button Command="{Binding NavigateCommand}"
        CommandParameter="ViewA">Navigate to View A</Button>
<ContentControl prism:RegionManager.RegionName="ContentRegion" />
```

### 3.2 带完成回调（示例 18）

```csharp
private void Navigate(string navigatePath)
{
    if (navigatePath != null)
        _regionManager.RequestNavigate("ContentRegion", navigatePath, NavigationComplete);
}

private void NavigationComplete(NavigationResult result)
{
    // 真实代码只弹了 URI，但 NavigationResult 还携带 Success / Exception
    MessageBox.Show(string.Format("Navigation to {0} complete. ", result.Context.Uri));
}
```

> 第三参数是一个 `Action<NavigationResult>`。导航**完成（成功或失败）后**回到 UI 线程调用。用它检查 `result.Success` 与 `result.Exception` 做错误处理。

### 3.3 带参数（示例 21）

```csharp
private void PersonSelected(Person person)
{
    var parameters = new NavigationParameters();
    parameters.Add("person", person);

    if (person != null)
        _regionManager.RequestNavigate("PersonDetailsRegion", "PersonDetail", parameters);
}
```

> 参数、回调可以同时给：`RequestNavigate(region, uri, NavigationComplete, parameters)`。还可以传 `Uri` 对象（含查询字符串，如 `new Uri("PersonDetail?name=Tom", UriKind.Relative)`），参数会被解析进 `NavigationParameters`。

## 5.4 导航生命周期全景

一次 `RequestNavigate` 在内部按顺序发生如下事件：

```
RequestNavigate(region, uri)
  ① 旧视图 IsNavigationTarget?  ──true──▶ 复用已有实例
        │false / 无
        ▼
  解析并创建新视图
  ② 旧视图 OnNavigatedFrom
  ③ 新视图 OnNavigatedTo
  ④ Journal 记录 + ⑤ NavigationResult 回调
```

> 若**旧视图**实现了 `IConfirmNavigationRequest`，在第 ① 步之前还会先调用 `ConfirmNavigationRequest` 询问是否允许离开（见 5.8）。

## 5.5 INavigationAware 三方法规则

导航目标（View 或 ViewModel，或两者）实现 `INavigationAware` 即可参与生命周期。示例 20 的 `ViewAViewModel` 是最小可运行范式：

```csharp
public class ViewAViewModel : BindableBase, INavigationAware
{
    private int _pageViews;
    public int PageViews { get => _pageViews; set => SetProperty(ref _pageViews, value); }

    public void OnNavigatedTo(NavigationContext navigationContext)
    {
        PageViews++;   // 每次进入都自增，可证明视图被复用
    }

    public bool IsNavigationTarget(NavigationContext navigationContext)
    {
        return PageViews / 3 != 1;   // 返回 true=复用当前实例；false=创建新实例
    }

    public void OnNavigatedFrom(NavigationContext navigationContext) { }
}
```

| 方法 | 调用时机 | 返回值含义 | 典型用途 |
|---|---|---|---|
| `OnNavigatedTo(ctx)` | 新视图成为活动视图**之后** | void | 读参数、加载数据、递增计数、绑定 Journal |
| `IsNavigationTarget(ctx)` | 导航解析阶段，决定复用哪个已有实例 | true→复用现有实例；false→新建 | 按业务键复用（如同一 Person 复用同一页） |
| `OnNavigatedFrom(ctx)` | 旧视图即将失去活动状态**之前** | void | 保存草稿、注销事件、释放临时资源 |

> **IsNavigationTarget 是导航的「复用开关」。** 默认（不实现 INavigationAware）每次导航都会创建新实例并叠加到 Region 的 Views 集合。实现后返回 `true` 可让同一 Region 复用同一视图，避免无限堆叠。

## 5.6 导航参数传递（示例 21）

**发送方**：

```csharp
private void PersonSelected(Person person)
{
    var parameters = new NavigationParameters();
    parameters.Add("person", person);

    if (person != null)
        _regionManager.RequestNavigate("PersonDetailsRegion", "PersonDetail", parameters);
}
```

```xml
<!-- PersonList.xaml -->
<ListBox x:Name="_listOfPeople" ItemsSource="{Binding People}">
  <i:Interaction.Triggers>
    <i:EventTrigger EventName="SelectionChanged">
      <prism:InvokeCommandAction Command="{Binding PersonSelectedCommand}"
            CommandParameter="{Binding SelectedItem, ElementName=_listOfPeople}" />
    </i:EventTrigger>
  </i:Interaction.Triggers>
</ListBox>
<TabControl prism:RegionManager.RegionName="PersonDetailsRegion" />
```

**接收方**（在 `OnNavigatedTo` 取参数）：

```csharp
public void OnNavigatedTo(NavigationContext navigationContext)
{
    var person = navigationContext.Parameters["person"] as Person;
    if (person != null)
        SelectedPerson = person;
}

public bool IsNavigationTarget(NavigationContext navigationContext)
{
    var person = navigationContext.Parameters["person"] as Person;
    if (person != null)
        return SelectedPerson != null && SelectedPerson.LastName == person.LastName;
    else
        return true;
}
```

> 这里 `IsNavigationTarget` 用 `LastName` 作为业务键：导航到「同一人」时复用同一页，导航到「不同人」时新建页。参数的 key 区分大小写，取不到返回 `null`。也可 `GetValue<T>(key)` 取值。

## 5.7 导航完成回调 NavigationResult（示例 18）

| 属性 | 含义 |
|---|---|
| `result.Success` | 导航是否成功（视图解析/创建/激活无异常） |
| `result.Exception` | 失败时的异常，用来定位「视图未注册 / 构造异常 / 区域不存在」等 |
| `result.Context` | 本次导航的 `NavigationContext`（含 Uri、Parameters、Region、NavigationService） |

```csharp
private void NavigationComplete(NavigationResult result)
{
    if (result.Success)
        _log.Info($"导航到 {result.Context.Uri} 成功");
    else
        MessageBox.Show($"导航失败：{result.Exception?.Message}");
}
```

> 导航回调在 **UI 线程**执行。若视图构造函数或 `OnNavigatedTo` 抛异常，`Success=false` 且 `Exception` 非空——务必处理，否则区域会停留在旧视图且无提示。

## 5.8 确认/取消导航：IConfirmNavigationRequest（示例 22）

当目标（或当前活动视图）实现 `IConfirmNavigationRequest` 时，Prism 在离开前调用它，**必须调用 `continuationCallback(bool)` 给出裁决**，否则导航会永久挂起。

```csharp
public class ViewAViewModel : BindableBase, IConfirmNavigationRequest
{
    public void ConfirmNavigationRequest(NavigationContext navigationContext,
                                         Action<bool> continuationCallback)
    {
        bool result = true;
        if (MessageBox.Show("Do you want to navigate?", "Navigate?",
                MessageBoxButton.YesNo) == MessageBoxResult.No)
            result = false;

        continuationCallback(result);   // 必须调用：true 放行，false 取消
    }

    public bool IsNavigationTarget(NavigationContext navigationContext) => true;
    public void OnNavigatedFrom(NavigationContext navigationContext) { }
    public void OnNavigatedTo(NavigationContext navigationContext) { }
}
```

> **规则**：① `continuationCallback` 只能调用一次；② 异步场景可延后调用（如等用户确认弹窗）；③ 返回 `false` 时本次导航整体取消，旧视图保持活动；④ 确认逻辑也可放在**正要离开**的视图上，不一定要在目标视图。

## 5.9 视图复用与生命周期：IRegionMemberLifetime（示例 23）

默认导航视图在离开后**仍保留**在 Region 的 Views 集合中（只是非活动）。实现 `IRegionMemberLifetime` 并把 `KeepAlive` 设为 `false`，离开后即被移除并销毁。

```csharp
public class ViewAViewModel : BindableBase, INavigationAware, IRegionMemberLifetime
{
    public bool KeepAlive => false;   // 离开即销毁，下次导航重新创建

    public bool IsNavigationTarget(NavigationContext navigationContext) => false;
    public void OnNavigatedFrom(NavigationContext navigationContext) { }
    public void OnNavigatedTo(NavigationContext navigationContext) { }
}
```

| `KeepAlive` | 行为 | 适用 |
|---|---|---|
| `true`（默认） | 离开后视图实例保留，可随时切回，状态不丢 | 表单、编辑页等需保留现场 |
| `false` | 离开即移除销毁，下次重新构造 | 一次性向导页、轻量展示页 |

## 5.10 前进/后退日志：IRegionNavigationJournal（示例 24）

每次成功的 `RequestNavigate` 都会被记入 Region 的 `NavigationService.Journal`。在 `OnNavigatedTo` 里取出 Journal，即可实现浏览器式前进/后退。

```csharp
// PersonDetailViewModel（后退）
private IRegionNavigationJournal _journal;

public void OnNavigatedTo(NavigationContext navigationContext)
{
    _journal = navigationContext.NavigationService.Journal;   // 从上下文取日志
    var person = navigationContext.Parameters["person"] as Person;
    if (person != null) SelectedPerson = person;
}

private void GoBack() => _journal.GoBack();
```

```csharp
// PersonListViewModel（前进，带 CanExecute）
public void OnNavigatedTo(NavigationContext navigationContext)
{
    _journal = navigationContext.NavigationService.Journal;
    GoForwardCommand.RaiseCanExecuteChanged();   // 进入后刷新按钮可用态
}
private void GoForward() => _journal.GoForward();
private bool CanGoForward() => _journal != null && _journal.CanGoForward;
```

| 成员 | 作用 |
|---|---|
| `GoBack()` / `CanGoBack` | 后退到上一记录；无历史时为 false |
| `GoForward()` / `CanGoForward` | 前进到下一记录；已在最新时为 false |
| `Clear()` | 清空历史 |

> **只有 `RequestNavigate` 才会写入 Journal。** 用 View Injection / Activation 切视图、或直接 `region.Activate(view)` 都不会产生历史记录，`GoBack/GoForward` 也就无效果。示例 24 中后退按钮放在 `PersonDetail`、前进按钮放在 `PersonList`，二者共享同一个 Region 的 Journal。

## 5.11 View 与 ViewModel 谁参与导航？

Prism 会**同时检查 View 和 ViewModel** 是否实现 `INavigationAware` / `IConfirmNavigationRequest` / `IRegionMemberLifetime`，两者都会收到调用。

| 场景 | 建议放哪 | 原因 |
|---|---|---|
| 读参数、加载数据 | ViewModel | 纯逻辑，可单测，不依赖 UI 线程 |
| MessageBox 确认离开 | View 代码后台 或 VM | 示例 22 放在 VM；确需弹窗可放 View。务必调用 continuationCallback |
| 操作具体控件 / 焦点 | View 代码后台 | 需要视觉元素引用 |
| KeepAlive | ViewModel（更常见） | 生命周期状态与 VM 绑定更自然 |

> 示例 19 用 `TabControl` 作 Region，并把 `TabItem.Header` 绑定到 `DataContext.Title`，证明「导航目标可以是任何被 RegionAdapter 支持的控件」，不只是 ContentControl。导航参与的钩子对 View / VM 一视同仁。

## 5.12 NavigationContext 完整 API

| 成员 | 类型 | 说明 |
|---|---|---|
| `Parameters` | `NavigationParameters` | 本次导航携带的全部参数，支持索引器 `[key]` 与 `GetValue<T>(key)` |
| `Uri` | `Uri` | 本次导航目标 URI（含查询字符串，若用 Uri 形式发起） |
| `NavigationService` | `IRegionNavigationService` | 本次导航服务，持有 `Journal`，可继续 `RequestNavigate` 链式导航 |
| `Region` | `IRegion` | 目标所在 Region |

## 5.13 规则与避坑清单

1. **先注册，后导航。** 未 `RegisterForNavigation` 的视图调用 `RequestNavigate` 会失败，`NavigationResult.Success=false` 且 `Exception` 提示「未找到视图」。
2. **区域名必须存在。** 第一个参数 `"ContentRegion"` 要在 XAML 里用 `prism:RegionManager.RegionName` 声明过，否则找不到区域。
3. **默认每次导航都新建视图。** 想复用必须实现 `IsNavigationTarget` 返回 true，否则 Region.Views 会无限堆叠（内存泄漏风险）。
4. **确认导航必须调用 continuationCallback。** 忘了调用 → 导航卡死，界面无响应。
5. **Journal 只对 RequestNavigate 生效。** View Injection / Activation 不产生历史，GoBack/GoForward 无效。
6. **KeepAlive=false 会销毁视图。** 若你又在 `IsNavigationTarget` 返回 true 会冲突——示例 23 同时返回 false 表示「不复用且离开即销毁」，二者语义要一致。
7. **参数跨模块传对象要可序列化/可共享。** 推荐传 Id 或 DTO，而非直接传 UI 元素；跨模块时类型需在共享契约层（如 Application 层）可见。
8. **回调在 UI 线程。** 可在回调里直接操作 UI / 弹窗，但别做长耗时同步操作。
9. **导航目标可放在 ViewModel 或 View。** 同一导航周期里两者都会被调用，注意别重复处理逻辑。
10. **异步导航。** Prism 9 提供 `RequestNavigate` 的任务重载（`Task<NavigationResult>`），可在 `async/await` 中等待完成，取代回调写法。
11. **Region 适配器决定容器语义。** ContentControl=单活动视图；Selector/TabControl/ItemsControl=可多视图共存。导航/Journal 行为在单视图容器下最直观。
12. **与 ViewModelLocator 共存。** 导航视图同样适用 `AutoWireViewModel`；用 `RegisterForNavigation<TView,TViewModel>()` 可绕过命名约定强制绑定。

## 5.14 综合可运行骨架（整合全部要素）

```csharp
// App.xaml.cs
public partial class App : PrismApplication
{
    protected override Window CreateShell() => Container.Resolve<MainWindow>();
    protected override void RegisterTypes(IContainerRegistry c) { }
    protected override void ConfigureModuleCatalog(IModuleCatalog cat)
        => cat.AddModule<ModuleA.ModuleAModule>();
}

// ModuleA/ModuleAModule.cs
public void RegisterTypes(IContainerRegistry c)
{
    c.RegisterForNavigation<PersonList>();
    c.RegisterForNavigation<PersonDetail, PersonDetailViewModel>();
}

// 发起（PersonListViewModel）
_regionManager.RequestNavigate("MainRegion", "PersonDetail",
    new NavigationParameters { { "id", 42 } });

// 接收（PersonDetailViewModel : INavigationAware）
public void OnNavigatedTo(NavigationContext ctx)
{
    Id = ctx.Parameters.GetValue<int>("id");
    _journal = ctx.NavigationService.Journal;   // 接管 Journal 以支持后退
}
```

> 结合现有 **ABP + Prism 分层**：把 `RegisterForNavigation` 放进各模块的 `RegisterTypes`（模块即 General.EQP 的上料/视觉/运控子模块），导航参数优先用 **Application 层契约 DTO**（如 `PickTaskDto`）而非 Domain 实体，保证跨模块类型可见且解耦。WMX3 运控回调触发导航时，从后台线程回到 UI 用 `RequestNavigate` 的任务重载 + `await`。
