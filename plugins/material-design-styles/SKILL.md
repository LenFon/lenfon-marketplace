---
name: material-design-styles
description: MaterialDesignInXamlToolkit 命名样式（x:Key）参考与 WPF 控件样式选型指南，锁定最新稳定版 v5.3.2，按 MD2 / MD3 分组收录 405 个唯一命名样式（含目标类型、中文说明、继承自）。当用户在 WPF / Material Design 项目中需要选控件样式、做配色、决定 Raised / Flat / Outlined / FloatingHint / Filled 变体、判断 MD2 与 MD3 用法差异，或排查样式键不存在时使用本技能。
agent_created: true
last_verified: "2026-09-02"
---

# MaterialDesign 命名样式选型

适用：WPF / MaterialDesignThemes（`.Wpf` 或 `.MahApps`）项目的控件样式选型与 XAML 编写。

## 选型流程

1. 确认设计语言：默认 MD3，遗留项目才用 MD2。
2. 按控件与变体查 `references/MD样式分类清单.md`，取样式键（清单含目标类型、中文说明、继承自）。
3. 以 `Style="{StaticResource <Key>}"` 引用：基础控件用 MD2/MD3 共用的 `MaterialDesignTheme.*` 键，MD3 专属组件用 `MaterialDesign3.*` 键。
4. 校验键名不在「已移除 / 合并」清单内、且属于当前校验版本，避免套用 v4.x 旧键。

完整清单（405 个唯一命名样式，按 MD2 共享核心 / MD3 专属 / 已废弃 / 默认映射分组）与统计表见 `references/MD样式分类清单.md`。

## 版本状态

- **当前校验版本：v5.3.2**（最新稳定版；NuGet `MaterialDesignThemes` / `MaterialDesignColors` 5.3.2，目标框架 **.NET 10**；最后校验 2026-09-02，仍无更新稳定版）。
- 安装：`Install-Package MaterialDesignThemes`（或 `MaterialDesignThemes.MahApps`）。
- 写 XAML 一律以 v5.3.2 的命名样式为准，**不要混用旧版本键名**。
- v5.3.x 要点：v5.3.1 新增 `StatusBar` 默认样式、将 `material-color-utilities` 移植到 dotnet（动态调色板更准）；v5.3.2 为 `Clock` 增加 `MinuteSelectionStep` 属性。
- 已移除 / 合并、禁止再用的旧键名示例：`MaterialDesignRichTextBox`、`MaterialDesignScrollViewer`、`MaterialDesignWindow`、`MaterialDesignOutlinedComboBox`、`MaterialDesignToolBarToggleButton`、MD3 `NavigationBar*` / `NavigationRail*` 的 ListBox 派生样式、Snackbar 动作按钮变体（`MaterialDesignSnackbarAction*Button`）等。

## 架构要点

- 样式两大类：① 隐式默认样式（仅 `TargetType`、无 `x:Key`，由 `*Defaults.xaml` 自动套用）；② 命名变体样式（带 `x:Key`，需 `StaticResource` 引用）。
- MD3 **不另写控件**，而是「复用 MD2 核心控件库 `MaterialDesignTheme.*` + 叠加 MD3 专属文件 `MaterialDesign3.*`」。
- 默认外观映射：`MaterialDesign2.Defaults.xaml`（MD2）/ `MaterialDesign3.Defaults.xaml`（MD3）。
- 变体派生规律：`Raised` → `Flat` → `Outlined` → `FloatingHint` → `Filled`，辅以 `Mini` / `Reveal`（密码显隐）/ `Discrete`（离散刻度）/ `Switch`（开关）；可叠加 `Light` / `Dark` / `Primary` / `Secondary` 配色前缀。

## 常用按钮变体

- 实心带阴影：`MaterialDesignRaisedButton`
- 扁平无阴影：`MaterialDesignFlatButton`
- 描边透明底：`MaterialDesignOutlinedButton`
- 悬浮操作：`MaterialDesignFloatingActionButton`（支持 `Mini` / `Dark` / `Light` / `Secondary` 派生）

## 维护

执行月度版本校验 / 更新前，先加载 `references/维护与月度更新.md`，按其步骤核对 NuGet 稳定版并同步清单。
