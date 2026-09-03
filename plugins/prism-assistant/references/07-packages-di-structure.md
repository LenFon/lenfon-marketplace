# 7. 依赖注入、推荐目录结构与最佳实践

> 综合 Prism 官方示例与用户 ABP+Prism 分层约定（src/ 分层 + CPM + slnx）。

## 7.1 依赖注入与容器

所有服务/VM 通过构造函数注入，注册集中在 `RegisterTypes`：

```csharp
protected override void RegisterTypes(IContainerRegistry c)
{
    c.Register<IMyService, MyService>();           // 瞬态（每次解析新建）
    c.RegisterSingleton<IAppState, AppState>();     // 单例（全局共享，如 ApplicationCommands）
    c.RegisterScoped<IUnitOfWork, UnitOfWork>();    // 作用域（视容器支持）
    c.RegisterDialog<MyDialog, MyDialogViewModel>();
}
// 解析：Container.Resolve<T>()；构造函数参数由容器自动注入
```

> 容器抽象接口 `IContainerRegistry`（注册）与 `IContainerProvider`（解析）。Unity / DryIoc 均实现，API 一致。模块内也可在 `RegisterTypes(IContainerRegistry)` 注册自己的服务。

## 7.2 推荐目录结构（结合 ABP+Prism 分层）

```
Solution/                 (根：Xxx.slnx + Directory.Build.props + Directory.Packages.props)
├─ src/
│  ├─ MyApp.Wpf/          (组合根，引用所有层；CreateShell、RegisterTypes)
│  ├─ MyApp.Application/  (契约/服务接口 IMyService)
│  ├─ MyApp.Infrastructure/(实现 MyService)
│  └─ MyApp.Domain/       (领域模型)
└─ modules/ (可选)         (各 IModule 独立程序集)
```

> 按用户项目约定：类库目标框架用 `netX.0`（无 `-windows`），仅 WPF 应用用 `netX.0-windows`；启用中央包管理器（CPM）；命名空间跟随程序集。组合根 `MyApp.Wpf` 可直接引用所有层，模块通过 `IModule` 解耦。

## 7.3 Prism 9 命名空间重组（关键坑）

| 类型 | 命名空间 |
|---|---|
| `IRegionManager` / `RegionManager` / `IRegion` / `INavigationAware` / `NavigationContext` | `Prism.Navigation.Regions`（程序集跨 Prism.Core + Prism.Wpf） |
| `NavigationParameters` / `INavigationParameters` / `NavigationResult` | `Prism.Navigation` |
| `BindableBase` / `SetProperty` | `Prism.Mvvm` |
| `DelegateCommand` / `CompositeCommand` | `Prism.Commands` |
| `IEventAggregator` / `PubSubEvent<T>` | `Prism.Events` |
| `IDialogService` / `IDialogAware` / `DialogParameters` / `ButtonResult` | `Prism.Dialogs` |
| `IModule` / `IModuleCatalog` | `Prism.Modularity` |

> 写 `Prism.Regions` 报 CS0234（旧命名空间已迁移）。导航代码须 `using Prism.Navigation.Regions;` + `using Prism.Navigation;`。

## 7.4 最佳实践与常见陷阱

| 要点 | 建议 |
|---|---|
| 启动方式 | 新项目统一用 `PrismApplication`，不要混用旧 Bootstrapper |
| VM 绑定 | 优先用 `AutoWireViewModel="True"`；非常规命名再改约定或手动注册 |
| CanExecute | 优先 `ObservesCanExecute(() => ...)`，避免忘记 `RaiseCanExecuteChanged` |
| 跨模块通信 | 事件聚合用 `PubSubEvent<T>`；UI 线程回调务必 `ThreadOption.UIThread` |
| 事件注销 | `keepSubscriberReferenceAlive:true` 时必须显式 `Unsubscribe` |
| 导航 | 接收参数用 `INavigationAware`；需要「确认离开」实现 `IConfirmNavigationRequest` |
| 对话框 | VM 实现 `IDialogAware`，结果经 `RequestClose` 回传，调用方读 `r.Result` |
| 模块 | 大型系统按业务拆 `IModule`；主壳只组合，不写业务 |
| 依赖 | 服务注册集中到 `RegisterTypes`；单例慎用（注意线程与状态） |
| 包版本 | 只装稳定版，禁止 preview/alpha/beta/rc |

## 7.5 与 wpf-basic-template 脚手架的衔接

- `wpf-basic-template` 已内置 Prism 9 + Material Design 5 + CommunityToolkit.Mvvm 的 `src/` 四层骨架，`Shell` 用 `MetroWindow` + `AutoWireViewModel`、`LoadedCommand` 经 `Interaction.Triggers` 在窗口 `Loaded` 后 `RequestNavigate("ContentRegion","MainView")`。
- 在脚手架基础上加导航页：① `RegisterForNavigation<XxxView>()` 放进模块 `RegisterTypes`；② 目标 VM 实现 `INavigationAware` 收参；③ 跨模块传参用 Application 层 DTO。
- 导航失败时优先查 5.13 避坑清单（未注册 / 区域名不存在 / 未实现 IsNavigationTarget 堆叠 / 确认导航未调 continuationCallback）。
