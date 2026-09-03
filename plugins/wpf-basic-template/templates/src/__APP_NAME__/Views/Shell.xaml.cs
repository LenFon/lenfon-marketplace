using System.Windows;

namespace __APP_NAME__.Views;

/// <summary>
/// 主窗口（Shell）。仅作为导航容器承载 <c>ContentRegion</c>，自身不绑定业务视图模型
/// （<c>AutoWireViewModel=False</c>）。实际内容由 <see cref="App.OnInitialized"/> 通过 Prism
/// 区域导航加载 <c>MainView</c>。
/// </summary>
public partial class Shell : Window
{
    public Shell() => InitializeComponent();
}
