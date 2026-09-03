using System.Windows;
using MahApps.Metro.Controls;

namespace __APP_NAME__.Views;

/// <summary>
/// 主窗口（Shell）。作为导航容器承载 <c>ContentRegion</c>，并通过 Prism 的 ViewModelLocator
/// 自动装配 <c>ShellViewModel</c>（<c>AutoWireViewModel=True</c>，DataContext 即 ShellViewModel）。
/// 窗口 Loaded 后由 <see cref="ViewModels.ShellViewModel.LoadedCommand"/>（XAML 中
/// <c>Interaction.Triggers</c> + <c>i:InvokeCommandAction</c>（Microsoft.Xaml.Behaviors.Wpf 自带）触发）通过 Prism 区域导航
/// 加载 <c>MainView</c>；ShellViewModel 承载应用级状态（标题、状态栏）。
/// </summary>
public partial class Shell : MetroWindow
{
    public Shell() => InitializeComponent();
}
