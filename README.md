# lenfon-marketplace

lenfon 的个人 WorkBuddy 用户市场，收录 WPF/.NET 桌面开发方向的自研技能，源码托管于 GitHub，**可直接用 WorkBuddy 安装**。

| 维度 | 内容 |
|---|---|
| 市场名 | lenfon-marketplace |
| 安装地址 | `https://github.com/LenFon/lenfon-marketplace`（main 分支） |
| 属主 | lenfon |
| 收录方向 | WPF / .NET 桌面开发 |

## 插件清单

| 插件 | 版本 | 方向 | 说明 |
|---|---|---|---|
| `material-design-styles` | 1.0.0 | WPF 样式 | MaterialDesignInXamlToolkit 命名样式参考与 WPF 控件样式选型指南（基于最新稳定版 v5.3.2）。 |
| `wpf-basic-template` | 1.4.0 | WPF 脚手架 | 用户标准化 WPF 脚手架（Prism 9 + Material Design 5【默认 MD3 样式】+ CommunityToolkit.Mvvm + CPM + slnx + src 分层）。 |
| `prism-assistant` | 1.0.0 | Prism 参考 | Prism for WPF 使用参考助手：基于官方 PrismLibrary/Prism 与 Prism-Samples-Wpf 示例归纳的 MVVM / 导航 / 模块 / 对话框 / 事件聚合真实用法与避坑清单。 |

## 技能编写规范

本市场所有技能遵循 CodeBuddy Skills 规范（https://www.codebuddy.cn/docs/ide/Features/Skills）：

| 规范项 | 落实方式 |
|---|---|
| 目录结构 | `SKILL.md` + 可选 `scripts/`（可执行代码）、`references/`（按需加载文档）、`assets/`（输出用模板） |
| frontmatter | 必填 `name` + `description`；`description` 明确写出「功能 + 何时使用」的触发场景 |
| 正文指令 | 用祈使句 / 动词开头，不用第二人称 |
| 渐进式披露 | 元数据常驻 → SKILL.md 正文（<5k 词）→ references 按需加载 |
| 避免重复 | 长清单、维护流程、坑位明细一律下沉 `references/`，SKILL.md 只留流程 + 速查表 + 资源索引 |

## 在 WorkBuddy 中安装

在 WorkBuddy 对话中直接发送下面这句即可（AI 会代为添加并启用插件）：

> 请添加插件市场 https://github.com/LenFon/lenfon-marketplace ，并安装、启用其中的 material-design-styles、wpf-basic-template 与 prism-assistant。

如需仅安装部分插件，去掉不需要的插件名即可；也可直接描述需求（如「从市场 lenfon-marketplace 安装 prism-assistant 技能」），WorkBuddy 会自动从市场拉取并安装到用户级技能目录。

**更新插件**：对话中再次发送市场安装指令即可拉取最新版；或进入市场目录执行 `git pull`。

## 目录结构

```
lenfon-marketplace/            # 即 GitHub 仓库根，clone 后即为市场
├── README.md                  # 本说明
├── LICENSE
├── .codebuddy-plugin/
│   └── marketplace.json       # 市场清单（name + plugins 登记）
└── plugins/
    ├── material-design-styles/   # 插件：MaterialDesign 命名样式参考
    │   ├── .codebuddy-plugin/plugin.json
    │   ├── SKILL.md
    │   ├── README.md
    │   └── references/       # MD样式分类清单.md + 维护与月度更新.md
    ├── wpf-basic-template/       # 插件：用户标准化 WPF 脚手架
    │   ├── .codebuddy-plugin/plugin.json
    │   ├── SKILL.md
    │   ├── README.md
    │   ├── references/       # 6 篇：布局/代码风格/Prism 与 UI/坑位/编译验证/模板清单
    │   └── assets/           # 全套模板文件（slnx/分层 src/...）
    └── prism-assistant/         # 插件：Prism for WPF 使用参考助手
        ├── .codebuddy-plugin/plugin.json
        ├── SKILL.md
        ├── README.md
        ├── references/          # 分主题用法文档
        └── assets/             # HTML 指南（人类可读带样式版）
```
