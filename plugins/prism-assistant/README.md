# prism-assistant

WorkBuddy 技能：**Prism for WPF 使用参考助手**。

沉淀自 github.com/PrismLibrary/Prism 与 Prism-Samples-Wpf 官方仓库（示例 01–29）的真实源码归纳，覆盖 MVVM、ViewModelLocator、DelegateCommand、CompositeCommand、EventAggregator、Region、Region Navigation、Modules、DialogService、依赖注入等全部核心模块。所有 C#/XAML 片段均来自仓库原文。

## 特性

| 项 | 说明 |
|---|---|
| 内容来源 | PrismLibrary/Prism（README、NuGet 包说明）+ Prism-Samples-Wpf（01/03/07/08/09/10/11/12/14/15/17/18/19/20/21/22/23/24/26/29 等示例真实源码） |
| MVVM | `BindableBase` / `SetProperty`、`ViewModelLocator`（含自定义约定 09/手动注册 10）、`DelegateCommand`（ObservesProperty/ObservesCanExecute）、`CompositeCommand` + `IActiveAware` |
| 导航 | 深度覆盖：注册四重载、RequestNavigate 三形态、INavigationAware 三方法、参数传递、完成回调、IConfirmNavigationRequest、IRegionMemberLifetime、IRegionNavigationJournal，含生命周期全景图与 12 条避坑清单 |
| 模块化 | `IModule` 完整实现 + 四种加载方式（代码/App.config/目录/手动）对照 |
| 通信 | `EventAggregator`（PubSubEvent、ThreadOption、filter 订阅） |
| 对话框 | `IDialogService` / `IDialogAware` 四成员 + 真实 XAML |
| 适配 | 结合用户 ABP+Prism 分层（`src/` 分层 + CPM + slnx）给出落地建议 |

## 安装方式

本技能收录于用户市场 **lenfon-marketplace**（GitHub 仓库 `https://github.com/LenFon/lenfon-marketplace`），安装方式如下：

1. 在 WorkBuddy 对话中发送安装指令，例如：

   > 请添加插件市场 https://github.com/LenFon/lenfon-marketplace ，并安装、启用其中的 prism-assistant 技能。

   或直接描述需求（如"从市场 lenfon-marketplace 安装 prism-assistant 技能"），WorkBuddy 会自动从市场拉取并安装到用户级技能目录。
2. 在左侧【技能】面板可看到 `prism-assistant`。

**更新技能**：对话中再次发送市场安装指令即可拉取最新版（或进入技能目录执行 `git pull`）。

## 使用方式

在 WorkBuddy 对话中触发（涉及 Prism 的 WPF 开发任务时，WorkBuddy 会自动参考本技能）：

```
用 prism-assistant 查证 Prism Region Navigation 的 INavigationAware 用法
```

或手动查阅 `references/` 下分主题 Markdown 文档（人类可读带样式版见 `assets/` 下两个 HTML 指南）。

## 与 wpf-basic-template 的关系

- `wpf-basic-template`：WPF 标准脚手架，直接产出可编译项目（Prism 9 + Material Design 5 + CommunityToolkit.Mvvm + CPM + slnx）。
- `prism-assistant`：Prism 框架知识参考，遇到用法细节/排错时查阅。

两者互补：先用 wpf-basic-template 搭骨架，再用 prism-assistant 查细节。

## 许可证

[MIT](LICENSE) © 2026 lenfon
