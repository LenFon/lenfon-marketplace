using System.Windows;

namespace __APP_NAME__.Views;

/// <summary>
/// 主窗口（Shell）。作为导航容器承载 <c>ContentRegion</c>，并通过 Prism 的 ViewModelLocator
/// 自动装配 <c>ShellViewModel</c>（<c>AutoWireViewModel=True</c>，DataContext 即 ShellViewModel）。
/// 实际内容由 <see cref="ViewModels.ShellViewModel.Initialize"/> 通过 Prism 区域导航加载 <c>MainView</c>。
/// </summary>
public partial class Shell : Window
{
    public Shell() => InitializeComponent();
}
