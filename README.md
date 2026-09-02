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

### 方式一：界面操作（推荐）
1. 打开 WorkBuddy → 进入插件 / 技能（市场）管理页面；
2. 选择「添加插件市场」，粘贴安装地址：
   ```
   https://github.com/LenFon/lenfon-marketplace
   ```
3. 确认后 WorkBuddy 自动拉取仓库并识别出 `lenfon-marketplace`；
4. 在市场详情中安装并启用插件：`material-design-styles`、`wpf-basic-template`；
5. 重启 WorkBuddy（或新开会话）后即可在技能列表中调用。

### 方式二：让 AI 代装
在 WorkBuddy 对话中直接发送下面这句即可（AI 会代为添加并启用插件）：

> 请添加插件市场 https://github.com/LenFon/lenfon-marketplace ，并安装、启用其中的 material-design-styles 与 wpf-basic-template。

### 方式三：CLI（可选，CodeBuddy Code 命令行）
```bash
codebuddy plugin marketplace add https://github.com/LenFon/lenfon-marketplace -n lenfon-marketplace
codebuddy plugin install material-design-styles@lenfon-marketplace
codebuddy plugin install wpf-basic-template@lenfon-marketplace
```

## 更新市场内容

市场源更新并推送（`git push origin main`）后，使用方在 WorkBuddy 市场管理中对 `lenfon-marketplace` 执行「更新 / 刷新」即可同步，或运行：

```bash
codebuddy plugin marketplace update lenfon-marketplace
```

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

插件目录内不含 `.git` / `.gitignore` / `LICENSE` 等仓库元数据，保持发布形态干净。

## 维护：添加新插件并发布

1. 复制技能目录到 `plugins/<name>/`；
2. 补写 `plugins/<name>/.codebuddy-plugin/plugin.json`（版本格式 `x.y.z`，`skills` 用相对插件根的路径如 `./SKILL.md`）；
3. 在 `.codebuddy-plugin/marketplace.json` 的 `plugins` 数组登记一项；
4. 提交推送发布：
   ```bash
   git add -A
   git commit -m "feat: 新增插件 <name>"
   git push origin main
   ```
5. 使用方对市场执行「更新」即可看到新插件。

## 本机既有安装（2026-09 首装，无需重装）

本机仍以 `directory` 型注册在 `known_marketplaces.json` 并直连本目录，插件已启用（启用键 `material-design-styles@lenfon-marketplace`、`wpf-basic-template@lenfon-marketplace`）。本仓库即该本地目录的 git 镜像与分发源，功能等价。
