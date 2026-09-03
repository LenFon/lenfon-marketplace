# 1. 简介、NuGet 包、示例索引与启动生命周期

> 本文件来自 PrismLibrary/Prism 与 Prism-Samples-Wpf 官方仓库归纳。

## 1.1 简介

**Prism** 是一套用于构建**松耦合、可维护、可测试**的 XAML 应用的框架，内置 MVVM、依赖注入、命令、EventAggregator、Region、导航、对话框等模式。跨平台核心 `Prism.Core` 基于 .NET Standard 2.0，平台相关能力在各平台库中分别实现。

## 1.2 平台支持与 NuGet 包

| 平台 | 主包 | 容器包 |
|---|---|---|
| WPF | `Prism.Wpf` | `Prism.Unity` / `Prism.DryIoc` |
| Avalonia | `Prism.Avalonia` | `Prism.DryIoc.Avalonia` |
| .NET MAUI | `Prism.Maui` | `Prism.DryIoc.Maui` / `Prism.Maui.Rx` |
| Uno / WinUI | `Prism.Uno` | `Prism.DryIoc.Uno.WinUI` |

> ⚠️ 从 v7 起 Prism 改为**按平台/容器分发包**。WPF 项目应直接装 `Prism.Unity` 或 `Prism.DryIoc`（已含 Prism.Wpf + 容器集成），不要再混装独立的 `Prism.Wpf`+`Prism.Unity.Container` 旧组合。容器建议全项目统一（示例多用 Unity / DryIoc）。**只装生产可用稳定版，禁止 preview/alpha/beta/rc。**

## 1.3 官方示例总索引（Prism-Samples-Wpf）

示例建议从 01 起顺序学习，每个建立在上一概念之上。括号内为对应的关键 API。

| # | 主题 | 学到什么 |
|---|---|---|
| 01 | Bootstrapper & Shell | 基础启动器与外壳（`PrismApplication`/`PrismBootstrapper`） |
| 02 | Regions | 声明区域 |
| 03 | Custom Regions | 为 `StackPanel` 写自定义区域适配器 |
| 04 | View Discovery | 按约定自动注入视图 |
| 05 | View Injection | 手动增删视图 |
| 06 | View Activation | 激活/停用视图 |
| 07 | Modules | 模块目录：App.config / Code / Directory / 手动 |
| 08 | ViewModelLocator | 自动绑定 VM |
| 09 | Change Convention | 修改 VM 定位约定 |
| 10 | Custom Registrations | 手动注册 VM |
| 11 | DelegateCommands | `DelegateCommand` / `ObservesXxx` |
| 12 | CompositeCommands | 聚合多个命令 |
| 13 | IActiveAware Commands | 仅活动视图的命令生效 |
| 14 | Event Aggregator | 发布/订阅 |
| 15 | Filtering Events | 订阅时过滤 |
| 16 | RegionContext | 向嵌套区域传数据 |
| 17 | Basic Region Navigation | 基础区域导航 |
| 18 | Navigation Callback | 导航完成回调 |
| 19 | Navigation Participation | 视图/VM 参与导航（`INavigationAware`） |
| 20 | Navigate To Existing Views | 控制导航时的视图实例 |
| 21 | Passing Parameters | 导航传参 |
| 22 | Confirm/Cancel Navigation | 确认或取消导航 |
| 23 | Region Member Lifetime | 控制视图存活期 |
| 24 | Navigation Journal | 前进/后退 |
| 26 | Dialog Service | 对话框服务 |
| 27/28 | Styling / Custom Window | 对话框样式与自定义窗口 |
| 29 | InvokeCommandAction | 交互行为绑定命令 |

## 1.4 核心概念与生命周期

| 概念 | 作用 | 关键类型 |
|---|---|---|
| Shell | 主窗口（组合根），含 Region 占位 | 普通 `Window` |
| Container | 依赖注入，解析 View/VM/服务 | `IContainerRegistry` / `IContainerProvider` |
| BindableBase | 属性变更通知基类 | `SetProperty` |
| ViewModelLocator | 按约定注入 DataContext | `ViewModelLocationProvider` |
| DelegateCommand | ICommand 实现 | `DelegateCommand` / `CompositeCommand` |
| EventAggregator | 弱引用发布/订阅 | `IEventAggregator` / `PubSubEvent<T>` |
| Region | Shell 中可填充的占位区 | `IRegionManager` / `RegionAdapterBase` |
| Navigation | 区域间切视图、传参 | `RequestNavigate` / `INavigationAware` |
| Module | 可插拔功能单元 | `IModule` / `IModuleCatalog` |
| DialogService | 模态弹窗与结果 | `IDialogService` / `IDialogAware` |

**应用启动生命周期：**

```
App.OnStartup → Container 构建 → ConfigureViewModelLocator()
  → RegisterTypes()        // 注册服务/视图/对话框
  → ConfigureModuleCatalog()// 加载模块
  → InitializeModules()
  → CreateShell()          // 解析并展示主窗口
  → 模块 OnInitialized()   // 把视图注册到区域
```

## 1.5 应用启动（PrismApplication）

新版示例一律用 `PrismApplication`（示例 01/07/17/26）：

```csharp
// App.xaml —— 去掉 StartupUri，只保留 x:Class
// App.xaml.cs
public partial class App : PrismApplication
{
    // 创建主窗口（Shell）；用 Container 解析，依赖自动注入
    protected override Window CreateShell() => Container.Resolve<MainWindow>();

    // 组合根：注册所有服务、视图、对话框
    protected override void RegisterTypes(IContainerRegistry containerRegistry) { }

    // 可选：以代码方式加载模块
    protected override void ConfigureModuleCatalog(IModuleCatalog moduleCatalog)
    {
        moduleCatalog.AddModule<ModuleA.ModuleAModule>();
    }
}
```

> 旧式 `PrismBootstrapper`（示例 01 早期写法）：在 `App.OnStartup` 里 `new Bootstrapper().Run();`，Bootstrapper 重写 `CreateShell()` 与 `RegisterTypes()`。新项目直接用 `PrismApplication` 即可，无需自己写 Bootstrapper。
