using System.Windows.Controls;

namespace __APP_NAME__.Views;

/// <summary>
/// 主内容视图。由 Prism 区域导航加载到 Shell 的 <c>ContentRegion</c>；
/// DataContext 由 ViewModelLocator 按命名约定自动注入 <c>MainViewViewModel</c>。
/// </summary>
public partial class MainView : UserControl
{
    public MainView() => InitializeComponent();
}
