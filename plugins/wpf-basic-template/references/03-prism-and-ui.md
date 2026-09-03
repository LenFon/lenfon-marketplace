# Prism 引导、主题与 UI 约定

## Prism 引导

- `App.xaml` 根元素必须是 `prism:PrismApplication`，**不写 `StartupUri`**、不在 `App()` 里调 `Initialize()`（基类自动完成）。
- `CreateShell()` 在 Prism 9 返回 `Window`：`protected override Window CreateShell()`。
- 契约注册在 `RegisterTypes`：`containerRegistry.RegisterSingleton<IMessageService, MessageService>();`
- 视图注册：`containerRegistry.RegisterForNavigation<MainView>();`

### Shell 与主内容导航

- **Shell 自带视图模型**：`Shell.xaml` 设 `prism:ViewModelLocator.AutoWireViewModel="True"`，由 Prism 按命名约定自动装配 `ShellViewModel`（Views.Shell -> ViewModels.ShellViewModel），承载应用级状态（标题 / 子标题 / 状态栏）。
- `ShellViewModel` 以 `[ObservableProperty]` 分部属性暴露 `Title`/`SubTitle`/`StatusText`。
- Shell 根元素改用 MahApps.Metro 的 `MetroWindow`（`xmlns:mah="http://metro.mahapps.com/winfx/xaml/controls"`），标题栏通过 `TitleTemplate` 显示 `Title`（主）+ `SubTitle`（次）。
- `ShellViewModel` **不实现 `INavigationAware`**（Shell 是 `CreateShell` 根窗口、非区域导航目标，其 `OnNavigatedTo` 不会自动触发），依赖 `IRegionManager`（DI 注入），提供 `ShellViewModel.Design.cs` 设计器无参构造，XAML 直接 `d:DesignInstance IsDesignTimeCreatable=True`。
- 初始导航（加载 `MainView` 到 `ContentRegion`）由 `ShellViewModel.LoadedCommand` 经 `Shell.xaml` 的 `Interaction.Triggers` 在窗口 `Loaded` 后处理，App 无需重写 `OnInitialized`。

```xml
<i:Interaction.Triggers>
    <i:EventTrigger EventName="Loaded">
        <i:InvokeCommandAction Command="{Binding LoadedCommand}" />
    </i:EventTrigger>
</i:Interaction.Triggers>
```

- `i:InvokeCommandAction` 取自 `Microsoft.Xaml.Behaviors.Wpf`（优先于 Prism 的 `InvokeCommandAction`）。
- `LoadedCommand` 内执行 `regionManager.RequestNavigate("ContentRegion", "MainView")`。

## 全局异常处理 + Serilog（模板内建）

`App.GlobalException.cs` 与 `App.xaml.cs` 已挂钩，无需重写：

- `OnStartup`：先 `ConfigureLogging()` 再 `AttachGlobalExceptionHandlers()`；`OnExit` 里 `Log.CloseAndFlush()`。
- 三钩子：`DispatcherUnhandledException`（UI 线程，记 Error+弹窗+`Handled=true`）、`AppDomain.UnhandledException`（进程级，记 Fatal+弹窗+退出）、`TaskScheduler.UnobservedTaskException`（只记 Error+`SetObserved()`）。
- 日志落盘 **exe 运行目录** `logs\`（`AppContext.BaseDirectory\logs\app-YYYYMMdd.log`），按天滚动、保留 14 天、`shared:true`、UTF-8。运行目录语义 = 程序文件所在目录，不随启动方式（VS / 双击 / dotnet run）漂移；Serilog 自动创建 `logs\` 目录。**注意**：若部署到无写权限目录（如 `Program Files`），写文件会失败——按部署场景改回 `%LOCALAPPDATA%`（注释已写明）。
- 弹窗防重复：`ShowDialogLock`（`System.Threading.Lock`）+ `_isShowingDialog`；后台线程自动调度回 UI。
- **强约束：ViewModel 内不 try-catch，异常一律冒泡到全局收口**；异步加载用 `async void` 让异常直达 Dispatcher 钩子即时弹窗。
- `Application.Current` 须写全限定 `System.Windows.Application.Current`（App 在 `<AppName>` 命名空间下会被解析成 `<AppName>.Application`）。

## View 设计时绑定（强制）

**凡是生成的 View，都必须把 ViewModel 绑到设计时 `DataContext`**（`Window`/`UserControl`/`Page` 全部）。生成 View 时同步：建 ViewModel、在 XAML 根声明 `d:DataContext`、VM 有 DI 依赖时补 `.Design.cs`。

```xml
xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
xmlns:vm="clr-namespace:<AppName>.ViewModels"
mc:Ignorable="d"
d:DesignWidth="880" d:DesignHeight="540"
d:DataContext="{d:DesignInstance Type=vm:MainViewModel, IsDesignTimeCreatable=True}"
```

- `mc:Ignorable="d"` 必须加；属性值写一行。
- VM 有构造依赖：把设计时构造放 `ViewModels/XxxViewModel.Design.cs`（分部类另一半），只填静态示例数据、绝不触碰注入服务，字段 `_service = null!;` 占位，标注 `[Obsolete(...)]`；DI 容器会选参数可解析的构造。无依赖则直接 `IsDesignTimeCreatable=True`。
- `d:*` 编译期被忽略，与 Prism 的 `ViewModelLocator.AutoWireViewModel` 不冲突，可并存。

### 跨程序集 `clr-namespace` 必须带 `;assembly=`

XAML 里 `xmlns:xxx="clr-namespace:<命名空间>"` 指向**当前 WPF 程序集之外**的类型（如 `<AppName>.Domain`/`<AppName>.Application` 的 Model/契约/枚举），必须写成 `clr-namespace:<命名空间>;assembly=<程序集名>`，否则 XAML 只在当前程序集查找会解析失败。同程序集（ViewModels/Converters 等）无需 assembly。

```xml
xmlns:models="clr-namespace:PcMonitor.Domain.Models;assembly=PcMonitor.Domain"  <!-- 跨 DLL：带 assembly -->
xmlns:vm="clr-namespace:PcMonitor.ViewModels"                                    <!-- 同 DLL：不带 -->
```

## Material Design 主题（默认 Material Design 3）

**设计语言默认 MD3**，MD2 仅作遗留兼容（见下方「切换到 MD2」）。MD3 复用 MD2 核心控件库 `MaterialDesignTheme.*`，再叠加 `MaterialDesign3.Defaults.xaml` 映射 MD3 外观。

`App.xaml` 用 `MahAppsBundledTheme`（同时生成 MD 调色板与 MahApps 画刷，Shell 的 MetroWindow 沿用 `AccentColorBrush`/`GlowBrush`），并手动合并 MahApps 基础样式 + MD×MahApps 桥接字典（模板现成写法，照抄即可）：

```xml
<materialDesign:MahAppsBundledTheme BaseTheme="Light"
                                    PrimaryColor="DeepPurple"
                                    SecondaryColor="Lime" />

<!-- MahApps.Metro 基础样式（MetroWindow 窗体必需），必须手动合并 -->
<ResourceDictionary Source="pack://application:,,,/MahApps.Metro;component/Styles/Controls.xaml" />
<ResourceDictionary Source="pack://application:,,,/MahApps.Metro;component/Styles/Fonts.xaml" />

<!-- Material Design 3 默认样式 -->
<ResourceDictionary Source="pack://application:,,,/MaterialDesignThemes.Wpf;component/Themes/MaterialDesign3.Defaults.xaml" />

<!-- Material Design × MahApps 桥接：聚合字典，一次性桥接全部 MahApps 控件样式到 MD 配色 -->
<ResourceDictionary Source="pack://application:,,,/MaterialDesignThemes.MahApps;component/Themes/MaterialDesignTheme.MahApps.Defaults.xaml" />
```

- **`MahAppsBundledTheme`**：`BundledTheme` 的 MahApps 变体，按 `PrimaryColor`/`SecondaryColor` 自动生成 MahApps 画刷（`AccentColorBrush`/`HighlightBrush` 等），无需手工映射。`ColorAdjustment` 子元素（MD3 色调对比开关，属性 `Contrast`/`DesiredContrastRatio`/`Colors`）仍可作为可选子元素追加以微调 MD3 对比度；模板采用最简形式（等效默认 `Contrast="Medium"`）。
- **MahApps 基础样式必须手动合并**：`MahApps.Metro` 的 `Styles/Controls.xaml` + `Styles/Fonts.xaml` 需显式合并（MetroWindow 依赖）；`MaterialDesignThemes.MahApps` 桥接字典会把 MD 配色套到 MahApps 控件，但**不会**替代上面两个基础字典的合并。

### 切换到 MD2（仅遗留兼容）

把 `MaterialDesign3.Defaults.xaml` 换成 `MaterialDesign2.Defaults.xaml` 即可（`MahAppsBundledTheme` 仅留 `BaseTheme`/`PrimaryColor`/`SecondaryColor`，其余 MahApps 基础字典与桥接字典保持不变）。新项目一律用 MD3。

```xml
<materialDesign:MahAppsBundledTheme BaseTheme="Light"
                                    PrimaryColor="DeepPurple"
                                    SecondaryColor="Lime" />
<ResourceDictionary Source="pack://application:,,,/MahApps.Metro;component/Styles/Controls.xaml" />
<ResourceDictionary Source="pack://application:,,,/MahApps.Metro;component/Styles/Fonts.xaml" />
<ResourceDictionary Source="pack://application:,,,/MaterialDesignThemes.Wpf;component/Themes/MaterialDesign2.Defaults.xaml" />
<ResourceDictionary Source="pack://application:,,,/MaterialDesignThemes.MahApps;component/Themes/MaterialDesignTheme.MahApps.Defaults.xaml" />
```

## 技能依赖：material-design-styles（强制）

本脚手架的 Material Design 命名样式清单来自 `material-design-styles` 技能。**每次新建 / 修改 XAML 前，先确认该技能已安装；未安装则按下方说明从市场 `lenfon-marketplace` 安装（不再走 GitHub clone）**：

```bash
# 检查是否已安装（优先市场路径，其次用户级技能目录）
if [ -d "$USERPROFILE/.workbuddy/plugins/marketplaces/lenfon-marketplace/plugins/material-design-styles" ] || \
   [ -d "$USERPROFILE/.workbuddy/skills/material-design-styles" ]; then
  echo "material-design-styles 已安装"
else
  echo "请在 WorkBuddy 中从市场 lenfon-marketplace 安装 material-design-styles 技能"
fi
```

安装方式（均来自市场 `lenfon-marketplace`，二选一）：

- 对话中直接说「**从市场 lenfon-marketplace 安装 material-design-styles 技能**」，由 WorkBuddy 一键安装；
- 或在左侧【技能】面板进入市场，搜索 `material-design-styles` 并安装。

- 安装成功后用 Skill 工具加载 `material-design-styles` 再写 XAML。
- **默认设计语言为 MD3**：命名样式选型优先取 `MaterialDesignTheme.*` 共用键（MD2/MD3 共享基础），MD3 专属组件用 `MaterialDesign3.*` 键；不要用 v4.x 旧键名（见 material-design-styles 技能「已废弃」清单）。
- 技能市场归属：`lenfon-marketplace`（市场仓库 `https://github.com/LenFon/lenfon-marketplace`，插件位于其 `plugins/material-design-styles` 子目录，安装请走市场）。

## 值转换器（强制）

**优先用 `ValueConverters` 包，命中即用，不重复造轮子；所有转换器统一走共享资源字典。**

1. **优先用包**：XAML 命名空间 `xmlns:conv="http://schemas.superdev.ch/valueconverters/2016/xaml"`。常用：`BoolToVisibilityConverter`、`BoolToBrushConverter`、`BoolNegationConverter`、`EnumToBoolConverter`、`NullToBoolConverter`、`StringIsNotNullOrEmptyConverter`、`DateTimeConverter`、`EnumWrapperConverter`、`ValueConverterGroup`、`IsInRangeConverter` 等。语义/参数/目标类型都匹配才叫「合适」（如「bool→Visibility 取反」直接用 `BoolToVisibilityConverter`，不必自写 `InverseBoolToVisibilityConverter`）。
2. **仅以下情况自写**（放 `<AppName>/Converters/`，命名 `XxxConverter`，继承 `IValueConverter`/`IMultiValueConverter`）：① 包中无等价实现；② 需 `ConvertBack` 双向绑定且包不支持；③ 参数/行为差异过大。多转换串联优先用包内 `ValueConverterGroup`。
3. **统一走共享字典**：所有转换器（包提供的或自定义的）集中在 `Resources/Converters.xaml`，View 一律 `StaticResource` 引用。禁止两种写法：① View 内联标记扩展 `{conv:BoolToVisibilityConverter}`；② 单个 View 局部定义 `<conv:... x:Key/>`。

```xml
<!-- Resources/Converters.xaml（已在 App.xaml 全局合并） -->
<conv:BoolToVisibilityConverter x:Key="BoolToVisibilityConverter" />
<conv:BoolNegationConverter    x:Key="BoolNegationConverter" />
<!-- View 里只引用，不声明 xmlns:conv、不写内联 -->
<TextBlock Visibility="{Binding HasError, Converter={StaticResource BoolToVisibilityConverter}}" />
```

- 模板已内置 `Resources/Converters.xaml` 并在 `App.xaml` 合并 → 全应用任意 View 可直接 `StaticResource`。
- 新增自定义转换器：先放 `<AppName>.Converters` 命名空间，再到 `Converters.xaml` 注册一个 `x:Key`。
