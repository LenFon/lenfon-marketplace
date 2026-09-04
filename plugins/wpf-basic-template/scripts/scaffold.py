#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WPF 标准模板一键脚手架（跨平台：Windows / macOS / Linux 任意机器可跑）。

用法:
    python scaffold.py <目标目录> <AppName> [--no-git] [--skill-dir <路径>]

功能:
    1. 复制技能 assets/ 下全部模板文件到 <目标目录>（含 .gitignore）
    2. 占位符 __APP_NAME__ 全局替换（文件内容 + 文件/目录名）
    3. git init + 首次提交（--no-git 或未装 git 时跳过）
    4. 打印后续 restore/build 命令；仅在检测到 NuGet 环境异常时附加 env 前缀

约定:
    - 纯标准库，无第三方依赖；Python >= 3.10
    - 读 utf-8-sig（吞模板残留 BOM），写 utf-8（无 BOM）
    - 重命名用 os.replace，不用 shutil.rmtree（部分受限环境拦截删除）
    - 退出码: 0=成功 1=参数/IO 错误 2=git 环节失败（文件已就位，可手动补救）
"""
import argparse
import os
import pathlib
import shutil
import subprocess
import sys

PLACEHOLDER = "__APP_NAME__"


def fail(msg: str, code: int = 1) -> int:
    print(f"[scaffold] 错误: {msg}", file=sys.stderr)
    return code


def replace_and_rename(root: pathlib.Path, app_name: str) -> int:
    """替换文件内容中的占位符，再重命名含占位符的文件/目录（自底向上）。"""
    count = 0
    for p in root.rglob("*"):
        if p.is_file():
            p.write_text(
                p.read_text(encoding="utf-8-sig").replace(PLACEHOLDER, app_name),
                encoding="utf-8",
            )
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

    target = pathlib.Path(args.target).resolve()
    if target.exists() and any(target.iterdir()):
        return fail(f"目标目录非空: {target}")

    try:
        target.mkdir(parents=True, exist_ok=True)
        shutil.copytree(assets, target, dirs_exist_ok=True)  # 纯 Python 复制，含隐藏文件
        n = replace_and_rename(target, name)
    except OSError as e:
        return fail(f"复制/替换失败: {e}")

    print(f"[scaffold] 模板文件已就位: {target}（{n} 个文件已替换占位符 -> {name}）")

    if not args.no_git and not git_setup(target):
        print("[scaffold] git 环节失败（退出码 2），后续命令仍可执行", file=sys.stderr)

    cmd = build_command()
    if cmd:
        print(f"[scaffold] cd {target} && {cmd}")
    print("[scaffold] 验收标准: 0 错 0 警")
    return 0


if __name__ == "__main__":
    sys.exit(main())
