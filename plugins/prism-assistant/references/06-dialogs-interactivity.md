# 6. DialogService 对话框与 Interactivity 交互行为

> 片段来自 Prism-Samples-Wpf（26/29）。

## 6.1 DialogService 对话框

统一的模态弹窗服务；对话框本体是 `UserControl`，由 DialogService 自动包进 Window（示例 26）。

### ① 注册（App.RegisterTypes）

```csharp
containerRegistry.RegisterDialog<NotificationDialog, NotificationDialogViewModel>();
```

### ② 调用（VM 中）

```csharp
private readonly IDialogService _dialogService;
public MainWindowViewModel(IDialogService dialogService) => _dialogService = dialogService;

private void ShowDialog()
{
    var message = "This is a message that should be shown in the dialog.";
    _dialogService.ShowDialog("NotificationDialog",
        new DialogParameters($"message={message}"),
        r =>
        {
            if (r.Result == ButtonResult.OK) Title = "Result is OK";
            else if (r.Result == ButtonResult.Cancel) Title = "Result is Cancel";
            else Title = "Result is None";
        });
}
```

### ③ 对话框 XAML（绑定 VM 命令关闭）

```xml
<UserControl ... prism:ViewModelLocator.AutoWireViewModel="True" Width="300" Height="150">
  <Grid Margin="5">
    <TextBlock Text="{Binding Message}" Grid.Row="0" TextWrapping="Wrap"/>
    <StackPanel Orientation="Horizontal" HorizontalAlignment="Right" Grid.Row="1">
      <Button Command="{Binding CloseDialogCommand}" CommandParameter="true"
              Content="OK" IsDefault="True"/>
      <Button Command="{Binding CloseDialogCommand}" CommandParameter="false"
              Content="Cancel" IsCancel="True"/>
    </StackPanel>
  </Grid>
</UserControl>
```

### ④ 实现 IDialogAware（对话框 VM）

```csharp
public class NotificationDialogViewModel : BindableBase, IDialogAware
{
    public string Message { get => _message; set => SetProperty(ref _message, value); }
    public DialogCloseListener RequestClose { get; }

    public virtual void OnDialogOpened(IDialogParameters parameters)
        => Message = parameters.GetValue<string>("message");   // 接收参数

    public virtual bool CanCloseDialog() => true;             // 是否允许关闭
    public virtual void OnDialogClosed() { }                   // 关闭后清理

    protected virtual void CloseDialog(string parameter)
    {
        var result = parameter?.ToLower() == "true" ? ButtonResult.OK : ButtonResult.Cancel;
        RequestClose.Invoke(new DialogResult(result));         // 关闭并回传结果
    }
    // XAML 中 CloseDialogCommand 调用 CloseDialog(string)
}
```

| 成员 | 作用 |
|---|---|
| `OnDialogOpened(params)` | 打开时接收 `DialogParameters` |
| `CanCloseDialog()` | 返回 false 时窗口不可关 |
| `OnDialogClosed()` | 关闭后释放资源 |
| `RequestClose.Invoke(result)` | 主动关闭并回传 `IDialogResult` |

> 命名空间为 `Prism.Dialogs`（Prism 8/9）。`ButtonResult`：None / OK / Cancel / Yes / No。`Show` 为非模态，`ShowDialog` 为模态。样式/自定义窗口见示例 27/28。

## 6.2 Interactivity 交互行为（InvokeCommandAction）

用 `prism:InvokeCommandAction` 把任意路由事件映射到 VM 命令，无需 code-behind（示例 29）：

```xml
<Button>
  <i:Interaction.Triggers>
    <i:EventTrigger EventName="MouseEnter">
      <prism:InvokeCommandAction Command="{Binding MyCommand}"
                                  CommandParameter="{Binding ...}"/>
    </i:EventTrigger>
  </i:Interaction.Triggers>
</Button>
```

> 与 `DelegateCommand` 配合，可把双击、鼠标进入、SelectionChanged 等事件都转成命令，保持 View 无逻辑。用户项目同时装了 `Microsoft.Xaml.Behaviors.Wpf`，其自带 `i:InvokeCommandAction` 优先级更高、可替代 Prism 的 `InvokeCommandAction`（见 wpf-basic-template 技能§四）。
