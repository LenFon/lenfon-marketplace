using CommunityToolkit.Mvvm.ComponentModel;
using Prism.Mvvm;
using Prism.Navigation.Regions;

namespace __APP_NAME__.ViewModels;

/// <summary>
/// 主窗口（Shell）视图模型。由 Prism 的 ViewModelLocator 按命名约定自动装配：
/// Views.Shell -> ViewModels.ShellViewModel（<c>AutoWireViewModel=True</c>）。
/// 承载应用级状态（标题、状态栏文本等），并在 <see cref="Initialize"/> 中通过区域导航
/// 将 <c>MainView</c> 加载进 Shell 的 <c>ContentRegion</c>。
/// </summary>
/// <remarks>
/// 本视图模型依赖 <c>IRegionManager</c>（DI 注入），故提供分部设计器构造函数
/// （见 ShellViewModel.Design.cs）；运行时由 Prism 容器解析带参主构造函数。
/// 全部可通知属性均使用 C# 13 <b>分部属性（partial properties）</b>。
/// </remarks>
public partial class ShellViewModel : ObservableObject, IInitialize
{
    private readonly IRegionManager _regionManager;

    public ShellViewModel(IRegionManager regionManager)
    {
        _regionManager = regionManager;
    }

    /// <summary>
    /// 窗口标题。绑定到 Shell 的 <c>Title</c>。
    /// </summary>
    [ObservableProperty]
    public partial string AppTitle { get; set; } = "__APP_NAME__";

    /// <summary>
    /// 状态栏文本。绑定到 Shell 底部状态栏。
    /// </summary>
    [ObservableProperty]
    public partial string StatusText { get; set; } = "就绪";

    /// <summary>
    /// 视图就绪后（Prism 在 Shell Loaded 后自动调用），将主内容视图 <c>MainView</c>
    /// 导航到 <c>ContentRegion</c>。Shell.xaml 已用 <c>prism:RegionManager.RegionName</c>
    /// 声明该区域，此时区域已注册，导航必然生效。
    /// </summary>
    public void Initialize() => _regionManager.RequestNavigate("ContentRegion", "MainView");
}
