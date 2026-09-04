# 模板文件清单与维护约定

## assets/ 下 25 个模板文件

| 文件 | 说明 |
|---|---|
| `__APP_NAME__.slnx` | 解决方案（4 项目在 `/src/`；两 props + nuget.config 挂在 `/解决方案项/` 下） |
| `Directory.Build.props` | `LangVersion` / `Nullable` / `ImplicitUsings` |
| `Directory.Packages.props` | CPM，10 个包版本集中管理 |
| `nuget.config` | NuGet 源：仅官方 `nuget.org`（详见 `01-project-layout.md`） |
| `src/__APP_NAME__/__APP_NAME__.csproj` | WPF 应用，10 个包 + 3 个项目引用 |
| `src/__APP_NAME__/App.xaml` / `.cs` | Prism 引导 + MD 主题 + Serilog/全局异常挂钩 |
| `src/__APP_NAME__/App.GlobalException.cs` | 全局异常三钩子 + Serilog 配置（App 分部类） |
| `src/__APP_NAME__/AssemblyInfo.cs` | `SupportedOSPlatform` + `ThemeInfo` |
| `src/__APP_NAME__/Resources/Converters.xaml` | 共享值转换器字典（App.xaml 全局合并，View 用 `StaticResource`） |
| `src/__APP_NAME__/Views/Shell.xaml` / `.cs` | 主窗口（Shell），`AutoWireViewModel=True` 自动装配 `ShellViewModel`；含 `ContentRegion` + 状态栏 |
| `src/__APP_NAME__/Views/MainView.xaml` / `.cs` | 主内容视图（区域导航加载到 `ContentRegion`） |
| `src/__APP_NAME__/ViewModels/ShellViewModel.cs` | Shell 视图模型：应用级状态 + `[RelayCommand] LoadedCommand`（窗口 Loaded 后导航加载 MainView）；依赖 `IRegionManager`，配 `ShellViewModel.Design.cs` |
| `src/__APP_NAME__/ViewModels/ShellViewModel.Design.cs` | 设计器专用无参构造（对应 `IRegionManager` 依赖） |
| `src/__APP_NAME__/ViewModels/MainViewModel.cs` | `[ObservableProperty]` 全量分部属性 + RelayCommand 示例；实现 `INavigationAware`（导航页 ViewModel 标准做法） |
| `src/__APP_NAME__/ViewModels/MainViewModel.Design.cs` | 设计器专用无参构造 + 示例数据 |
| `src/__APP_NAME__.Domain/*` | csproj + `MessageItem.cs` + `MessageItem.Impl.cs` |
| `src/__APP_NAME__.Application/*` | csproj + `IMessageService.cs` |
| `src/__APP_NAME__.Infrastructure/*` | csproj + `MessageService.cs` |

示例业务（消息列表）只是占位，按实际需求替换，但**结构与写法保持不变**。

## 维护约定（强制）

- **版本核对按需进行，不设定期巡检**：每次新建项目时（SKILL.md 快速流程第 3 步）核对 `01-project-layout.md`「包组合」全部包的最新【稳定版】，有新版则同步 `SKILL.md` 索引、`assets/Directory.Packages.props`、`assets/src/__APP_NAME__/__APP_NAME__.csproj`。**更新后无需推送 GitHub**，本地保留即可。
- **只取稳定版**：禁 preview/alpha/beta/rc；成对包（Prism 双包、MD 双包）版本严格一致。
- 坑位与写法变更即时手动更新，不等待任何定时任务。
- 任何改动遵循本技能约定（CPM 集中管版本、csproj 不带 Version、纯 UTF-8 无 BOM、共享转换器字典、跨 DLL 命名空间带 `;assembly=`），保持与模板一致。

## 技能本体维护约定

- SKILL.md 保持精简（快速流程 + 强制约定速查 + 资源索引），详细规则一律沉到 `references/`；新增内容优先加 references 并在 SKILL.md 索引表里补一行。
- frontmatter 的 `name` / `description` 决定技能何时被触发，改动后须保证 description 仍明确写出「新建 WPF 项目 / 解决方案骨架 / View / UserControl」等触发场景。
