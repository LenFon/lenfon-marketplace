# lenfon-marketplace

lenfon 的个人 WorkBuddy 用户市场，收录 WPF/.NET 桌面开发方向的自研技能，源码托管于 GitHub，**可直接用 WorkBuddy 安装**。

| 维度 | 内容 |
|---|---|
| 市场名 | lenfon-marketplace |
| 安装地址 | `https://github.com/LenFon/lenfon-marketplace`（main 分支） |
| 属主 | lenfon |
| 收录方向 | WPF / .NET 桌面开发 |
| 收录插件 | `material-design-styles` v1.0.0（MaterialDesignInXamlToolkit 样式参考与控件选型指南）<br>`wpf-basic-template` v1.4.0（Prism 9 + Material Design 5 标准化 WPF 脚手架） |

## 在 WorkBuddy 中安装

在 WorkBuddy 对话中直接发送下面这句即可（AI 会代为添加并启用插件）：

> 请添加插件市场 https://github.com/LenFon/lenfon-marketplace ，并安装、启用其中的 material-design-styles 与 wpf-basic-template。

## 目录结构

```
lenfon-marketplace/            # 即 GitHub 仓库根，clone 后即为市场
├── README.md                  # 本说明
├── .codebuddy-plugin/
│   └── marketplace.json       # 市场清单（name + plugins 登记）
└── plugins/
    ├── material-design-styles/   # 插件：MaterialDesign 命名样式参考
    │   ├── .codebuddy-plugin/plugin.json
    │   ├── SKILL.md
    │   ├── README.md
    │   └── references/MD样式分类清单.md
    └── wpf-basic-template/       # 插件：用户标准化 WPF 脚手架
        ├── .codebuddy-plugin/plugin.json
        ├── SKILL.md
        ├── README.md
        └── templates/           # 全套模板文件（slnx/分层 src/...）
```
