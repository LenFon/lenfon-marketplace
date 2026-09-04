using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using Prism.Navigation.Regions;

namespace __APP_NAME__.ViewModels;

/// <summary>
/// 主窗口（Shell）视图模型。由 Prism 的 ViewModelLocator 按命名约定自动装配：
/// Views.Shell -> ViewModels.ShellViewModel（AutoWireViewModel=True）。
/// 承载应用级状态（标题、子标题、状态栏文本等）。窗口 Loaded 后通过 LoadedCommand
/// 将主内容视图 MainView 区域导航到 Shell 的 ContentRegion。
/// </summary>
/// <remarks>
/// 本视图模型依赖 IRegionManager（DI 注入），故提供分部设计器构造函数
/// （见 ShellViewModel.Design.cs）；运行时由 Prism 容器解析带参主构造函数。
/// 全部可通知属性均使用 C# 13 分部属性（partial properties），命令使用
/// CommunityToolkit.Mvvm 的 [RelayCommand] 源生成（LoadedCommand）。
/// 注意：Shell 由 CreateShell 作为根窗口直接创建，并非区域导航目标，
/// 因此不实现 INavigationAware；初始导航改由窗口 Loaded 事件触发 LoadedCommand 完成。
/// </remarks>
public partial class ShellViewModel : ObservableObject
{
    // 运行时由 Prism 容器注入；设计器专用无参构造（Design.cs）中以 null! 占位
    private readonly IRegionManager _regionManager;

    public ShellViewModel(IRegionManager regionManager)
    {
        _regionManager = regionManager;
    }

    /// <summary>
    /// 窗口 Loaded 后执行的命令：将主内容视图 MainView 导航到 ContentRegion。
    /// 由 Shell.xaml 的 Interaction.Triggers（EventTrigger Loaded -> i:InvokeCommandAction，Microsoft.Xaml.Behaviors.Wpf 自带）触发。
    /// </summary>
    [RelayCommand]
    private void Loaded() => _regionManager.RequestNavigate("ContentRegion", "MainView");

    /// <summary>
    /// 应用标题。绑定到 Shell 顶部标题栏（第一行）与窗口 Title。
    /// </summary>
    [ObservableProperty]
    public partial string Title { get; set; } = "__APP_NAME__";

    /// <summary>
    /// 应用子标题。绑定到 Shell 顶部标题栏（第二行）。
    /// </summary>
    [ObservableProperty]
    public partial string SubTitle { get; set; } = "Prism 9 + Material Design 5 + CommunityToolkit.Mvvm 8";

    /// <summary>
    /// 状态栏文本。绑定到 Shell 底部状态栏。
    /// </summary>
    [ObservableProperty]
    public partial string StatusText { get; set; } = "就绪";
}
