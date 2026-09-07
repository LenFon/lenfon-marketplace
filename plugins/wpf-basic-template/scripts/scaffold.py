#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WPF 标准模板一键脚手架（跨平台：Windows / macOS / Linux 任意机器可跑）。

用法:
    python scaffold.py <目标目录> <AppName> [--owner <公司/组织名>] [--license <协议>] [--no-git] [--skill-dir <路径>]

功能:
    1. 复制技能 assets/ 下全部模板文件到 <目标目录>（含 .gitignore）
    2. 占位符 __APP_NAME__（项目名）、__OWNER__（版权所有者）、__YEAR__（年份）全局替换（文件内容 + 文件/目录名）
    3. 按 --license 选择协议生成根目录 LICENSE（默认 mit；可选 mit / apache-2.0 / bsd-3-clause / mpl-2.0 / gpl-3.0）
    4. git init + 首次提交（--no-git 或未装 git 时跳过）
    5. 打印后续 restore/build 命令；仅在检测到 NuGet 环境异常时附加 env 前缀

版权所有者约定:
    - LICENSE 的版权所有者用 __OWNER__ 占位，应为公司 / 组织名，**不是**项目名
    - 未传 --owner 时，默认带出 git 用户名（git config user.name）；无 git 则回退 OS 登录名
    - 有交互终端时，创建者会看到默认值并被要求确认 / 覆盖；非交互（如 CI / 智能体）直接用默认值

协议约定:
    - 协议模板在 scripts/licenses/ 下，文件名即协议标识（如 MIT.txt）；创建时由脚手架按 --license 写入根 LICENSE
    - 默认 mit（最常用）；其余可选 apache-2.0 / bsd-3-clause / mpl-2.0 / gpl-3.0（含常见别名，如 apache / gpl）
    - 年份用 __YEAR__ 占位，默认当前年

约定:
    - 纯标准库，无第三方依赖；Python >= 3.10
    - 读 utf-8-sig（吞模板残留 BOM），写 utf-8（无 BOM）
    - 重命名用 os.replace，不用 shutil.rmtree（部分受限环境拦截删除）
    - 退出码: 0=成功 1=参数/IO 错误 2=git 环节失败（文件已就位，可手动补救）
"""
import argparse
import datetime
import os
import pathlib
import shutil
import subprocess
import sys

PLACEHOLDER = "__APP_NAME__"
OWNER_PLACEHOLDER = "__OWNER__"
YEAR_PLACEHOLDER = "__YEAR__"

# 协议模板目录（相对技能根 scripts/ 下），不随 assets 拷贝进新项目
LICENSE_DIR = "licenses"
DEFAULT_LICENSE = "mit"
# 协议标识（含常见别名，小写）→ 模板文件名
LICENSE_ALIASES = {
    "mit": "MIT.txt",
    "apache": "Apache-2.0.txt",
    "apache-2.0": "Apache-2.0.txt",
    "apache2.0": "Apache-2.0.txt",
    "bsd": "BSD-3-Clause.txt",
    "bsd-3": "BSD-3-Clause.txt",
    "bsd-3-clause": "BSD-3-Clause.txt",
    "mpl": "MPL-2.0.txt",
    "mpl-2.0": "MPL-2.0.txt",
    "mpl2.0": "MPL-2.0.txt",
    "gpl": "GPL-3.0.txt",
    "gpl-3": "GPL-3.0.txt",
    "gpl-3.0": "GPL-3.0.txt",
    "gpl3": "GPL-3.0.txt",
    "gpl3.0": "GPL-3.0.txt",
}


def fail(msg: str, code: int = 1) -> int:
    print(f"[scaffold] 错误: {msg}", file=sys.stderr)
    return code


def resolve_license(skill_dir: str, license_arg: str | None):
    """解析协议模板文件，返回 (模板文件名, Path)；未知协议返回 (None, None)。"""
    lic_dir = pathlib.Path(skill_dir) / "scripts" / LICENSE_DIR
    key = (license_arg or DEFAULT_LICENSE).strip().lower()
    fname = LICENSE_ALIASES.get(key)
    if not fname:
        return None, None
    p = lic_dir / fname
    if not p.is_file():
        return None, None
    return fname, p


def write_license(target: pathlib.Path, lic_path: pathlib.Path, owner: str, year: str) -> None:
    """按所选协议生成根目录 LICENSE，替换版权所有者与年份占位符。"""
    text = lic_path.read_text(encoding="utf-8-sig")
    text = text.replace(OWNER_PLACEHOLDER, owner).replace(YEAR_PLACEHOLDER, year)
    (target / "LICENSE").write_text(text, encoding="utf-8")


def get_git_user() -> str:
    """取 git 配置 user.name 作为版权所有者默认值（无 git / 未配置则返回 None）。"""
    if shutil.which("git") is None:
        return None
    try:
        r = subprocess.run(
            ["git", "config", "user.name"],
            capture_output=True, text=True, timeout=10,
        )
        return r.stdout.strip() or None
    except Exception:
        return None


def confirm_owner(default: str) -> str:
    """无 --owner 时交互确认版权所有者（公司 / 组织名），默认带出 git 用户名。

    非交互（无 tty / 管道）或读取失败时直接回退默认值，不阻塞。
    """
    try:
        if not sys.stdin.isatty():
            return default
        val = input(f"版权所有者（公司/组织名，默认 git 用户名「{default}」）: ").strip()
        return val or default
    except (EOFError, OSError):
        return default


def replace_and_rename(root: pathlib.Path, app_name: str, owner: str, year: str) -> int:
    """替换文件内容中的占位符，再重命名含占位符的文件/目录（自底向上）。"""
    count = 0
    for p in root.rglob("*"):
        if p.is_file():
            text = p.read_text(encoding="utf-8-sig")
            text = (
                text.replace(PLACEHOLDER, app_name)
                .replace(OWNER_PLACEHOLDER, owner)
                .replace(YEAR_PLACEHOLDER, year)
            )
            p.write_text(text, encoding="utf-8")
            count += 1
    for p in sorted(root.rglob(f"*{PLACEHOLDER}*"), key=lambda x: len(x.parts), reverse=True):
        new = p.with_name(p.name.replace(PLACEHOLDER, app_name))
        os.replace(p, new)
    return count


def git_setup(root: pathlib.Path) -> bool:
    """git init + 全量首次提交。未装 git 或身份未配置时不阻塞（文件已就位）。"""
    if shutil.which("git") is None:
        print("[scaffold] 未检测到 git，跳过仓库初始化（可装 git 后手动 git init）", file=sys.stderr)
        return True  # 不视为失败

    def run(*args: str) -> subprocess.CompletedProcess:
        return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)

    if run("init").returncode != 0:
        print("[scaffold] git init 失败（目录权限？），可手动执行: git init", file=sys.stderr)
        return False
    run("add", "-A")
    commit = run("commit", "-m", "chore: scaffold from wpf-basic-template")
    if commit.returncode != 0:
        # 常见原因: 未配置 user.name / user.email
        print(f"[scaffold] git commit 未完成: {commit.stderr.strip()}", file=sys.stderr)
        print("[scaffold] 文件与仓库已就位，配置好身份后手动执行: git add -A && git commit", file=sys.stderr)
        return False
    print("[scaffold] git init + 首次提交完成")
    return True


def nuget_env_ok() -> bool:
    """Windows 下检测 NuGet 所需环境变量是否健康。

    受限 shell（沙箱 / CI）常见两种异常：APPDATA/PROGRAMFILES 缺失，或
    HOME 为 POSIX 风格（如 /c/Users/xxx）导致 NuGet 报 path1 null。
    此时需要显式 env 前缀；环境正常则直接 dotnet restore 即可。
    非 Windows 恒为 True。
    """
    if os.name != "nt":
        return True
    appdata = os.environ.get("APPDATA", "")
    home = os.environ.get("HOME", "")
    progfiles = os.environ.get("PROGRAMFILES", "")
    home_ok = bool(home) and "\\" in home and not home.startswith("/")
    return bool(appdata) and home_ok and bool(progfiles)


def build_command() -> str:
    """生成 restore+build 命令；NuGet 环境异常时按当前机器环境变量补 env 前缀。"""
    plain = "dotnet restore && dotnet build --no-restore"
    if nuget_env_ok():
        return plain

    # 从本机环境变量派生，绝不硬编码用户名 / 路径
    profile = (os.environ.get("USERPROFILE") or "").replace("/", "\\")
    if os.name != "nt" or "\\" not in profile:
        print("[scaffold] 警告：无法从环境变量推导 NuGet 所需路径（USERPROFILE 缺失或非 Windows 风格），"
              "若 restore 报 path1 null 请手动注入 APPDATA/HOME/PROGRAMFILES")
        return plain
    appdata = (os.environ.get("APPDATA", "").replace("/", "\\")
               or profile + "\\AppData\\Roaming")
    progfiles = os.environ.get("PROGRAMFILES", "") or os.environ.get("SystemDrive", "C:") + "\\Program Files"

    bash_prefix = f"env APPDATA='{appdata}' HOME='{profile}' PROGRAMFILES='{progfiles}'"
    print("[scaffold] 检测到 NuGet 环境异常（path1 null 坑），bash 下用第一行；PowerShell 用第二组：")
    print(f"[scaffold] {bash_prefix} {plain}")
    print("[scaffold] PowerShell: 先逐行执行 "
          f"$env:APPDATA='{appdata}'; $env:HOME='{profile}'; $env:PROGRAMFILES='{progfiles}' 再运行 {plain}")
    return ""


def main() -> int:
    parser = argparse.ArgumentParser(description="WPF 标准模板一键脚手架（跨平台）")
    parser.add_argument("target", help="新解决方案根目录（不存在则创建）")
    parser.add_argument("app_name", help="项目名（同时用于解决方案与根命名空间）")
    parser.add_argument("--owner", default=None,
                        help="版权所有者（公司/组织名，写入 LICENSE）；省略则默认 git 用户名并交互确认")
    parser.add_argument("--license", default=DEFAULT_LICENSE,
                        help="开源协议（默认 mit）；可选 mit / apache-2.0 / bsd-3-clause / mpl-2.0 / gpl-3.0（含别名）")
    parser.add_argument("--no-git", action="store_true", help="跳过 git init + 首次提交")
    parser.add_argument(
        "--skill-dir",
        default=str(pathlib.Path(__file__).resolve().parent.parent),
        help="技能根目录（默认取脚本所在位置上一级）",
    )
    args = parser.parse_args()

    # C# 根命名空间合法性：字母/下划线开头，仅含字母数字下划线与点段
    name = args.app_name.strip()
    if not name or any(not (seg.isidentifier()) for seg in name.split(".")):
        return fail(f"非法项目名: {args.app_name!r}（每段须为合法 C# 标识符，如 MyApp.Core）")

    assets = pathlib.Path(args.skill_dir) / "assets"
    if not assets.is_dir():
        return fail(f"模板 assets 目录不存在: {assets}")

    # 协议解析（早失败：未知协议不浪费拷贝）
    lic_name, lic_path = resolve_license(args.skill_dir, args.license)
    if lic_path is None:
        avail = ", ".join(sorted(set(LICENSE_ALIASES)))
        return fail(f"未知协议: {args.license!r}（可选: {avail}）")

    target = pathlib.Path(args.target).resolve()
    if target.exists() and any(target.iterdir()):
        return fail(f"目标目录非空: {target}")

    # 版权所有者：--owner 优先，否则默认 git 用户名（无 git 则 OS 登录名）并交互确认
    try:
        os_login = os.getlogin()
    except OSError:
        os_login = ""
    owner_default = get_git_user() or os_login or "Unknown"
    owner = args.owner.strip() if args.owner else confirm_owner(owner_default)
    year = str(datetime.date.today().year)

    try:
        target.mkdir(parents=True, exist_ok=True)
        shutil.copytree(assets, target, dirs_exist_ok=True)  # 纯 Python 复制，含隐藏文件
        n = replace_and_rename(target, name, owner, year)
        write_license(target, lic_path, owner, year)  # 生成根 LICENSE（所选协议）
    except OSError as e:
        return fail(f"复制/替换失败: {e}")

    print(f"[scaffold] 模板文件已就位: {target}（{n} 个文件已替换占位符 -> {name}）")
    print(f"[scaffold] 版权所有者（LICENSE）: {owner}")
    print(f"[scaffold] 开源协议（LICENSE）: {lic_name}")

    if not args.no_git and not git_setup(target):
        print("[scaffold] git 环节失败（退出码 2），后续命令仍可执行", file=sys.stderr)

    cmd = build_command()
    if cmd:
        print(f"[scaffold] cd {target} && {cmd}")
    print("[scaffold] 验收标准: 0 错 0 警")
    return 0


if __name__ == "__main__":
    sys.exit(main())
