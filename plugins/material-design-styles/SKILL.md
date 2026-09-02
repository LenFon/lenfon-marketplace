---
name: material-design-styles
description: MaterialDesignInXamlToolkit 命名样式参考与 WPF 控件样式选型指南（基于最新稳定版 v5.3.2）。按 MD2/MD3 分组复用 405 个唯一命名样式（x:Key）清单，覆盖按钮、输入框、卡片等控件变体。当用户在 WPF / Material Design 项目中需要「选样式」「配色」「Raised/Flat/Outlined/FloatingHint/Filled 变体」「MD2 vs MD3」时使用。
agent_created: true
last_verified: "2026-09-02"
---

# MaterialDesign 样式参考 Skill

适用：WPF / MaterialDesignThemes（`.Wpf` 或 `.MahApps`）项目的控件样式选型与 XAML 编写。

## 维护与月度更新流程

本技能**至少每月校验一次**，确保版本信息与样式清单不过时。月度自动化（recurring）会执行以下步骤，手动更新时同理：

1. **核对最新稳定版**：`WebFetch https://www.nuget.org/packages/MaterialDesignThemes/` 提取最新 **稳定** 版本号（忽略 `-ci` / `-alpha` / `-beta` / `-rc` 等预发布）。
2. **比对**：将 NuGet 稳定版与 `frontmatter.last_verified` 旁边记录的版本（当前 v5.3.2）比较。
3. **若推出更新的稳定版**：
   - 更新本文件「版本」小节：新版本号、发布日期、.NET 目标框架、`vX.Y.x` 版本要点。
   - 重新核对 `references/MD样式分类清单.md`：比对 `src/MaterialDesignThemes.Wpf/Themes/` 新增/移除/合并的命名样式键，更新统计表与清单；并为新增键补充「目标类型 / 中文说明 / 继承自」。
   - 更新两处「已移除/合并、禁止再用的旧键名」列表。
   - 同步刷新本文件与 references 头部的「校验版本」。
4. **若无更新稳定版**：仅将 `frontmatter.last_verified` 改为本次校验日期；references 头部「最后校验日期」同步更新，不改动正文。
5. **约束**：只认生产可用稳定版，**绝不**把预发布版写入技能正文；NuGet 强约束与用户授权偏好一致（免费/开源、稳定版）。

> 校验依据：NuGet `MaterialDesignThemes` / `MaterialDesignColors`；样式键来源 `github.com/MaterialDesignInXAML/MaterialDesignInXamlToolkit` → `src/MaterialDesignThemes.Wpf/Themes/`。

## 版本（优先使用最新版）
- **当前校验版本：v5.3.2**（最新稳定版；NuGet `MaterialDesignThemes` / `MaterialDesignColors` 5.3.2，目标框架 **.NET 10**；最后校验 2026-09-02，仍无更新稳定版）。
- 安装：`Install-Package MaterialDesignThemes`（或 `MaterialDesignThemes.MahApps`）。
- 写 XAML 默认以 v5.3.2 的命名样式为准；旧版本（v4.x 及更早）的样式键与本节清单可能不一致，**不要混用旧键名**。
- v5.3.x 要点：v5.3.1 新增 `StatusBar` 默认样式、将 `material-color-utilities` 移植到 dotnet（动态调色板更准）；v5.3.2 为 `Clock` 增加 `MinuteSelectionStep` 属性。
- 已移除/合并、禁止再用的旧键名示例：`MaterialDesignRichTextBox`、`MaterialDesignScrollViewer`、`MaterialDesignWindow`、`MaterialDesignOutlinedComboBox`、`MaterialDesignToolBarToggleButton`、MD3 `NavigationBar*`/`NavigationRail*` 的 ListBox 派生样式、Snackbar 动作按钮变体（`MaterialDesignSnackbarAction*Button`）等。

## 核心约定（长期使用）
凡使用 `MaterialDesignThemes` 创建 WPF 程序，**先看样式参考、再写 XAML**：优先选用命名样式（`x:Key`）以 `StaticResource` 引用，按 MD2/MD3 分组选取合适变体，并遵循对应 `Defaults` 映射。

## 架构要点
- 样式两大类：① 隐式默认样式（仅 `TargetType`、无 `x:Key`，由 `*Defaults.xaml` 自动套用）；② 命名变体样式（带 `x:Key`，需 `StaticResource` 引用）。
- MD3 **不另写控件**，而是「复用 MD2 核心控件库 `MaterialDesignTheme.*`（共享基础）+ 叠加 MD3 专属文件 `MaterialDesign3.*`」。
- 默认外观映射：`MaterialDesign2.Defaults.xaml`(MD2) / `MaterialDesign3.Defaults.xaml`(MD3)。
- 变体派生规律：`Raised` → `Flat` → `Outlined` → `FloatingHint` → `Filled`，辅以 `Mini` / `Reveal`(密码显隐) / `Discrete`(离散刻度) / `Switch`(开关)；可叠加 `Light`/`Dark`/`Primary`/`Secondary` 配色前缀。

## 样式统计（共 405 个唯一命名样式，已对 v5.3.2 去重）
| 分组 | 数量 | 说明 |
|---|---|---|
| MD2 共享核心 | 350 | `MaterialDesignTheme.*` + `MaterialDesign2.Defaults`（MD3 复用的键计入此处） |
| MD3 专属新增 | 28 | `MaterialDesign3.*` 新组件/排版（仅 MD3 文件独有的键） |
| 已废弃 | 25 | `ObsoleteStyles`（Accent 系列） |
| 默认映射 | 2 | `MaterialDesign2.Defaults` / `MaterialDesign3.Defaults` 中的映射键 |

> 注：源码中跨文件同名键已按「主定义文件」归并，故唯一键数（405）小于原始 `<Style x:Key>` 元素总数（446）。框架内部键（`ComponentResourceKey` / `x:Static ...StyleKey`）不计入。

## 完整清单
完整 405 个命名样式（含 样式键 / 目标类型 / 中文说明 / 继承自）见：

`references/MD样式分类清单.md`

用法：命名样式通过 `Style="{StaticResource <Key>}"` 引用。

## 快速选型示例（按钮）
- 实心带阴影：`MaterialDesignRaisedButton`
- 扁平无阴影：`MaterialDesignFlatButton`
- 描边透明底：`MaterialDesignOutlinedButton`
- 悬浮操作：`MaterialDesignFloatingActionButton`（支持 `Mini`/`Dark`/`Light`/`Secondary` 派生）
