# lenfon-marketplace（本地用户市场）

> **市场描述**：lenfon 的个人本地用户市场——以 `directory` 型固化在本机，
> 内容不会被远程同步覆盖，用于长期沉淀自定义技能与插件。
> 当前收录 WPF/.NET 桌面开发方向技能，持续扩充中。

| 维度 | 内容 |
|---|---|
| 名称 | lenfon-marketplace |
| 类型 | directory（本地目录市场，无远程同步覆盖） |
| 属主 | lenfon |
| 收录方向 | WPF / .NET 桌面开发 |
| 收录插件 | `material-design-styles`（MaterialDesignInXamlToolkit 样式参考与控件选型指南）<br>`wpf-basic-template`（Prism 9 + Material Design 5 标准化 WPF 脚手架） |
| 展示描述 | `marketplace.json` 的 `description` / `description_en`（UI 市场页展示用） |

## 目录结构

```
lenfon-marketplace/
├── .codebuddy-plugin/
│   └── marketplace.json          # 市场清单（注册到 known_marketplaces.json）
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

## 注册与启用

1. 市场已在 `C:\Users\PC\.workbuddy\plugins\known_marketplaces.json` 注册
   （键 `lenfon-marketplace`，`type: directory`，指向本目录）。
2. 插件已安装并启用：启用键位于 `settings.json` 的 `enabledPlugins`，
   安装本体位于 `plugins/cache/lenfon-marketplace/<插件>/<版本>/`。
3. 重启 WorkBuddy 生效。

> 迁移说明：同名技能原位于 `~/.workbuddy/skills/`，启用市场版本前已备份至
> `~/.workbuddy/standalone-skills-backup-20260902/`，可随时移回回滚。

## 添加新插件

把技能目录复制到 `plugins/<name>/`，补写 `.codebuddy-plugin/plugin.json`，
再在 `.codebuddy-plugin/marketplace.json` 的 `plugins` 数组中登记一项即可。

- 版本格式需为 `x.y.z` 语义化版本。
- `plugin.json.skills` 用相对插件根目录的路径，如 `./SKILL.md`。
- 发布形态不含 `.git` / `.gitignore` / `LICENSE`。
