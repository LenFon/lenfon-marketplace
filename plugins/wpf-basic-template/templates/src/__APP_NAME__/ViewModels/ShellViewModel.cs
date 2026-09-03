using CommunityToolkit.Mvvm.ComponentModel;

namespace __APP_NAME__.ViewModels;

/// <summary>
/// 主窗口（Shell）视图模型。由 Prism 的 ViewModelLocator 按命名约定自动装配：
/// Views.Shell -> ViewModels.ShellViewModel（<c>AutoWireViewModel=True</c>）。
/// 承载应用级状态（标题、状态栏文本等）；主内容区由 <c>ContentRegion</c> 区域导航加载 <c>MainView</c>。
/// </summary>
/// <remarks>
/// 本视图模型无构造依赖，故无需单独的 <c>.Design.cs</c> 分部类；
/// XAML 直接以 <c>d:DesignInstance IsDesignTimeCreatable=True</c> 引用即可，设计器/IntelliSense 可见默认示例值。
/// 全部可通知属性均使用 C# 13 <b>分部属性（partial properties）</b>：
/// 声明处只写定义声明（public partial T X { get; set; }），
/// 由 CommunityToolkit.Mvvm 源生成器产出实现声明（SetProperty + 双向通知）。
/// </remarks>
public partial class ShellViewModel : ObservableObject
{
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
}
