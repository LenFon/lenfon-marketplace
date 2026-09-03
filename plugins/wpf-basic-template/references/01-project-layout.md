# 项目布局、编码与包管理

## 目录布局（强制）

```
<AppName>/                               <- 解决方案根
├─ <AppName>.slnx                        <- slnx 格式，不用 .sln
├─ Directory.Packages.props              <- CPM，与 slnx 同层
├─ Directory.Build.props                 <- 公共属性，与 slnx 同层
├─ nuget.config                          <- NuGet 源配置（仅官方源）
└─ src/                                  <- 所有项目一律在 src/ 下
   ├─ <AppName>/                         netX.0-windows，WPF 应用（Prism 组合根）
   │  ├─ Views/  ViewModels/
   ├─ <AppName>.Domain/                  netX.0，领域模型
   ├─ <AppName>.Application/             netX.0，契约（接口）
   └─ <AppName>.Infrastructure/          netX.0，实现
```

- **依赖方向**：`<AppName>` → `Infrastructure` → `Application` → `Domain`；WPF 应用作为组合根可直引全部三层。
- **命名空间跟随程序集**：`<AppName>.Domain.Models` / `<AppName>.Application.Services` / `<AppName>.Infrastructure.Services`。
- **目标框架**：类库用 `netX.0`（不带 `-windows`），仅 WPF 应用用 `netX.0-windows`。

建目录骨架：

```bash
mkdir -p <AppName>/src/<AppName>/Views <AppName>/src/<AppName>/ViewModels \
         <AppName>/src/<AppName>.Domain \
         <AppName>/src/<AppName>.Application \
         <AppName>/src/<AppName>.Infrastructure
```

## 文件编码（强制）：纯 UTF-8 无 BOM

所有源文件（`.cs`/`.xaml`/`.csproj`/`.props`/`.config`/`.slnx`/`.xml`/`.json`/`.md`）一律 `utf-8` 存储，不带 BOM、不用 GBK。

- 判定：首字节 `EF BB BF` 是 BOM（应剥离），`FF FE`/`FE FF` 是 UTF-16（应转 UTF-8）。
- 改造既有文件：用 Python 字节级剥离 BOM（`data[3:]`），**勿整文件解码重编码**（本机 DLP 会对非白名单读取器注入坏字节，见 `05-build-verification.md`）。

## 包组合（全部最新稳定版，禁 preview/alpha/beta/rc）

| 包 | 模板内置版本 | 说明 |
|---|---|---|
| Prism.Wpf | 9.0.537 | 模块化 + DI + Region 导航 |
| **Prism.DryIoc** | 9.0.537 | **必选**，版本必须与 Prism.Wpf 一致 |
| CommunityToolkit.Mvvm | 8.4.2 | 源生成器 MVVM |
| MaterialDesignThemes | 5.3.2 | 与 .MahApps 严格同版本 |
| MaterialDesignThemes.MahApps | 5.3.2 | MD × MahApps 桥接字典（MaterialDesignTheme.MahApps.Defaults.xaml），版本必须与 MaterialDesignThemes 一致 |
| **MahApps.Metro** | 2.4.11 | MetroWindow 窗口框架（Shell 改用 MetroWindow）；Styles/Controls.xaml + Styles/Fonts.xaml 须在 App.xaml 手动合并（见 `03-prism-and-ui.md`） |
| Serilog | 4.4.0 | 结构化日志（WPF 应用默认日志方案） |
| Serilog.Sinks.File | 7.0.0 | 文件 sink，按天滚动 |
| **ValueConverters** | 3.1.22 | 常用 IValueConverter 集合（thomasgalliker，开源），转换器首选来源 |
| **Microsoft.Xaml.Behaviors.Wpf** | 1.1.158 | XAML 行为宿主（`Interaction.Triggers` / `EventTrigger` / `InvokeCommandAction`）；优先使用其自带的 `i:InvokeCommandAction` 在事件触发时执行 ViewModel 命令（不依赖 Prism 的 `InvokeCommandAction`） |

建新项目时**先查 nuget.org 拿最新稳定版**再改 `Directory.Packages.props`，勿沿用旧版本号。

## NuGet 源（`nuget.config`，模板随附、放解决方案根）

- **仅官方 `nuget.org`**，不内置任何国内镜像 / 第三方源。
- 需要私有 / 内网源（如公司源）或自行维护的镜像时，在 `<packageSources>` 内追加 `<add key="名称" value="地址"/>`。
- 文件在 `<packageSources>` 首行写了 `<clear />`，排除机器级 / 用户级源（`local`、VS Offline Packages 等），还原行为可复现——仅走本文件显式声明的源；如确需本机其它源参与还原，删掉该 `<clear />` 即可。

## 中央包管理（CPM）

- 版本号集中在 `Directory.Packages.props`，各 csproj 只写 `PackageReference` 不带 `Version`。
- **禁止用 `dotnet add package`**（会把版本写死进 csproj，破坏 CPM）；改版本一律编辑 `Directory.Packages.props`。
