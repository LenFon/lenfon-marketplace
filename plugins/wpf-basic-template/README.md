# wpf-basic-template

WorkBuddy 技能：**WPF 标准解决方案脚手架**（含 25 个可拷贝模板文件）。

基于真实项目 WeatherApp 全链路验证，一键生成 Prism 9 + Material Design 5（默认 MD3 样式）+ CommunityToolkit.Mvvm 的 WPF 解决方案骨架。

## 特性

| 项 | 说明 |
|---|---|
| 框架 | Prism 9（模块化 + DI + Region 导航）+ Material Design 5（**默认 MD3 样式**，MaterialDesignThemes） |
| MVVM | CommunityToolkit.Mvvm 8.4.2，**凡 `[ObservableProperty]` 一律 C# 13 分部属性**（`[ObservableProperty] public partial string Title { get; set; }`），禁私有字段老写法，含生成后自检脚本 |
| 结构 | src/ 四层：`App`（组合根）→ `Infrastructure`（实现）→ `Application`（契约）→ `Domain`（领域模型） |
| 包管理 | 中央包管理（CPM）：`Directory.Packages.props` 集中 10 个包版本 + `nuget.config`（仅官方源，含 `<clear />`） |
| 解决方案 | `.slnx`（XML 格式），`Directory.Build.props` / `Directory.Packages.props` / `nuget.config` 挂在「解决方案项」文件夹 |
| 日志 | Serilog + Serilog.Sinks.File，全局异常三钩子 |
| 设计时 | 所有 View 根元素强制 `d:DataContext` 设计时绑定（含设计器专用无参构造分部类） |
| 质量 | 两轮编译验证 0 错 0 警（XAML 侧 + 纯 C# 侧） |

## 安装方式（通过 lenfon-marketplace 市场安装）

本技能收录于用户市场 **lenfon-marketplace**（GitHub 仓库 `https://github.com/LenFon/lenfon-marketplace`），推荐通过 WorkBuddy 市场一键安装：

1. 在 WorkBuddy 对话中发送安装指令，例如：

   > 请添加插件市场 https://github.com/LenFon/lenfon-marketplace ，并安装、启用其中的 wpf-basic-template 技能。

   或直接描述需求（如"从市场 lenfon-marketplace 安装 wpf-basic-template 技能"），WorkBuddy 会自动从市场拉取并安装到用户级技能目录。
2. 重启 WorkBuddy（或新开会话）使技能生效。
3. 在左侧【技能】面板可看到 `wpf-basic-template`，对话输入「用 wpf-basic-template 技能新建一个 WPF 项目」即可使用。

**更新技能**：对话中再次发送市场安装指令即可拉取最新版（或进入技能目录执行 `git pull`）。

> **说明**：安装来源为市场仓库 `https://github.com/LenFon/lenfon-marketplace`（插件位于其 `plugins/wpf-basic-template` 子目录），不再使用独立的 `wpf-basic-template` 仓库地址。

## 使用方式

在 WorkBuddy 对话中触发：

```
用 wpf-basic-template 技能新建一个 WPF 项目
```

或手动使用：

1. 将 `templates/` 下 25 个文件拷入新项目目录（`__APP_NAME__` 占位符全局替换为实际项目名）
2. 生成 slnx：`dotnet new sln -n <名称> --format slnx`
3. `dotnet restore && dotnet build --no-restore`

## 模板结构

```
templates/
├── __APP_NAME__.slnx                 # 解决方案（4 项目在 /src/）
├── Directory.Build.props             # LangVersion / Nullable / ImplicitUsings
├── Directory.Packages.props          # CPM，10 个包版本集中管理
├── nuget.config                      # NuGet 源：仅官方源 + <clear />（还原可复现）
└── src/
    ├── __APP_NAME__/                 # WPF 应用（Prism 引导 + MD3 主题 + Serilog）
    │   ├── App.xaml(.cs)             # Prism + DI 容器
    │   ├── App.GlobalException.cs    # 全局异常三钩子
    │   ├── Views/Shell.xaml(.cs)     # 主窗口（Shell）：AutoWireViewModel=True 注入 ShellViewModel，含 ContentRegion + 状态栏
    │   ├── Views/MainView.xaml(.cs)  # 主内容视图（区域导航加载到 ContentRegion）
    │   └── ViewModels/               # ShellViewModel（[RelayCommand] LoadedCommand 导航 MainView，由 Shell.xaml 的 Interaction.Triggers 在 Loaded 时触发，依赖 IRegionManager，配 ShellViewModel.Design.cs，含 Title/SubTitle/StatusText）+ MainViewModel（分部属性 + RelayCommand + INavigationAware + 设计器构造）
    ├── __APP_NAME__.Domain/          # 领域模型（MessageItem 示例）
    ├── __APP_NAME__.Application/     # 契约（IMessageService 示例）
    └── __APP_NAME__.Infrastructure/  # 实现（MessageService 示例）
```

## 坑位清单（已沉淀进 SKILL.md）

- Prism 9 命名空间重组：Region 类型在 `Prism.Navigation.Regions`，`NavigationParameters` 在 `Prism.Navigation`
- Material Design 5 无 `ProgressRing` 控件，用标准 `ProgressBar` + `MaterialDesignCircularProgressBar` 样式
- 密码绑定用 MD 官方附加属性 `PasswordBoxAssist.Password`（双向写回）
- 本机 DLP 加密环境下，编译验证需在临时目录跑（Stubs.cs 占位方案）

## 许可证

[MIT](LICENSE) © 2026 lenfon
