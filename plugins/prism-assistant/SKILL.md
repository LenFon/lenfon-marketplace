---
name: prism-assistant
description: Prism for WPF 框架使用参考助手，沉淀自官方 PrismLibrary/Prism 与 Prism-Samples-Wpf 示例（01–29）的真实源码，覆盖 MVVM、ViewModelLocator、DelegateCommand、CompositeCommand、EventAggregator、Region、Region Navigation、Modules、DialogService 与依赖注入。当用户用 Prism 做 WPF 开发、需要权威用法与真实代码片段、排查导航失败 / 视图堆叠 / 模块未加载 / 对话框不关闭等问题，或要把 Prism 接入 ABP + Prism 分层项目时使用本技能。
agent_created: true
---

# Prism for WPF 使用参考助手

内容沉淀自 `github.com/PrismLibrary/Prism` 与 `Prism-Samples-Wpf` 官方仓库（示例 01–29）的真实源码，所有 C# / XAML 片段均来自仓库 master 分支原文，未改写。

## 使用流程

1. 按下表定位主题，**只加载需要的 `references/` 文件**，避免一次性全量载入上下文。
2. 参照文件内的真实源码片段落地实现，勿凭记忆改写 API。
3. 涉及导航 / 模块化问题时，先用下方「核心规则速记」自查，再查 references 细节。

| 主题 | 文件 |
|---|---|
| 概览 / NuGet 包 / 示例索引 / 启动生命周期 | `references/01-overview.md` |
| MVVM、`ViewModelLocator`、`DelegateCommand`、`CompositeCommand`、`IActiveAware` | `references/02-mvvm-commands.md` |
| `EventAggregator`（跨模块通信、线程、过滤） | `references/03-eventaggregator.md` |
| `Regions`（含自定义适配器）、`Modules` 四种加载 | `references/04-regions-modules.md` |
| `Region Navigation` 深度（注册 / 发起 / `INavigationAware` / 参数 / 回调 / 确认 / KeepAlive / Journal） | `references/05-navigation.md` |
| `DialogService`（`IDialogAware`）、`Interactivity`（`InvokeCommandAction`） | `references/06-dialogs-interactivity.md` |
| 依赖注入、推荐目录结构、最佳实践与陷阱 | `references/07-packages-di-structure.md` |

人类可读的带样式版本见 `assets/Prism-WPF-Guide.html` 与 `assets/Prism-Navigation-Guide.html`。

## 核心规则速记（导航）

1. 视图须先 `RegisterForNavigation` 后 `RequestNavigate`，否则 `Success=false` 且 `Exception` 提示未找到视图。
2. 不实现 `IsNavigationTarget` → 每次导航都新建实例，`Region.Views` 无限堆叠（内存泄漏）。
3. 确认导航必须调用 `continuationCallback`，否则导航卡死。
4. 只有 `RequestNavigate` 写 Journal，View Injection / Activation 不产生前进 / 后退历史。
5. `KeepAlive=false` 离开即销毁，与 `IsNavigationTarget` 语义需一致。
6. 跨模块传参优先用 Id / DTO（Application 层契约），勿直接传 UI 元素。

详细规则与真实代码见 `references/05-navigation.md`。

## 项目约定（与用户项目一致）

- WPF 装 `Prism.Unity` 或 `Prism.DryIoc`（已含 Prism.Wpf），版本严格一致；只装稳定版，禁 preview / alpha / beta / rc。
- Prism 9 命名空间重组：`Region` 类型在 `Prism.Navigation.Regions`，`NavigationParameters` 在 `Prism.Navigation`（详见 `references/05-navigation.md`）。
- 结合 ABP + Prism 分层：组合根（WPF 应用）放 `CreateShell` / `RegisterTypes`；模块按业务拆 `IModule`；导航参数优先用 Application 层契约 DTO。
- 与 `wpf-basic-template` 技能互补：先用 `wpf-basic-template` 搭骨架，遇到 Prism 用法细节再查本技能。
