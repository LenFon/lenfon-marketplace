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
| `wpf-basic-template` | 1.5.1 | WPF 脚手架 | 用户标准化 WPF 一键脚手架（Prism 9 + Material Design 5【默认 MD3 样式】+ CommunityToolkit.Mvvm + CPM + slnx + src 分层）：`scripts/scaffold.py` 一条命令完成模板拷贝（28 个文件，含 .gitignore / README.md / LICENSE）→ 占位符替换 → git init + 首次提交（跨平台纯标准库），另附包版本核对脚本（逐包查 nuget.org 最新稳定版 + 成对包一致性校验）。 |
| `prism-assistant` | 1.0.0 | Prism 参考 | Prism for WPF 使用参考助手：基于官方 PrismLibrary/Prism 与 Prism-Samples-Wpf 示例归纳的 MVVM / 导航 / 模块 / 对话框 / 事件聚合真实用法与避坑清单。 |

## 技能编写规范

本市场所有技能遵循 CodeBuddy Skills 规范（https://www.codebuddy.cn/docs/ide/Features/Skills ）：

| 规范项 | 落实方式 |
|---|---|
| 目录结构 | `SKILL.md` + 可选 `scripts/`（可执行代码）、`references/`（按需加载文档）、`assets/`（输出用模板） |
| frontmatter | 必填 `name` + `description`；`description` 明确写出「功能 + 何时使用」的触发场景 |
| 正文指令 | 用祈使句 / 动词开头，不用第二人称 |
| 渐进式披露 | 元数据常驻 → SKILL.md 正文（<5k 词）→ references 按需加载 |
| 避免重复 | 长清单、维护流程、坑位明细一律下沉 `references/`，SKILL.md 只留流程 + 速查表 + 资源索引 |

## 添加市场与安装插件

在 WorkBuddy 对话中直接发送下面这句即可（AI 会代为添加并启用插件）：

> 请添加插件市场 https://github.com/LenFon/lenfon-marketplace ，并安装、启用其中的 material-design-styles、wpf-basic-template 与 prism-assistant。

如需仅安装部分插件，去掉不需要的插件名即可；也可直接描述需求（如「从市场 lenfon-marketplace 安装 prism-assistant 技能」），WorkBuddy 会自动从市场拉取并安装到用户级技能目录。

**更新插件**：对话中再次发送市场安装指令即可拉取最新版；或进入市场目录执行 `git pull`。插件安装后落在 `~/.workbuddy/plugins/cache/lenfon-marketplace/<插件>/<版本>/`，运行时只从该版本化快照加载。

### 手动安装（AI 代装失败时的兜底方案）

部分机器上，直接让 WorkBuddy 的 AI 代为添加市场 / 插件可能不生效（例如客户端版本差异、或 AI 未正确执行安装流程）。此时可用下面的**本地手动方式**，效果等价且可复现，适合给其他机器批量部署。

**前置条件**：已安装 Git，且 WorkBuddy 至少完整启动过一次（会自动创建 `~/.workbuddy/plugins/` 等目录）。

**步骤 1 — 克隆市场**

```powershell
git clone --depth 1 https://github.com/LenFon/lenfon-marketplace.git "$env:USERPROFILE\.workbuddy\plugins\marketplaces\lenfon-marketplace"
```

克隆完成后，WorkBuddy 一般会自动把该目录识别并注册为本地市场（`known_marketplaces.json` 中出现 `lenfon-marketplace`，`type: directory`）。若没有自动出现，按文末「注册条目参考」手动补齐即可。

**步骤 2–4 — 安装并启用插件（一键脚本）**

把下面脚本保存为仓库根目录的 `install.py` 并运行（自动把全部插件装进 `cache/`、登记 `installed_plugins.json`、启用 `settings.json`）：

```python
import json, os, shutil
from datetime import datetime, timezone

HOME = os.path.expanduser("~")
MARKET = "lenfon-marketplace"
MROOT = os.path.join(HOME, ".workbuddy", "plugins", "marketplaces", MARKET)
PDIR = os.path.join(HOME, ".workbuddy", "plugins")
CACHE = os.path.join(PDIR, "cache", MARKET)
_ms = datetime.now().microsecond // 1000
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.") + f"{_ms:03d}Z"

mkt = json.load(open(os.path.join(MROOT, ".codebuddy-plugin", "marketplace.json"), encoding="utf-8"))
plugins = mkt["plugins"]

# 1) known_marketplaces.json（仅当缺失时补齐）
km_path = os.path.join(PDIR, "known_marketplaces.json")
km = json.load(open(km_path, encoding="utf-8"))
if MARKET not in km:
    km[MARKET] = {
        "manifestName": MARKET,
        "type": "directory",
        "source": {"source": "directory", "path": MROOT},
        "installLocation": MROOT,
        "description": f"Marketplace from https://github.com/LenFon/{MARKET}",
        "lastUpdated": NOW,
        "autoUpdate": False,
        "isBuiltIn": False,
    }
    json.dump(km, open(km_path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print("已注册市场:", MARKET)

# 2) 安装到 cache + 登记 installed_plugins.json
ip_path = os.path.join(PDIR, "installed_plugins.json")
ip = json.load(open(ip_path, encoding="utf-8"))
ip.setdefault("plugins", {})
# 3) settings.json
s_path = os.path.join(HOME, ".workbuddy", "settings.json")
s = json.load(open(s_path, encoding="utf-8"))
s.setdefault("enabledPlugins", {})

for p in plugins:
    name = p["name"]
    ver = p.get("version", "1.0.0")
    src = os.path.join(MROOT, p.get("source", f"./plugins/{name}").lstrip("./"))
    dst = os.path.join(CACHE, name, ver)
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    key = f"{name}@{MARKET}"
    ip["plugins"][key] = [{
        "scope": "user",
        "installPath": dst,
        "version": ver,
        "installedAt": NOW,
        "lastUpdated": NOW,
    }]
    s["enabledPlugins"][key] = True
    print("已安装并启用:", key, "->", dst)

json.dump(ip, open(ip_path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
json.dump(s, open(s_path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("\n完成。请重启 WorkBuddy 使配置生效。")
```

**步骤 5 — 重启 WorkBuddy**

完全退出后重新打开，插件列表即可看到 `lenfon-marketplace` 及其技能。

**注册条目参考**（仅当步骤 1 未自动注册时，手动写入 `~/.workbuddy/plugins/known_marketplaces.json`）：

```json
"lenfon-marketplace": {
  "manifestName": "lenfon-marketplace",
  "type": "directory",
  "source": { "source": "directory", "path": "C:\\Users\\<用户名>\\.workbuddy\\plugins\\marketplaces\\lenfon-marketplace" },
  "installLocation": "C:\\Users\\<用户名>\\.workbuddy\\plugins\\marketplaces\\lenfon-marketplace",
  "description": "Marketplace from https://github.com/LenFon/lenfon-marketplace",
  "lastUpdated": "2026-01-01T00:00:00.000Z",
  "autoUpdate": false,
  "isBuiltIn": false
}
```

**原理提示**：WorkBuddy 桌面端的插件实际从 `~/.workbuddy/plugins/cache/<市场>/<插件>/<版本>/` 加载，而非直接读市场目录；因此「安装」= 把插件源目录复制进 `cache/` + 在 `installed_plugins.json` 登记 + 在 `settings.json` 的 `enabledPlugins` 写 `"<插件>@<市场>": true`。仅注册市场而不装进 `cache` / 启用，插件不会出现在可用列表里。

## 市场清单规范

本市场遵循插件市场规范（https://www.codebuddy.ai/docs/zh/cli/plugin-marketplaces ）：

| 规范项 | 落实方式 |
|---|---|
| 清单位置 | 仓库根 `.codebuddy-plugin/marketplace.json`（GitHub / Git / 本地目录型市场的标准位置） |
| 顶层必填 | `name`（kebab-case）+ `owner` + `plugins`；可选 `description`、`version` |
| 插件条目必填 | `name` + `source` + `description`；`source` 为相对市场根的路径（`./plugins/<插件>`） |
| 插件条目可选 | `version`、`author`、`homepage`、`repository`、`license`（SPDX）、`keywords`、`category`、`strict` |
| 组件声明 | `skills` 指向插件目录（本市场每个插件一个技能，入口为 `SKILL.md`） |
| 插件清单 | `strict: true`（默认）——每个插件目录都带 `.codebuddy-plugin/plugin.json`，marketplace 条目补充其元数据 |
| 版本与更新 | 市场与插件各自带 `version`；第三方市场默认不自动更新，按需 `update` 或 `git pull` |

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
    ├── wpf-basic-template/       # 插件：用户标准化 WPF 脚手架（v1.5.1）
    │   ├── .codebuddy-plugin/plugin.json
    │   ├── SKILL.md
    │   ├── README.md
    │   ├── references/       # 6 篇：布局/代码风格/Prism 与 UI/坑位/编译验证/模板清单
    │   ├── scripts/          # scaffold.py（一键脚手架，跨平台纯标准库）+ check-package-versions.py（CPM 包版本核对）
    │   └── assets/           # 全套模板文件（slnx/分层 src/.gitignore/README.md/LICENSE/...，28 个）
    └── prism-assistant/         # 插件：Prism for WPF 使用参考助手
        ├── .codebuddy-plugin/plugin.json
        ├── SKILL.md
        ├── README.md
        ├── references/          # 分主题用法文档
        └── assets/             # HTML 指南（人类可读带样式版）
```
