using System;

namespace __APP_NAME__.ViewModels;

/// <summary>
/// ShellViewModel 的<b>设计时</b>支持（分部类的另一半）。
/// 供 XAML 中的 <c>d:DesignInstance IsDesignTimeCreatable=True</c> 使用，
/// 让设计器 / IntelliSense 能真实看到示例数据，而不是一片空白。
/// </summary>
/// <remarks>
/// 运行时由 Prism 容器解析带 <c>IRegionManager</c> 参数的主构造函数，
/// 永远不会走到本文件的构造函数；该构造函数只填静态示例数据，不触碰服务。
/// </remarks>
public partial class ShellViewModel
{
    /// <summary>
    /// 仅供 XAML 设计器使用的无参构造函数。请勿在运行时调用。
    /// </summary>
    [Obsolete("设计器专用构造函数。运行时请使用带 IRegionManager 的构造函数。", false)]
    public ShellViewModel()
    {
        AppTitle = "__APP_NAME__";
        StatusText = "就绪（设计器预览）";
    }
}
