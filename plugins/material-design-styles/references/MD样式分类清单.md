# MaterialDesignInXamlToolkit 公开命名样式 · 按 Material Design 2.0 / 3.0 分类

> 来源：`github.com/MaterialDesignInXAML/MaterialDesignInXamlToolkit` → `src/MaterialDesignThemes.Wpf/Themes/`。
> 校验版本：**v5.3.2**（最新稳定版；NuGet `MaterialDesignThemes` / `MaterialDesignColors` 5.3.2，目标框架 .NET 10）。
> 最后校验日期：**2026-09-02**（NuGet 最新稳定版仍为 5.3.2；5.3.2 之后仅有 `5.3.3-ci` 预发布，未纳入）。
> 范围：**仅含命名样式（`x:Key`）**，按源文件/设计语言分组；已剔除隐式默认样式与框架内部键（`ComponentResourceKey` / `x:Static ...StyleKey`）。跨文件同名键按「主定义文件」归并（MD3 复用 MD2 核心的键计入 MD2）。
>
> **架构要点**：MD3 **复用**同一套 `MaterialDesignTheme.*` 核心控件库（即 A 部分，MD2 经典设计，也是 MD3 的共享基础），再叠加 `MaterialDesign3.*` **专属新增**文件（B 部分）。

## 速览

| 设计语言 | 命名样式数 | 说明 |
|---|---|---|
| **Material Design 2.0**（经典 / 共享核心） | 350 | `MaterialDesignTheme.*` 核心控件库 + `MaterialDesign2.Defaults` |
| **Material Design 3.0**（专属新增） | 28 | `MaterialDesign3.*` 新增组件/排版 + `MaterialDesign3.Defaults` |
| 已废弃（非 2.0/3.0） | 25 | `ObsoleteStyles`（Accent 系列等） |
| 默认映射 | 2 | `MaterialDesign2.Defaults` / `MaterialDesign3.Defaults` |
| **合计（去重后唯一命名样式）** | **405** | |

> 用法：命名样式 `Style="{StaticResource <Key>}"`。MD3 默认外观由 `MaterialDesign3.Defaults.xaml` 映射，MD2 由 `MaterialDesign2.Defaults.xaml` 映射。
>
> **v5.3.x 版本要点（优先使用最新版）**：v5.3.1 新增 `StatusBar` 默认样式，并将 `material-color-utilities` 移植到 dotnet（动态调色板更准）；v5.3.2 为 `Clock` 增加 `MinuteSelectionStep` 属性。下列旧命名样式已在 v5.x 中移除/合并，请勿再用：`MaterialDesignRichTextBox`、`MaterialDesignScrollViewer`、`MaterialDesignWindow`、`MaterialDesignOutlinedComboBox`、`MaterialDesignToolBarToggleButton`、MD3 `NavigationBar*`/`NavigationRail*` 的 ListBox 派生样式、Snackbar 动作按钮变体（`MaterialDesignSnackbarAction*Button`）等。

## A. Material Design 2.0（经典 / 共享核心）

### 默认映射 MD2 Defaults  _(2 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignDarkSeparator` | Separator | 深色变体；分隔线；深色分隔线 | MaterialDesignSeparator |
| `MaterialDesignLightSeparator` | Separator | 浅色变体；分隔线；浅色分隔线 | MaterialDesignSeparator |

### 按钮 Buttons  _(47 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `FocusVisual` | — | 命名样式 | — |
| `MaterialDesignRaisedButton` | ButtonBase | 凸起实心(带阴影) | — |
| `MaterialDesignRaisedLightButton` | ButtonBase | 凸起实心(带阴影)；浅色变体 | MaterialDesignRaisedButton |
| `MaterialDesignRaisedDarkButton` | ButtonBase | 凸起实心(带阴影)；深色变体 | MaterialDesignRaisedButton |
| `MaterialDesignRaisedSecondaryButton` | ButtonBase | 凸起实心(带阴影)；辅助色变体 | MaterialDesignRaisedButton |
| `MaterialDesignRaisedSecondaryLightButton` | ButtonBase | 凸起实心(带阴影)；浅色变体；辅助色变体 | MaterialDesignRaisedButton |
| `MaterialDesignRaisedSecondaryDarkButton` | ButtonBase | 凸起实心(带阴影)；深色变体；辅助色变体 | MaterialDesignRaisedButton |
| `MaterialDesignFlatButton` | ButtonBase | 扁平(无阴影) | — |
| `MaterialDesignFlatLightButton` | ButtonBase | 扁平(无阴影)；浅色变体 | MaterialDesignFlatButton |
| `MaterialDesignFlatDarkButton` | ButtonBase | 扁平(无阴影)；深色变体 | MaterialDesignFlatButton |
| `MaterialDesignFlatSecondaryButton` | ButtonBase | 扁平(无阴影)；辅助色变体 | MaterialDesignFlatButton |
| `MaterialDesignFlatSecondaryLightButton` | ButtonBase | 扁平(无阴影)；浅色变体；辅助色变体 | MaterialDesignFlatSecondaryButton |
| `MaterialDesignFlatSecondaryDarkButton` | ButtonBase | 扁平(无阴影)；深色变体；辅助色变体 | MaterialDesignFlatSecondaryButton |
| `MaterialDesignFlatLightBgButton` | ButtonBase | 扁平(无阴影)；浅色变体 | MaterialDesignRaisedLightButton |
| `MaterialDesignFlatMidBgButton` | ButtonBase | 扁平(无阴影) | MaterialDesignRaisedButton |
| `MaterialDesignFlatDarkBgButton` | ButtonBase | 扁平(无阴影)；深色变体 | MaterialDesignRaisedDarkButton |
| `MaterialDesignFlatSecondaryLightBgButton` | ButtonBase | 扁平(无阴影)；浅色变体；辅助色变体 | MaterialDesignRaisedSecondaryLightButton |
| `MaterialDesignFlatSecondaryMidBgButton` | ButtonBase | 扁平(无阴影)；辅助色变体 | MaterialDesignRaisedSecondaryButton |
| `MaterialDesignFlatSecondaryDarkBgButton` | ButtonBase | 扁平(无阴影)；深色变体；辅助色变体 | MaterialDesignRaisedSecondaryDarkButton |
| `MaterialDesignOutlinedButton` | ButtonBase | 描边(透明底+边框) | MaterialDesignFlatButton |
| `MaterialDesignOutlinedLightButton` | ButtonBase | 描边(透明底+边框)；浅色变体 | MaterialDesignOutlinedButton |
| `MaterialDesignOutlinedDarkButton` | ButtonBase | 描边(透明底+边框)；深色变体 | MaterialDesignOutlinedButton |
| `MaterialDesignOutlinedSecondaryButton` | ButtonBase | 描边(透明底+边框)；辅助色变体 | MaterialDesignOutlinedButton |
| `MaterialDesignOutlinedSecondaryLightButton` | ButtonBase | 描边(透明底+边框)；浅色变体；辅助色变体 | MaterialDesignOutlinedSecondaryButton |
| `MaterialDesignOutlinedSecondaryDarkButton` | ButtonBase | 描边(透明底+边框)；深色变体；辅助色变体 | MaterialDesignOutlinedSecondaryButton |
| `MaterialDesignToolButton` | ButtonBase | 按钮；工具 | MaterialDesignFlatButton |
| `MaterialDesignToolForegroundButton` | ButtonBase | 按钮；工具；前景 | MaterialDesignToolButton |
| `MaterialDesignFloatingActionMiniButton` | ButtonBase | 悬浮操作按钮FAB；操作按钮；迷你尺寸 | — |
| `MaterialDesignFloatingActionButton` | ButtonBase | 悬浮操作按钮FAB；操作按钮 | MaterialDesignFloatingActionMiniButton |
| `MaterialDesignFloatingActionMiniLightButton` | ButtonBase | 悬浮操作按钮FAB；操作按钮；浅色变体；迷你尺寸 | MaterialDesignFloatingActionMiniButton |
| `MaterialDesignFloatingActionMiniDarkButton` | ButtonBase | 悬浮操作按钮FAB；操作按钮；深色变体；迷你尺寸 | MaterialDesignFloatingActionMiniButton |
| `MaterialDesignFloatingActionMiniSecondaryButton` | ButtonBase | 悬浮操作按钮FAB；操作按钮；辅助色变体；迷你尺寸 | MaterialDesignFloatingActionMiniButton |
| `MaterialDesignFloatingActionMiniSecondaryLightButton` | ButtonBase | 悬浮操作按钮FAB；操作按钮；浅色变体；辅助色变体；迷你尺寸 | MaterialDesignFloatingActionMiniButton |
| `MaterialDesignFloatingActionMiniSecondaryDarkButton` | ButtonBase | 悬浮操作按钮FAB；操作按钮；深色变体；辅助色变体；迷你尺寸 | MaterialDesignFloatingActionMiniButton |
| `MaterialDesignFloatingActionLightButton` | ButtonBase | 悬浮操作按钮FAB；操作按钮；浅色变体 | MaterialDesignFloatingActionButton |
| `MaterialDesignFloatingActionDarkButton` | ButtonBase | 悬浮操作按钮FAB；操作按钮；深色变体 | MaterialDesignFloatingActionButton |
| `MaterialDesignFloatingActionSecondaryButton` | ButtonBase | 悬浮操作按钮FAB；操作按钮；辅助色变体 | MaterialDesignFloatingActionButton |
| `MaterialDesignFloatingActionSecondaryLightButton` | ButtonBase | 悬浮操作按钮FAB；操作按钮；浅色变体；辅助色变体 | MaterialDesignFloatingActionButton |
| `MaterialDesignFloatingActionSecondaryDarkButton` | ButtonBase | 悬浮操作按钮FAB；操作按钮；深色变体；辅助色变体 | MaterialDesignFloatingActionButton |
| `MaterialDesignIconButton` | ButtonBase | 按钮；图标 | MaterialDesignFlatButton |
| `MaterialDesignIconForegroundButton` | ButtonBase | 按钮；图标；前景 | MaterialDesignIconButton |
| `MaterialDesignPaperButton` | ButtonBase | 纸面容器 | — |
| `MaterialDesignPaperLightButton` | ButtonBase | 浅色变体；纸面容器 | MaterialDesignPaperButton |
| `MaterialDesignPaperDarkButton` | ButtonBase | 深色变体；纸面容器 | MaterialDesignPaperButton |
| `MaterialDesignPaperSecondaryLightButton` | ButtonBase | 浅色变体；辅助色变体；纸面容器 | MaterialDesignPaperButton |
| `MaterialDesignPaperSecondaryButton` | ButtonBase | 辅助色变体；纸面容器 | MaterialDesignPaperButton |
| `MaterialDesignPaperSecondaryDarkButton` | ButtonBase | 深色变体；辅助色变体；纸面容器 | MaterialDesignPaperButton |

### 开关按钮 ToggleButton  _(11 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignActionToggleButton` | ToggleButton | 操作按钮 | — |
| `MaterialDesignActionLightToggleButton` | ToggleButton | 操作按钮；浅色变体 | MaterialDesignActionToggleButton |
| `MaterialDesignActionDarkToggleButton` | ToggleButton | 操作按钮；深色变体 | MaterialDesignActionToggleButton |
| `MaterialDesignActionSecondaryToggleButton` | ToggleButton | 操作按钮；辅助色变体 | MaterialDesignActionToggleButton |
| `MaterialDesignFlatToggleButton` | ToggleButton | 扁平(无阴影) | — |
| `MaterialDesignFlatPrimaryToggleButton` | ToggleButton | 扁平(无阴影)；主色变体 | MaterialDesignFlatToggleButton |
| `MaterialDesignSwitchToggleButton` | ToggleButton | 开关Switch | — |
| `MaterialDesignSwitchLightToggleButton` | ToggleButton | 开关Switch；浅色变体 | MaterialDesignSwitchToggleButton |
| `MaterialDesignSwitchDarkToggleButton` | ToggleButton | 开关Switch；深色变体 | MaterialDesignSwitchToggleButton |
| `MaterialDesignSwitchSecondaryToggleButton` | ToggleButton | 开关Switch；辅助色变体 | MaterialDesignSwitchToggleButton |
| `MaterialDesignHamburgerToggleButton` | ToggleButton | 汉堡菜单 | — |

### 窗口布局 Window  _(1 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignWindow` | Window | 窗口 | — |

### 专用控件 AutoSuggestBox  _(5 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignAutoSuggestBoxBase` | AutoSuggestBox | 自动建议框；基础；框 | MaterialDesignTextBoxBase |
| `MaterialDesignAutoSuggestBox` | AutoSuggestBox | 自动建议框；框 | MaterialDesignAutoSuggestBoxBase |
| `MaterialDesignFloatingHintAutoSuggestBox` | AutoSuggestBox | 浮动提示标签 | MaterialDesignAutoSuggestBox |
| `MaterialDesignFilledAutoSuggestBox` | AutoSuggestBox | 填充式 | MaterialDesignFloatingHintAutoSuggestBox |
| `MaterialDesignOutlinedAutoSuggestBox` | AutoSuggestBox | 描边(透明底+边框) | MaterialDesignFloatingHintAutoSuggestBox |

### 容器卡片 Badged  _(2 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignBadge` | Badged | 角标 | — |
| `MaterialDesignMiniBadge` | Badged | 迷你尺寸；角标 | — |

### 日期时间 Calendar  _(6 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignCalendarButton` | CalendarButton | 日历；按钮；日历按钮 | — |
| `MaterialDesignCalendarDayButton` | CalendarDayButton | 日历；按钮；日历日按钮 | — |
| `MaterialDesignCalendarItemPortrait` | CalendarItem | 日历；竖屏；项；日历项 | — |
| `MaterialDesignCalendarPortraitBase` | Calendar | 日历；竖屏；基础 | — |
| `MaterialDesignCalendarPortrait` | Calendar | 日历；竖屏 | MaterialDesignCalendarPortraitBase |
| `MaterialDesignCalendarPortraitForeground` | Calendar | 日历；竖屏；前景 | MaterialDesignCalendarPortrait |

### 容器卡片 Card  _(2 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignElevatedCard` | Card | 卡片容器 | — |
| `MaterialDesignOutlinedCard` | Card | 描边(透明底+边框)；卡片容器 | — |

### 选择 CheckBox  _(16 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `OptionMarkFocusVisual` | — | 命名样式 | — |
| `MaterialDesignActionCheckBox` | CheckBox | 操作按钮 | MaterialDesignActionToggleButton |
| `MaterialDesignActionLightCheckBox` | CheckBox | 操作按钮；浅色变体 | MaterialDesignActionCheckBox |
| `MaterialDesignActionDarkCheckBox` | CheckBox | 操作按钮；深色变体 | MaterialDesignActionCheckBox |
| `MaterialDesignActionSecondaryCheckBox` | CheckBox | 操作按钮；辅助色变体 | MaterialDesignActionCheckBox |
| `MaterialDesignCheckBox` | CheckBox | 复选框；勾选；框 | — |
| `MaterialDesignLightCheckBox` | CheckBox | 浅色变体 | MaterialDesignCheckBox |
| `MaterialDesignDarkCheckBox` | CheckBox | 深色变体 | MaterialDesignCheckBox |
| `MaterialDesignSecondaryCheckBox` | CheckBox | 辅助色变体 | MaterialDesignCheckBox |
| `MaterialDesignUserForegroundCheckBox` | CheckBox | 复选框；勾选；框；前景；用户前景 | — |
| `MaterialDesignFilterChipCheckBox` | ToggleButton | 筛选芯片 | — |
| `MaterialDesignFilterChipOutlineCheckBox` | ToggleButton | 筛选芯片 | — |
| `MaterialDesignFilterChipPrimaryCheckBox` | ToggleButton | 筛选芯片；主色变体 | MaterialDesignFilterChipCheckBox |
| `MaterialDesignFilterChipSecondaryCheckBox` | ToggleButton | 筛选芯片；辅助色变体 | MaterialDesignFilterChipCheckBox |
| `MaterialDesignFilterChipPrimaryOutlineCheckBox` | ToggleButton | 筛选芯片；主色变体 | MaterialDesignFilterChipOutlineCheckBox |
| `MaterialDesignFilterChipSecondaryOutlineCheckBox` | ToggleButton | 筛选芯片；辅助色变体 | MaterialDesignFilterChipOutlineCheckBox |

### 显示排版 Chip  _(1 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignOutlineChip` | Chip | 筛选芯片；描边 | — |

### 日期时间 Clock  _(10 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignClockItemThumb` | Thumb | 时钟；滑块Thumb；项 | — |
| `MaterialDesignCalendarMeridiemRadioButton` | RadioButton | 单选按钮；日历；按钮；上下午；单选 | — |
| `MaterialDesignCalendarMeridiemRadioButtonDefault` | RadioButton | 单选按钮；日历；按钮；上下午；单选 | — |
| `MaterialDesignCalendarMeridiemRadioButtonThemed` | RadioButton | 单选按钮；日历；按钮；主题化；上下午；单选 | — |
| `MaterialDesignClock` | Clock | 时钟 | — |
| `TimeTextBlock` |  | 文本；时间 | — |
| `MaterialDesignClockVertical` | Clock | 时钟；垂直 | — |
| `MaterialDesignClockVerticalThemed` | Clock | 时钟；垂直；主题化 | — |
| `MaterialDesignClockHorizontal` | Clock | 时钟；水平 | — |
| `MaterialDesignClockHorizontalThemed` | Clock | 时钟；水平；主题化 | — |

### 专用控件 ColorPicker  _(1 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignColorSlider` | Slider | 颜色滑块；滑块；颜色 | — |

### 选择 ComboBox  _(8 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignComboBoxEditableTextBox` | TextBox | 文本框；组合框；可编辑；文本；框；组合；组合框可编辑文本 | — |
| `MaterialDesignComboBoxItemStyle` | ComboBoxItem | 组合框；项；框；组合；组合框项 | — |
| `MaterialDesignComboBoxItemSelectedCollapsedStyle` | ComboBoxItem | 组合框；选中；折叠；项；框；组合；组合框项 | MaterialDesignComboBoxItemStyle |
| `MaterialDesignComboBoxToggleButton` | ToggleButton | 组合框；开关按钮；按钮；开关；框；组合；组合框开关 | — |
| `MaterialDesignComboBox` | ComboBox | 组合框；框；组合 | — |
| `MaterialDesignFloatingHintComboBox` | ComboBox | 浮动提示标签 | MaterialDesignComboBox |
| `MaterialDesignFilledComboBox` | ComboBox | 填充式 | MaterialDesignFloatingHintComboBox |
| `MaterialDesignOutlinedComboBox` | ComboBox | 描边(透明底+边框) | MaterialDesignFloatingHintComboBox |

### 选择 DataGrid·ComboBox  _(4 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignDataGridComboBoxItemStyle` | ComboBoxItem | 数据网格；组合框；项；网格；框；组合；数据网格组合框；组合框项 | — |
| `MaterialDesignDataGridComboBoxToggleButton` | ToggleButton | 数据网格；组合框；开关按钮；按钮；开关；网格；框；组合；数据网格组合框；组合框开关 | — |
| `MaterialDesignDataGridComboBoxEditableTextBox` | TextBox | 数据网格；文本框；组合框；可编辑；文本；网格；框；组合；数据网格组合框；组合框可编辑文本 | — |
| `MaterialDesignDataGridComboBox` | ComboBox | 数据网格；组合框；网格；框；组合；数据网格组合框 | — |

### 列表集合 DataGrid  _(10 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignDataGridCheckBoxColumnStyle` | CheckBox | 数据网格；复选框；列；勾选；网格；框；数据网格勾选列 | MaterialDesignCheckBox |
| `MaterialDesignDataGridCheckBoxColumnEditingStyle` | CheckBox | 数据网格；复选框；列；勾选；网格；框；数据网格勾选列 | MaterialDesignCheckBox |
| `MaterialDesignDataGridTextColumnEditingStyle` | TextBox | 数据网格；列；文本；网格；数据网格文本列 | MaterialDesignTextBox |
| `MaterialDesignDataGridTextColumnStyle` | TextBlock | 数据网格；列；文本；网格；数据网格文本列 | {x:Type TextBlock |
| `MaterialDesignDataGridTextColumnPopupEditingStyle` | TextBox | 数据网格；弹出；列；文本；网格；数据网格文本列 | MaterialDesignTextBox |
| `MaterialDesignDataGridCell` | DataGridCell | 数据网格；单元格；网格；数据网格单元格 | — |
| `MaterialDesignDataGridColumnHeader` | DataGridColumnHeader | 数据网格；标题；列；网格；数据网格列头 | — |
| `MaterialDesignDataGridRowHeader` | DataGridRowHeader | 数据网格；标题；行；网格；数据网格行；数据网格行头 | — |
| `MaterialDesignDataGridRow` | DataGridRow | 数据网格；行；网格；数据网格行 | — |
| `MaterialDesignDataGrid` | DataGrid | 数据网格；网格 | — |

### 日期时间 DatePicker  _(6 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignDatePickerCalendarPortrait` | Calendar | 日期选择器；日历；竖屏；日期 | MaterialDesignCalendarPortrait |
| `MaterialDesignDatePicker` | DatePicker | 日期选择器；日期 | — |
| `NestedTextBoxStyle` | DatePickerTextBox | 文本框；文本；框；嵌套 | MaterialDesignOutlinedTextBox |
| `MaterialDesignFloatingHintDatePicker` | DatePicker | 浮动提示标签 | MaterialDesignDatePicker |
| `MaterialDesignFilledDatePicker` | DatePicker | 填充式 | MaterialDesignFloatingHintDatePicker |
| `MaterialDesignOutlinedDatePicker` | DatePicker | 描边(透明底+边框) | MaterialDesignFloatingHintDatePicker |

### 显示排版 DialogHost  _(2 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignDialogHostPopup` | PopupEx | 对话框宿主；弹出；对话框 | — |
| `MaterialDesignEmbeddedDialogHost` | DialogHost | 对话框宿主；内嵌；对话框 | — |

### 容器卡片 Expander  _(4 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignExpanderToggleButton` | ToggleButton | 开关按钮；展开器；按钮；开关 | — |
| `MaterialDesignHorizontalHeaderStyle` | ToggleButton | 水平；标题 | — |
| `MaterialDesignVerticalHeaderStyle` | ToggleButton | 垂直；标题 | — |
| `MaterialDesignExpander` | Expander | 展开器 | — |

### 容器卡片 FlipperClassic  _(1 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignCardFlipperClassic` | FlipperClassic | 卡片容器 | {x:Type wpf:FlipperClassic |

### 窗口布局 GridSplitter  _(2 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignGridSplitterPreview` | — | 网格分隔器；网格；复合 | — |
| `MaterialDesignGridSplitter` | GridSplitter | 网格分隔器；网格；复合 | — |

### 容器卡片 GroupBox  _(3 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignHeaderedContentControl` | HeaderedContentControl | 标题 | — |
| `MaterialDesignGroupBox` | GroupBox | 组框；框 | — |
| `MaterialDesignCardGroupBox` | GroupBox | 卡片容器 | — |

### 显示排版 Hyperlink  _(13 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignHyperlink` | Hyperlink | 超链接 | — |
| `MaterialDesignBody1Hyperlink` | Hyperlink | Body正文排版 | MaterialDesignHyperlink |
| `MaterialDesignBody2Hyperlink` | Hyperlink | Body正文排版 | MaterialDesignBody1Hyperlink |
| `MaterialDesignCaptionHyperlink` | Hyperlink | Caption排版 | MaterialDesignBody1Hyperlink |
| `MaterialDesignOverlineHyperlink` | Hyperlink | Overline上标 | MaterialDesignBody1Hyperlink |
| `MaterialDesignSubtitle1Hyperlink` | Hyperlink | Subtitle副标题 | MaterialDesignBody1Hyperlink |
| `MaterialDesignSubtitle2Hyperlink` | Hyperlink | Subtitle副标题 | MaterialDesignBody1Hyperlink |
| `MaterialDesignHeadline6Hyperlink` | Hyperlink | Headline标题 | MaterialDesignBody1Hyperlink |
| `MaterialDesignHeadline5Hyperlink` | Hyperlink | Headline标题 | MaterialDesignBody1Hyperlink |
| `MaterialDesignHeadline4Hyperlink` | Hyperlink | Headline标题 | MaterialDesignBody1Hyperlink |
| `MaterialDesignHeadline3Hyperlink` | Hyperlink | Headline标题 | MaterialDesignBody1Hyperlink |
| `MaterialDesignHeadline2Hyperlink` | Hyperlink | Headline标题 | MaterialDesignBody1Hyperlink |
| `MaterialDesignHeadline1Hyperlink` | Hyperlink | Headline标题 | MaterialDesignBody1Hyperlink |

### 显示排版 Label  _(1 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignLabel` | Label | Label标签 | — |

### 列表集合 ListBox  _(38 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignToolToggleListBoxItem` | ListBoxItem | 列表框；开关；工具；项；列表；框；列表项 | — |
| `MaterialDesignToolToggleListBox` | ListBox | 列表框；开关；工具；列表；框 | — |
| `MaterialDesignToolVerticalToggleListBox` | ListBox | 列表框；开关；工具；垂直；列表；框 | MaterialDesignToolToggleListBox |
| `MaterialDesignToolToggleFlatListBox` | ListBox | 扁平(无阴影) | MaterialDesignToolToggleListBox |
| `MaterialDesignListBoxItem` | ListBoxItem | 列表框；项；列表；框；列表项 | — |
| `MaterialDesignListBox` | ListBox | 列表框；列表；框 | — |
| `MaterialDesignCardsListBoxItem` | ListBoxItem | 卡片容器 | — |
| `MaterialDesignCardsListBox` | ListBox | 卡片容器 | MaterialDesignListBox |
| `MaterialDesignNavigationListBoxItem` | ListBoxItem | 导航项 | — |
| `MaterialDesignNavigationPrimaryListBoxItem` | ListBoxItem | 导航项；主色变体 | MaterialDesignNavigationListBoxItem |
| `MaterialDesignNavigationSecondaryListBoxItem` | ListBoxItem | 导航项；辅助色变体 | MaterialDesignNavigationListBoxItem |
| `MaterialDesignNavigationListBox` | ListBox | 导航项 | MaterialDesignListBox |
| `MaterialDesignNavigationPrimaryListBox` | ListBox | 导航项；主色变体 | MaterialDesignListBox |
| `MaterialDesignNavigationSecondaryListBox` | ListBox | 导航项；辅助色变体 | MaterialDesignListBox |
| `MaterialDesignFilterChipListBoxItem` | ListBoxItem | 筛选芯片 | — |
| `MaterialDesignFilterChipListBox` | ListBox | 筛选芯片 | — |
| `MaterialDesignFilterChipPrimaryListBoxItem` | ListBoxItem | 筛选芯片；主色变体 | — |
| `MaterialDesignFilterChipPrimaryListBox` | ListBox | 筛选芯片；主色变体 | MaterialDesignFilterChipListBox |
| `MaterialDesignFilterChipSecondaryListBoxItem` | ListBoxItem | 筛选芯片；辅助色变体 | — |
| `MaterialDesignFilterChipSecondaryListBox` | ListBox | 筛选芯片；辅助色变体 | MaterialDesignFilterChipListBox |
| `MaterialDesignFilterChipOutlineListBoxItem` | ListBoxItem | 筛选芯片 | — |
| `MaterialDesignFilterChipOutlineListBox` | ListBox | 筛选芯片 | MaterialDesignFilterChipListBox |
| `MaterialDesignFilterChipPrimaryOutlineListBoxItem` | ListBoxItem | 筛选芯片；主色变体 | — |
| `MaterialDesignFilterChipPrimaryOutlineListBox` | ListBox | 筛选芯片；主色变体 | MaterialDesignFilterChipListBox |
| `MaterialDesignFilterChipSecondaryOutlineListBoxItem` | ListBoxItem | 筛选芯片；辅助色变体 | — |
| `MaterialDesignFilterChipSecondaryOutlineListBox` | ListBox | 筛选芯片；辅助色变体 | MaterialDesignFilterChipListBox |
| `MaterialDesignChoiceChipListBoxItem` | ListBoxItem | 单选芯片 | — |
| `MaterialDesignChoiceChipListBox` | ListBox | 单选芯片 | MaterialDesignFilterChipListBox |
| `MaterialDesignChoiceChipPrimaryListBoxItem` | ListBoxItem | 单选芯片；主色变体 | — |
| `MaterialDesignChoiceChipPrimaryListBox` | ListBox | 单选芯片；主色变体 | MaterialDesignChoiceChipListBox |
| `MaterialDesignChoiceChipSecondaryListBoxItem` | ListBoxItem | 单选芯片；辅助色变体 | — |
| `MaterialDesignChoiceChipSecondaryListBox` | ListBox | 单选芯片；辅助色变体 | MaterialDesignChoiceChipListBox |
| `MaterialDesignChoiceChipOutlineListBoxItem` | ListBoxItem | 单选芯片 | — |
| `MaterialDesignChoiceChipOutlineListBox` | ListBox | 单选芯片 | MaterialDesignChoiceChipListBox |
| `MaterialDesignChoiceChipPrimaryOutlineListBoxItem` | ListBoxItem | 单选芯片；主色变体 | — |
| `MaterialDesignChoiceChipPrimaryOutlineListBox` | ListBox | 单选芯片；主色变体 | MaterialDesignChoiceChipListBox |
| `MaterialDesignChoiceChipSecondaryOutlineListBoxItem` | ListBoxItem | 单选芯片；辅助色变体 | — |
| `MaterialDesignChoiceChipSecondaryOutlineListBox` | ListBox | 单选芯片；辅助色变体 | MaterialDesignChoiceChipListBox |

### 列表集合 ListView  _(2 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignGridViewItem` | ListViewItem | 网格视图 | — |
| `MaterialDesignListView` | ListView | 列表视图；列表；视图 | — |

### 导航 Menu  _(3 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignMenuItem` | MenuItem | 菜单；项 | {x:Null |
| `MaterialDesignMenu` | MenuBase | 菜单 | — |
| `MaterialDesignContextMenu` | ContextMenu | 菜单；上下文 | MaterialDesignMenu |

### 专用控件 NumericUpDown  _(12 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignNumericUpDownButtonsStyle` | ButtonBase | 数值增减框；按钮；数值；增减 | MaterialDesignFlatButton |
| `MaterialDesignNumericUpDown` | UpDownBase | 数值增减框；数值；增减 | — |
| `NestedNumericUpDownButtonsStyle` | ButtonBase | 数值增减框；按钮；数值；增减；嵌套 | MaterialDesignNumericUpDownButtonsStyle |
| `MaterialDesignFloatingHintUpDownBase` | UpDownBase | 浮动提示标签 | MaterialDesignNumericUpDown |
| `MaterialDesignFloatingHintNumericUpDown` | NumericUpDown | 浮动提示标签 | MaterialDesignFloatingHintUpDownBase |
| `MaterialDesignFloatingHintDecimalUpDown` | DecimalUpDown | 浮动提示标签 | MaterialDesignFloatingHintUpDownBase |
| `MaterialDesignFilledUpDownBase` | UpDownBase | 填充式 | MaterialDesignFloatingHintUpDownBase |
| `MaterialDesignFilledNumericUpDown` | NumericUpDown | 填充式 | MaterialDesignFilledUpDownBase |
| `MaterialDesignFilledDecimalUpDown` | DecimalUpDown | 填充式 | MaterialDesignFilledUpDownBase |
| `MaterialDesignOutlinedUpDownBase` | UpDownBase | 描边(透明底+边框) | MaterialDesignFloatingHintUpDownBase |
| `MaterialDesignOutlinedNumericUpDown` | NumericUpDown | 描边(透明底+边框) | MaterialDesignOutlinedUpDownBase |
| `MaterialDesignOutlinedDecimalUpDown` | DecimalUpDown | 描边(透明底+边框) | MaterialDesignOutlinedUpDownBase |

### 文本输入 PasswordBox  _(12 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignPasswordBox` | PasswordBox | 密码框；框 | — |
| `MaterialDesignPasswordCharacterCounterTextBlock` | TextBlock | 字符计数器；文本 | {x:Type TextBlock |
| `MaterialDesignPasswordHelperTextBlock` | TextBlock | 辅助说明；文本 | {x:Type TextBlock |
| `MaterialDesignFloatingHintPasswordBox` | PasswordBox | 浮动提示标签 | MaterialDesignPasswordBox |
| `MaterialDesignFilledPasswordBox` | PasswordBox | 填充式 | MaterialDesignFloatingHintPasswordBox |
| `MaterialDesignOutlinedPasswordBox` | PasswordBox | 描边(透明底+边框) | MaterialDesignFloatingHintPasswordBox |
| `MaterialDesignRevealPasswordBox` | PasswordBox | 可显隐密码 | — |
| `MaterialDesignRawTextBox` | TextBox | 文本框；文本；框 | — |
| `MaterialDesignRawToggleButton` | ToggleButton | 开关按钮；按钮；开关 | — |
| `MaterialDesignFloatingHintRevealPasswordBox` | PasswordBox | 浮动提示标签；可显隐密码 | MaterialDesignRevealPasswordBox |
| `MaterialDesignFilledRevealPasswordBox` | PasswordBox | 填充式；可显隐密码 | MaterialDesignFloatingHintRevealPasswordBox |
| `MaterialDesignOutlinedRevealPasswordBox` | PasswordBox | 描边(透明底+边框)；可显隐密码 | MaterialDesignFloatingHintRevealPasswordBox |

### 容器卡片 PopupBox  _(9 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignPopupBoxButton` | Button | 弹出盒；按钮；弹出；框 | — |
| `MaterialDesignPopupBox` | PopupBox | 弹出盒；弹出；框 | — |
| `ToggleButtonStyle` | ToggleButton | 开关按钮；按钮；开关 | — |
| `MaterialDesignToolPopupBox` | PopupBox | 弹出盒；工具；弹出；框 | MaterialDesignPopupBox |
| `MaterialDesignToolForegroundPopupBox` | PopupBox | 弹出盒；工具；弹出；框；前景 | MaterialDesignToolPopupBox |
| `MaterialDesignMultiFloatingActionPopupBox` | PopupBox | 悬浮操作按钮FAB；操作按钮 | — |
| `MaterialDesignMultiFloatingActionLightPopupBox` | PopupBox | 悬浮操作按钮FAB；操作按钮；浅色变体 | MaterialDesignMultiFloatingActionPopupBox |
| `MaterialDesignMultiFloatingActionDarkPopupBox` | PopupBox | 悬浮操作按钮FAB；操作按钮；深色变体 | MaterialDesignMultiFloatingActionPopupBox |
| `MaterialDesignMultiFloatingActionSecondaryPopupBox` | PopupBox | 悬浮操作按钮FAB；操作按钮；辅助色变体 | MaterialDesignMultiFloatingActionPopupBox |

### 显示排版 ProgressBar  _(2 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignLinearProgressBar` | ProgressBar | 线性进度 | — |
| `MaterialDesignCircularProgressBar` | ProgressBar | 圆形进度 | — |

### 选择 RadioButton  _(17 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignRadioButton` | RadioButton | 单选按钮；按钮；单选 | — |
| `MaterialDesignLightRadioButton` | RadioButton | 浅色变体 | MaterialDesignRadioButton |
| `MaterialDesignDarkRadioButton` | RadioButton | 深色变体 | MaterialDesignRadioButton |
| `MaterialDesignSecondaryRadioButton` | RadioButton | 辅助色变体 | MaterialDesignRadioButton |
| `MaterialDesignUserForegroundRadioButton` | RadioButton | 单选按钮；按钮；单选；前景；用户前景 | — |
| `MaterialDesignTabRadioButton` | RadioButton | 单选按钮；按钮；单选；选项卡；选项卡单选按钮 | — |
| `MaterialDesignTabRadioButtonLeft` | RadioButton | 单选按钮；按钮；单选；选项卡；选项卡单选按钮 | MaterialDesignTabRadioButton |
| `MaterialDesignTabRadioButtonTop` | RadioButton | 单选按钮；按钮；单选；选项卡；选项卡单选按钮 | MaterialDesignTabRadioButton |
| `MaterialDesignTabRadioButtonRight` | RadioButton | 单选按钮；按钮；单选；选项卡；选项卡单选按钮 | MaterialDesignTabRadioButton |
| `MaterialDesignTabRadioButtonBottom` | RadioButton | 单选按钮；按钮；单选；选项卡；选项卡单选按钮 | MaterialDesignTabRadioButton |
| `MaterialDesignToolRadioButton` | RadioButton | 单选按钮；按钮；工具；单选 | — |
| `MaterialDesignChoiceChipRadioButton` | ToggleButton | 单选芯片 | — |
| `MaterialDesignChoiceChipOutlineRadioButton` | ToggleButton | 单选芯片 | — |
| `MaterialDesignChoiceChipPrimaryRadioButton` | ToggleButton | 单选芯片；主色变体 | MaterialDesignChoiceChipRadioButton |
| `MaterialDesignChoiceChipSecondaryRadioButton` | ToggleButton | 单选芯片；辅助色变体 | MaterialDesignChoiceChipRadioButton |
| `MaterialDesignChoiceChipPrimaryOutlineRadioButton` | ToggleButton | 单选芯片；主色变体 | MaterialDesignChoiceChipOutlineRadioButton |
| `MaterialDesignChoiceChipSecondaryOutlineRadioButton` | ToggleButton | 单选芯片；辅助色变体 | MaterialDesignChoiceChipOutlineRadioButton |

### 文本输入 RichTextBox  _(4 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignRichTextBox` | RichTextBox | 富文本框；文本框；文本；框 | MaterialDesignTextBoxBase |
| `MaterialDesignFloatingHintRichTextBox` | RichTextBox | 浮动提示标签 | MaterialDesignRichTextBox |
| `MaterialDesignFilledRichTextBox` | RichTextBox | 填充式 | MaterialDesignFloatingHintRichTextBox |
| `MaterialDesignOutlinedRichTextBox` | RichTextBox | 描边(透明底+边框) | MaterialDesignFloatingHintRichTextBox |

### 显示排版 ScrollBar  _(5 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignScrollBarButton` | RepeatButton | 滚动条；按钮；条；滚动 | — |
| `MaterialDesignRepeatButtonTransparent` | RepeatButton | 重复按钮；按钮；重复 | — |
| `MaterialDesignScrollBarThumb` | Thumb | 滚动条；滑块Thumb；条；滚动 | — |
| `MaterialDesignScrollBar` | ScrollBar | 滚动条；条；滚动 | — |
| `MaterialDesignScrollBarMinimal` | ScrollBar | 迷你尺寸 | MaterialDesignScrollBar |

### 显示排版 ScrollViewer  _(1 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignScrollViewer` | ScrollViewer | 滚动视图；视图；滚动 | — |

### 显示排版 Separator  _(1 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignSeparator` | Separator | 分隔线 | — |

### Theme.Slider  _(5 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignRepeatButton` | RepeatButton | 重复按钮；按钮；重复 | — |
| `MaterialDesignSlider` | Slider | 滑块 | — |
| `MaterialDesignDiscreteHorizontalSlider` | Slider | 离散刻度 | — |
| `MaterialDesignDiscreteVerticalSlider` | Slider | 离散刻度 | — |
| `MaterialDesignDiscreteSlider` | Slider | 离散刻度 | MaterialDesignDiscreteHorizontalSlider |

### 显示排版 Snackbar  _(4 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignSnackbarActionButton` | Button | 操作按钮；Snackbar操作按钮 | — |
| `MaterialDesignSnackbarActionLightButton` | Button | 操作按钮；浅色变体；Snackbar操作按钮 | MaterialDesignSnackbarActionButton |
| `MaterialDesignSnackbarActionMidButton` | Button | 操作按钮；Snackbar操作按钮 | MaterialDesignSnackbarActionButton |
| `MaterialDesignSnackbarActionDarkButton` | Button | 操作按钮；深色变体；Snackbar操作按钮 | MaterialDesignSnackbarActionButton |

### 复合按钮 SplitButton  _(25 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignSplitButton` | SplitButton | 复合按钮；按钮；复合 | — |
| `MaterialDesignRaisedSplitButton` | SplitButton | 凸起实心(带阴影) | MaterialDesignSplitButton |
| `MaterialDesignRaisedLightSplitButton` | SplitButton | 凸起实心(带阴影)；浅色变体 | MaterialDesignRaisedSplitButton |
| `MaterialDesignRaisedDarkSplitButton` | SplitButton | 凸起实心(带阴影)；深色变体 | MaterialDesignRaisedSplitButton |
| `MaterialDesignRaisedSecondarySplitButton` | SplitButton | 凸起实心(带阴影)；辅助色变体 | MaterialDesignRaisedSplitButton |
| `MaterialDesignRaisedSecondaryLightSplitButton` | SplitButton | 凸起实心(带阴影)；浅色变体；辅助色变体 | MaterialDesignRaisedSplitButton |
| `MaterialDesignRaisedSecondaryDarkSplitButton` | SplitButton | 凸起实心(带阴影)；深色变体；辅助色变体 | MaterialDesignRaisedSplitButton |
| `MaterialDesignOutlinedSplitButton` | SplitButton | 描边(透明底+边框) | MaterialDesignSplitButton |
| `MaterialDesignOutlinedLightSplitButton` | SplitButton | 描边(透明底+边框)；浅色变体 | MaterialDesignOutlinedSplitButton |
| `MaterialDesignOutlinedDarkSplitButton` | SplitButton | 描边(透明底+边框)；深色变体 | MaterialDesignOutlinedSplitButton |
| `MaterialDesignOutlinedSecondarySplitButton` | SplitButton | 描边(透明底+边框)；辅助色变体 | MaterialDesignOutlinedSplitButton |
| `MaterialDesignOutlinedSecondaryLightSplitButton` | SplitButton | 描边(透明底+边框)；浅色变体；辅助色变体 | MaterialDesignOutlinedSplitButton |
| `MaterialDesignOutlinedSecondaryDarkSplitButton` | SplitButton | 描边(透明底+边框)；深色变体；辅助色变体 | MaterialDesignOutlinedSplitButton |
| `MaterialDesignFlatSplitButton` | SplitButton | 扁平(无阴影) | MaterialDesignSplitButton |
| `MaterialDesignFlatLightSplitButton` | SplitButton | 扁平(无阴影)；浅色变体 | MaterialDesignFlatSplitButton |
| `MaterialDesignFlatDarkSplitButton` | SplitButton | 扁平(无阴影)；深色变体 | MaterialDesignFlatSplitButton |
| `MaterialDesignFlatSecondarySplitButton` | SplitButton | 扁平(无阴影)；辅助色变体 | MaterialDesignFlatSplitButton |
| `MaterialDesignFlatSecondaryLightSplitButton` | SplitButton | 扁平(无阴影)；浅色变体；辅助色变体 | MaterialDesignFlatSplitButton |
| `MaterialDesignFlatSecondaryDarkSplitButton` | SplitButton | 扁平(无阴影)；深色变体；辅助色变体 | MaterialDesignFlatSplitButton |
| `MaterialDesignPaperSplitButton` | SplitButton | 纸面容器 | MaterialDesignSplitButton |
| `MaterialDesignPaperLightSplitButton` | SplitButton | 浅色变体；纸面容器 | MaterialDesignPaperSplitButton |
| `MaterialDesignPaperDarkSplitButton` | SplitButton | 深色变体；纸面容器 | MaterialDesignPaperSplitButton |
| `MaterialDesignPaperSecondarySplitButton` | SplitButton | 辅助色变体；纸面容器 | MaterialDesignPaperSplitButton |
| `MaterialDesignPaperSecondaryLightSplitButton` | SplitButton | 浅色变体；辅助色变体；纸面容器 | MaterialDesignPaperSplitButton |
| `MaterialDesignPaperSecondaryDarkSplitButton` | SplitButton | 深色变体；辅助色变体；纸面容器 | MaterialDesignPaperSplitButton |

### 窗口布局 StatusBar  _(2 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignStatusBar` | StatusBar | 状态栏；状态；条 | — |
| `MaterialDesignStatusBarItem` | StatusBarItem | 状态栏；项；状态；条 | — |

### 导航 TabControl  _(8 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignTabControlBase` | TabControl | 选项卡；基础 | — |
| `MaterialDesignTabControl` | TabControl | 选项卡 | MaterialDesignTabControlBase |
| `MaterialDesignUniformTabControl` | TabControl | 等宽分布 | MaterialDesignTabControl |
| `MaterialDesignFilledTabControl` | TabControl | 填充式 | MaterialDesignTabControlBase |
| `MaterialDesignFilledUniformTabControl` | TabControl | 填充式；等宽分布 | MaterialDesignFilledTabControl |
| `MaterialDesignTabItem` | TabItem | 项；选项卡；选项卡项 | — |
| `MaterialDesignNavigationRailTabItem` | TabItem | 导航项 | — |
| `MaterialDesignNavigationRailTabControl` | TabControl | 导航项 | — |

### 显示排版 TextBlock  _(14 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignTextBlock` | TextBlock | 文本 | — |
| `MaterialDesignCaptionTextBlock` | TextBlock | Caption排版 | MaterialDesignTextBlock |
| `MaterialDesignBody1TextBlock` | TextBlock | Body正文排版 | MaterialDesignTextBlock |
| `MaterialDesignBody2TextBlock` | TextBlock | Body正文排版 | — |
| `MaterialDesignOverlineTextBlock` | TextBlock | Overline上标 | — |
| `MaterialDesignSubtitle1TextBlock` | TextBlock | Subtitle副标题 | — |
| `MaterialDesignSubtitle2TextBlock` | TextBlock | Subtitle副标题 | — |
| `MaterialDesignHeadline6TextBlock` | TextBlock | Headline标题 | — |
| `MaterialDesignHeadline5TextBlock` | TextBlock | Headline标题 | — |
| `MaterialDesignHeadline4TextBlock` | TextBlock | Headline标题 | — |
| `MaterialDesignHeadline3TextBlock` | TextBlock | Headline标题 | — |
| `MaterialDesignHeadline2TextBlock` | TextBlock | Headline标题 | — |
| `MaterialDesignHeadline1TextBlock` | TextBlock | Headline标题 | — |
| `MaterialDesignButtonTextBlock` | TextBlock | 按钮；文本 | — |

### 文本输入 TextBox  _(7 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignHelperTextBlock` | TextBlock | 辅助说明；文本 | {x:Type TextBlock |
| `MaterialDesignCharacterCounterTextBlock` | TextBlock | 字符计数器；文本 | {x:Type TextBlock |
| `MaterialDesignTextBoxBase` | TextBoxBase | 文本框；基础；文本；框 | — |
| `MaterialDesignTextBox` | TextBox | 文本框；文本；框 | MaterialDesignTextBoxBase |
| `MaterialDesignFloatingHintTextBox` | TextBox | 浮动提示标签 | MaterialDesignTextBox |
| `MaterialDesignFilledTextBox` | TextBox | 填充式 | MaterialDesignFloatingHintTextBox |
| `MaterialDesignOutlinedTextBox` | TextBox | 描边(透明底+边框) | MaterialDesignFloatingHintTextBox |

### 窗口布局 Thumb  _(4 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignThumb` | Thumb | 滑块Thumb | — |
| `MaterialDesignGridRowHeaderGripper` | Thumb | 标题；行；网格 | MaterialDesignThumb |
| `MaterialDesignGridColumnHeaderGripper` | Thumb | 标题；列；网格 | MaterialDesignThumb |
| `MaterialDesignGridViewColumnHeaderGripper` | Thumb | 网格视图 | MaterialDesignThumb |

### 日期时间 TimePicker  _(4 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignTimePicker` | TimePicker | 时间选择器；时间 | — |
| `MaterialDesignFloatingHintTimePicker` | TimePicker | 浮动提示标签 | MaterialDesignTimePicker |
| `MaterialDesignFilledTimePicker` | TimePicker | 填充式 | MaterialDesignFloatingHintTimePicker |
| `MaterialDesignOutlinedTimePicker` | TimePicker | 描边(透明底+边框) | MaterialDesignFloatingHintTimePicker |

### 导航 ToolBar  _(5 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignToolBarVerticalOverflowButtonStyle` | ToggleButton | 工具栏 | — |
| `MaterialDesignToolBarHorizontalOverflowButtonStyle` | ToggleButton | 工具栏 | — |
| `MaterialDesignToolBarThumbStyle` | Thumb | 工具栏 | — |
| `MaterialDesignToolBarMainPanelBorderStyle` | Border | 工具栏 | — |
| `MaterialDesignToolBar` | ToolBar | 工具栏 | — |

### 导航 ToolBarTray  _(1 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignToolBarTray` | ToolBarTray | 工具栏 | — |

### 显示排版 ToolTip  _(1 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignToolTip` | ToolTip | 工具提示；工具 | — |

### 列表集合 TreeListView  _(4 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignTreeListViewToggleButtonStyle` | ToggleButton | 列表视图；树列表视图；开关按钮；按钮；开关；列表；视图；树 | — |
| `MaterialDesignTreeListViewItemFocusVisual` | — | 列表视图；树列表视图；项；列表；视图；树；树列表项；列表项 | — |
| `MaterialDesignTreeListViewItem` | TreeListViewItem | 列表视图；树列表视图；项；列表；视图；树；树列表项；列表项 | — |
| `MaterialDesignTreeListView` | TreeListView | 列表视图；树列表视图；列表；视图；树 | — |

### 列表集合 TreeView  _(4 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignTreeView` | TreeView | 树视图；视图；树 | — |
| `MaterialDesignTreeViewItemFocusVisual` | — | 树视图；项；视图；树；树项 | — |
| `MaterialDesignExpandCollapseToggleStyle` | ToggleButton | 开关；展开折叠 | — |
| `MaterialDesignTreeViewItem` | TreeViewItem | 树视图；项；视图；树；树项 | — |

## B. Material Design 3.0（专属新增）

### MD3 导航 NavigationBar  _(4 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesign3.NavigationBarListBoxItem` | ListBoxItem | 导航项 | — |
| `MaterialDesign3.NavigationBarPrimaryListBoxItem` | ListBoxItem | 导航项；主色变体 | MaterialDesign3.NavigationBarListBoxItem |
| `MaterialDesign3.NavigationBarListBox` | ListBox | 导航项 | MaterialDesignListBox |
| `MaterialDesign3.NavigationBarPrimaryListBox` | ListBox | 导航项；主色变体 | MaterialDesign3.NavigationBarListBox |

### MD3 导航 NavigationDrawer  _(2 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesign3.NavigationDrawerListBoxItem` | ListBoxItem | 导航项 | — |
| `MaterialDesign3.NavigationDrawerPrimaryListBoxItem` | ListBoxItem | 导航项；主色变体 | MaterialDesign3.NavigationDrawerListBoxItem |

### MD3 导航 NavigationRail  _(2 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesign3.NavigationRailListBoxItem` | ListBoxItem | 导航项 | — |
| `MaterialDesign3.NavigationRailPrimaryListBoxItem` | ListBoxItem | 导航项；主色变体 | MaterialDesign3.NavigationRailListBoxItem |

### MD3 滑块 Slider  _(5 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesign3.MaterialDesignRepeatButton` | RepeatButton | 重复按钮；按钮；重复 | — |
| `MaterialDesign3.MaterialDesignSlider` | Slider | 滑块 | — |
| `MaterialDesign3.MaterialDesignDiscreteHorizontalSlider` | Slider | 离散刻度 | — |
| `MaterialDesign3.MaterialDesignDiscreteVerticalSlider` | Slider | 离散刻度 | — |
| `MaterialDesign3.MaterialDesignDiscreteSlider` | Slider | 离散刻度 | MaterialDesign3.MaterialDesignDiscreteHorizontalSlider |

### MD3 排版 Typography  _(15 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignBodySmallTextBlock` | TextBlock | Body正文排版 | — |
| `MaterialDesignBodyMediumTextBlock` | TextBlock | Body正文排版 | — |
| `MaterialDesignBodyLargeTextBlock` | TextBlock | Body正文排版 | — |
| `MaterialDesignLabelSmallTextBlock` | TextBlock | Label标签 | — |
| `MaterialDesignLabelMediumTextBlock` | TextBlock | Label标签 | — |
| `MaterialDesignLabelLargeTextBlock` | TextBlock | Label标签 | — |
| `MaterialDesignTitleSmallTextBlock` | TextBlock | Title标题 | — |
| `MaterialDesignTitleMediumTextBlock` | TextBlock | Title标题 | — |
| `MaterialDesignTitleLargeTextBlock` | TextBlock | Title标题 | — |
| `MaterialDesignHeadlineSmallTextBlock` | TextBlock | Headline标题 | — |
| `MaterialDesignHeadlineMediumTextBlock` | TextBlock | Headline标题 | — |
| `MaterialDesignHeadlineLargeTextBlock` | TextBlock | Headline标题 | — |
| `MaterialDesignDisplaySmallTextBlock` | TextBlock | Display大标题 | — |
| `MaterialDesignDisplayMediumTextBlock` | TextBlock | Display大标题 | — |
| `MaterialDesignDisplayLargeTextBlock` | TextBlock | Display大标题 | — |

## C. 已废弃（不属于 2.0 / 3.0）

### 已废弃 Obsolete  _(25 个命名样式)_

| 样式键 Style Key | 目标类型 | 说明 | 继承自 |
|---|---|---|---|
| `MaterialDesignActionAccentCheckBox` | CheckBox | 操作按钮；强调色(已废弃) | MaterialDesignActionSecondaryCheckBox |
| `MaterialDesignAccentCheckBox` | CheckBox | 强调色(已废弃) | MaterialDesignSecondaryCheckBox |
| `MaterialDesignAccentRadioButton` | RadioButton | 强调色(已废弃) | MaterialDesignSecondaryRadioButton |
| `MaterialDesignActionAccentToggleButton` | ToggleButton | 操作按钮；强调色(已废弃) | MaterialDesignActionSecondaryToggleButton |
| `MaterialDesignChoiceChipAccentListBox` | ListBox | 单选芯片；强调色(已废弃) | MaterialDesignChoiceChipSecondaryListBox |
| `MaterialDesignChoiceChipAccentListBoxItem` | ListBoxItem | 单选芯片；强调色(已废弃) | MaterialDesignChoiceChipSecondaryListBoxItem |
| `MaterialDesignChoiceChipAccentOutlineListBox` | ListBox | 单选芯片；强调色(已废弃) | MaterialDesignChoiceChipSecondaryOutlineListBox |
| `MaterialDesignChoiceChipAccentOutlineListBoxItem` | ListBoxItem | 单选芯片；强调色(已废弃) | MaterialDesignChoiceChipSecondaryOutlineListBoxItem |
| `MaterialDesignChoiceChipAccentOutlineRadioButton` | RadioButton | 单选芯片；强调色(已废弃) | MaterialDesignChoiceChipSecondaryOutlineRadioButton |
| `MaterialDesignChoiceChipAccentRadioButton` | RadioButton | 单选芯片；强调色(已废弃) | MaterialDesignChoiceChipSecondaryRadioButton |
| `MaterialDesignFilterChipAccentCheckBox` | CheckBox | 筛选芯片；强调色(已废弃) | MaterialDesignFilterChipSecondaryCheckBox |
| `MaterialDesignFilterChipAccentListBoxItem` | ListBoxItem | 筛选芯片；强调色(已废弃) | MaterialDesignFilterChipSecondaryListBoxItem |
| `MaterialDesignFilterChipAccentListBox` | ListBox | 筛选芯片；强调色(已废弃) | MaterialDesignFilterChipSecondaryListBox |
| `MaterialDesignFilterChipAccentOutlineCheckBox` | CheckBox | 筛选芯片；强调色(已废弃) | MaterialDesignFilterChipSecondaryOutlineCheckBox |
| `MaterialDesignFilterChipAccentOutlineListBox` | ListBox | 筛选芯片；强调色(已废弃) | MaterialDesignFilterChipSecondaryOutlineListBox |
| `MaterialDesignFilterChipAccentOutlineListBoxItem` | ListBoxItem | 筛选芯片；强调色(已废弃) | MaterialDesignFilterChipSecondaryOutlineListBoxItem |
| `MaterialDesignFlatAccentButton` | ButtonBase | 扁平(无阴影)；强调色(已废弃) | MaterialDesignFlatSecondaryMidBgButton |
| `MaterialDesignFlatAccentBgButton` | ButtonBase | 扁平(无阴影)；强调色(已废弃) | MaterialDesignFlatSecondaryBgButton |
| `MaterialDesignFloatingActionMiniAccentButton` | ButtonBase | 悬浮操作按钮FAB；操作按钮；强调色(已废弃)；迷你尺寸 | MaterialDesignFloatingActionMiniSecondaryButton |
| `MaterialDesignFloatingActionAccentButton` | ButtonBase | 悬浮操作按钮FAB；操作按钮；强调色(已废弃) | MaterialDesignFloatingActionSecondaryButton |
| `MaterialDesignMultiFloatingActionAccentPopupBox` | PopupBox | 悬浮操作按钮FAB；操作按钮；强调色(已废弃) | MaterialDesignMultiFloatingActionSecondaryPopupBox |
| `MaterialDesignNavigationAccentListBoxItem` | ListBoxItem | 导航项；强调色(已废弃) | MaterialDesignNavigationSecondaryListBoxItem |
| `MaterialDesignNavigationAccentListBox` | ListBox | 导航项；强调色(已废弃) | MaterialDesignNavigationSecondaryListBox |
| `MaterialDesignRaisedAccentButton` | ButtonBase | 凸起实心(带阴影)；强调色(已废弃) | MaterialDesignRaisedSecondaryButton |
| `MaterialDesignSwitchAccentToggleButton` | ToggleButton | 开关Switch；强调色(已废弃) | MaterialDesignSwitchSecondaryToggleButton |

