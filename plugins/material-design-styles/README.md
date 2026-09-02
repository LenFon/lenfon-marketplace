# material-design-styles

WorkBuddy 技能：MaterialDesignInXamlToolkit（Material Design In XAML Toolkit）命名样式参考与 WPF 控件样式选型指南。

## 用途

在 WPF / Material Design 项目中需要「选样式」「配色」「Raised / Flat / Outlined / FloatingHint / Filled 变体」「MD2 vs MD3」时使用。基于最新稳定版源码整理，跨文件同名键已按主定义文件归并。

## 校验版本

- **v5.3.2**（最新稳定版；NuGet `MaterialDesignThemes` / `MaterialDesignColors` 5.3.2，目标框架 .NET 10）
- 命名样式统计（去重后唯一）：**405** 个
  - Material Design 2.0（经典 / 共享核心）：350
  - Material Design 3.0（专属新增）：28
  - 已废弃（非 2.0 / 3.0）：25
  - 默认映射：2

## 目录结构

```
material-design-styles/
├── SKILL.md                       # 技能说明（锁定版本、用法、版本要点）
├── references/
│   └── MD样式分类清单.md           # 完整命名样式清单（按 MD2 / MD3 / 已废弃分组）
├── LICENSE                        # MIT 许可证
└── .gitignore
```

## 安装方式

本技能托管在 GitHub，推荐直接在 WorkBuddy 对话框里安装，无需手动复制文件。

### 方式一：通过 WorkBuddy 对话框安装（推荐）

1. 复制本仓库地址：`https://github.com/LenFon/material-design-styles`
2. 在 WorkBuddy 对话框中发送安装指令，例如：

   > 安装这个技能：https://github.com/LenFon/material-design-styles

   或直接描述需求（如"从 GitHub 安装 material-design-styles 技能"），WorkBuddy 会自动从仓库拉取并安装到用户级技能目录。
3. 安装完成后，在任意对话中输入 `@skill:material-design-styles` 即可调用。

> 安装位置默认为用户级技能目录 `~/.workbuddy/skills/material-design-styles/`，对所有项目可用。

### 方式二：手动安装（对话框不可用时）

1. 获取仓库：

   ```bash
   git clone https://github.com/LenFon/material-design-styles.git
   ```

   或直接下载 ZIP 解压。

2. 将 `material-design-styles` 文件夹复制到 WorkBuddy 技能目录之一：

   - **用户级**（所有项目可用）：`%USERPROFILE%\.workbuddy\skills\material-design-styles\`
   - **项目级**（仅当前项目）：`<你的工作区>\.workbuddy\skills\material-design-styles\`

3. 刷新或重启 WorkBuddy 会话，即可在对话中调用本技能。

> 路径说明：Windows 上 `%USERPROFILE%` 即 `C:\Users\<你的用户名>`；复制后文件夹名须保持为 `material-design-styles`（与 `SKILL.md` 中 `name` 一致）。

## 使用方式

### 在 WorkBuddy 对话中调用

- 显式调用：输入 `@skill:material-design-styles` 或 `/material-design-styles`。
- 自然语言触发：描述如"WPF 按钮用哪个 Material Design 样式""MD3 输入框怎么写"等需求，WorkBuddy 会自动匹配本技能。
- 调用后，技能会给出样式选型建议（MD2 / MD3、Raised / Flat / Outlined / FloatingHint / Filled 等变体），并引用 `references/MD样式分类清单.md` 中的命名样式键。

### 在 XAML 中引用命名样式

按技能建议，在 XAML 中以 `StaticResource` 引用命名样式：

```xml
<Button Style="{StaticResource MaterialDesignRaisedButton}" />
```

常用按钮变体：

- 实心带阴影：`MaterialDesignRaisedButton`
- 扁平无阴影：`MaterialDesignFlatButton`
- 描边透明底：`MaterialDesignOutlinedButton`
- 悬浮操作：`MaterialDesignFloatingActionButton`（支持 `Mini` / `Dark` / `Light` / `Secondary` 派生）

> 更多控件（输入框、卡片、菜单、开关等）的命名样式键，见 `references/MD样式分类清单.md`。

## 许可

本项目基于 [MIT 许可证](LICENSE) 开源。
