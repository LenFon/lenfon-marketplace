---
name: wpf-basic-template
description: 用 lenfon 标准化脚手架新建 WPF 解决方案、项目、View、UserControl 或 ViewModel（Prism 9 + Material Design 5【默认 MD3】+ CommunityToolkit.Mvvm + CPM + slnx + src 四层），scripts/scaffold.py 一键生成（含 .gitignore + git init）。当用户要求新建 WPF 项目、搭解决方案骨架、新增 View / UserControl / ViewModel，或要求套用既有分层与编码约定（C# 13 分部属性、View 设计时绑定、共享转换器字典、CPM 集中版本、slnx 解决方案）时使用本技能。
agent_created: true
---

# WPF 标准解决方案脚手架

lenfon 于 2026-09-01 确立的个人标准模板。新建 WPF 项目一律照此搭建，不要另起炉灶。

## 快速流程

**方式一（推荐）：一键脚手架**

```bash
python scripts/scaffold.py <目标目录> <AppName>
```

一条命令完成：复制 `assets/` 全部模板文件（含 `.gitignore`）→ 占位符 `__APP_NAME__` 替换（内容 + 文件/目录名）→ `git init` + 首次提交（`--no-git` 跳过）→ 打印带 env 前缀的后续 restore/build 命令。

**方式二：手动分步**

1. 复制 `assets/` 下模板文件到新解决方案目录（清单见 `references/06-assets-manifest.md`），并把占位符 `__APP_NAME__` 全局替换为实际项目名（文件名与文件内容都要替换）。
2. 核对 `Directory.Packages.props` 的包版本为 nuget.org 最新**稳定版**（包表见 `references/01-project-layout.md`）：直接运行 `python scripts/check-package-versions.py <项目根>/Directory.Packages.props`（纯标准库，逐包查询 + 成对包版本一致性校验；退出码 0=全部最新 1=存在可升级 2=出错）。**可与第 3 步的 restore 并行执行**——props 已是最新时 restore 不受核对影响，仅在发现可升级时改 props 后重新 build。
3. 直接用 .NET SDK 还原包并编译生成的项目：`dotnet restore && dotnet build --no-restore`，迭代修复到 **0 错 0 警**（验证细则见 `references/05-build-verification.md`）。**Git Bash / PowerShell 宿主下首次 restore 必报 `path1` null**，直接带 env 前缀执行（`HOME` 须为 Windows 反斜杠路径，详见 `references/04-pitfalls.md`）：`env APPDATA='C:\Users\<用户>\AppData\Roaming' HOME='C:\Users\<用户>' PROGRAMFILES='C:\Program Files' dotnet restore`。
4. 新增 View / ViewModel 时套用 `references/03-prism-and-ui.md` 与 `references/02-code-style.md` 的写法。

手动替换占位符（Python；读 `utf-8-sig` 吞模板残留 BOM，写 `utf-8` 无 BOM）：

```python
import pathlib
for p in pathlib.Path('.').rglob('*'):
    if p.is_file():
        p.write_text(p.read_text(encoding='utf-8-sig').replace('__APP_NAME__', 'MyApp'), encoding='utf-8')
```

解决方案文件：优先沿用模板里的 `__APP_NAME__.slnx`（已含「解决方案项」文件夹，挂两个 props + nuget.config）。手动生成时依次执行 `dotnet new sln -n <AppName> --format slnx`、`dotnet sln add <四个 csproj> --solution-folder src`，再在 `<Solution>` 根下补 `<Folder Name="/解决方案项/">` 节点。

## 目录骨架（强制）

```
<AppName>/
├─ <AppName>.slnx             <- slnx 格式，不用 .sln
├─ Directory.Packages.props   <- CPM，与 slnx 同层
├─ Directory.Build.props      <- 公共属性，与 slnx 同层
├─ nuget.config               <- NuGet 源配置（仅官方源）
└─ src/                       <- 所有项目一律在 src/ 下
   ├─ <AppName>/                  netX.0-windows，WPF 应用（Prism 组合根）
   │  ├─ Views/  ViewModels/
   ├─ <AppName>.Domain/           netX.0，领域模型
   ├─ <AppName>.Application/      netX.0，契约（接口）
   └─ <AppName>.Infrastructure/   netX.0，实现
```

依赖方向：`<AppName>` → `Infrastructure` → `Application` → `Domain`；WPF 应用作为组合根可直引三层。完整约定见 `references/01-project-layout.md`。

## 强制约定速查

| 约定 | 要求 | 详情 |
|---|---|---|
| `[ObservableProperty]` | 一律 C# 13 分部属性 `public partial T X { get; set; }`，禁私有字段老写法；生成后跑自检脚本 | `02-code-style.md` |
| 文件编码 | 纯 UTF-8 无 BOM，禁 GBK / UTF-16 | `01-project-layout.md` |
| 包管理 | CPM 集中版本，禁 `dotnet add package`；只装稳定版，禁 preview/alpha/beta/rc | `01-project-layout.md` |
| 注释 | XML 文档注释多行展开；解释性 `//` 注释置于变量 / 字段上方，禁行尾跟随 | `02-code-style.md` |
| 变量 | 类型可推断时一律 `var` | `02-code-style.md` |
| 线程锁 | `System.Threading.Lock`（net9+） | `02-code-style.md` |
| Prism | `Prism.Wpf` + `Prism.DryIoc` 版本严格一致；Region 类型在 `Prism.Navigation.Regions` | `03-prism-and-ui.md`、`04-pitfalls.md` |
| 主题 | 默认 MD3（`MaterialDesign3.Defaults.xaml`）+ `MahAppsBundledTheme`（Shell 用 MetroWindow） | `03-prism-and-ui.md` |
| View | 根元素必做设计时绑定 `d:DataContext` + `mc:Ignorable="d"`；VM 有 DI 依赖补 `XxxViewModel.Design.cs`，并在其设计器无参构造首行给注入字段 `_xxx = null!;` 占位（否则 CS8618，破坏 0 警） | `03-prism-and-ui.md` |
| XAML 跨 DLL 命名空间 | 写成 `clr-namespace:X;assembly=Y`，同程序集不带 assembly | `03-prism-and-ui.md` |
| 转换器 | 优先用 `ValueConverters` 包，统一注册到 `Resources/Converters.xaml`，禁 View 内联定义 | `03-prism-and-ui.md` |
| 异常 | ViewModel 内不 try-catch，异常冒泡到全局三钩子收口 | `03-prism-and-ui.md` |
| 编译 | 必须 0 错 0 警；直接用 .NET SDK `dotnet restore && dotnet build` 验证（Git Bash / PowerShell 下 restore 须带 env 前缀，见快速流程第 4 步） | `05-build-verification.md` |

## 资源索引

| 资源 | 内容 |
|---|---|
| `references/01-project-layout.md` | 目录布局、文件编码、包组合、NuGet 源、CPM |
| `references/02-code-style.md` | 分部属性 + 自检脚本、XML 注释、单行注释位置、var、线程锁 |
| `references/03-prism-and-ui.md` | Prism 引导、Shell 导航、全局异常 + Serilog、MD3 主题、设计时绑定、值转换器 |
| `references/04-pitfalls.md` | 已踩坑位与解法（Prism 9 命名空间、CA1416、DLP 加密、git push 挂起等） |
| `references/05-build-verification.md` | 直接用 .NET SDK `dotnet restore && dotnet build` 验证编译 0 错要求 |
| `references/06-assets-manifest.md` | 模板文件清单 + 技能维护约定 |
| `scripts/check-package-versions.py` | CPM 包版本核对脚本（逐包查 nuget.org 最新稳定版 + 成对包一致性校验，纯标准库） |
| `scripts/scaffold.py` | 一键脚手架：复制 assets → 替换占位符（内容+文件名）→ git init + 首次提交 → 打印 env 前缀的 restore/build 命令（用法见快速流程方式一） |
| `assets/` | 26 个可直接拷贝的模板文件（slnx / 两个 props / nuget.config / .gitignore / src 四层） |

## 依赖技能

写 XAML 前先加载 `material-design-styles`（同一市场 `lenfon-marketplace`）查命名样式键；未安装则先从市场安装，再写 XAML。详见 `references/03-prism-and-ui.md`。
