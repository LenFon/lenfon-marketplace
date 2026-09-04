#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""核对 Directory.Packages.props 中全部包是否为 nuget.org 最新稳定版。

用途（wpf-basic-template 维护约定）：新建项目时 / 手动更新模板时运行一次，
替代已取消的月度巡检。纯标准库实现，无第三方依赖。

用法：
    python check-package-versions.py [Directory.Packages.props 路径]
    缺省路径为当前目录下的 Directory.Packages.props。

退出码：0 = 全部为最新稳定版；1 = 存在可升级包；2 = 运行出错（文件不存在 / 网络 / 解析）。
"""

import argparse
import json
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

# 成对包：版本必须严格一致（不一致即报 WARN，即使各自都是最新稳定版）
PAIRED_PACKAGES = [
    ("Prism.Wpf", "Prism.DryIoc"),
    ("MaterialDesignThemes", "MaterialDesignThemes.MahApps"),
]

NUGET_INDEX = "https://api.nuget.org/v3-flatcontainer/{package_id}/index.json"
TIMEOUT_SECONDS = 30
COLUMN_WIDTH = 36


def is_stable(version: str) -> bool:
    """NuGet 语义化版本：预发布版含连字符段（如 9.0.537-preview、1.0.0-rc.1）。"""
    return "-" not in version


def load_package_versions(props_path: Path) -> dict[str, str]:
    """解析 CPM 文件，返回 {包名: 版本}；兼容带 / 不带 xmlns 的写法。"""
    if not props_path.is_file():
        raise FileNotFoundError(f"找不到 {props_path}")

    root = ET.parse(props_path).getroot()

    def local_name(tag: str) -> str:
        return tag.rsplit("}", 1)[-1]

    versions: dict[str, str] = {}
    for element in root.iter():
        if local_name(element.tag) != "PackageVersion":
            continue
        package_id = element.get("Include", "").strip()
        version = element.get("Version", "").strip()
        if package_id and version:
            versions[package_id] = version
    return versions


def fetch_latest_stable(package_id: str) -> str | None:
    """查询 nuget.org 全部版本并返回最新稳定版；无稳定版返回 None。"""
    url = NUGET_INDEX.format(package_id=package_id.lower())
    request = urllib.request.Request(url, headers={"User-Agent": "check-package-versions/1.0"})
    with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        data = json.load(response)
    stable = [v for v in data.get("versions", []) if is_stable(v)]
    return stable[-1] if stable else None


def check_paired_consistency(versions: dict[str, str]) -> list[str]:
    """成对包版本必须一致，返回告警文案列表。"""
    warnings: list[str] = []
    for left, right in PAIRED_PACKAGES:
        if left in versions and right in versions and versions[left] != versions[right]:
            warnings.append(
                f"WARN  成对包版本不一致：{left}={versions[left]} 与 {right}={versions[right]} 必须严格一致"
            )
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="核对 CPM 包是否为 nuget.org 最新稳定版")
    parser.add_argument(
        "props",
        nargs="?",
        default="Directory.Packages.props",
        help="Directory.Packages.props 路径（默认当前目录）",
    )
    args = parser.parse_args()

    props_path = Path(args.props)
    try:
        versions = load_package_versions(props_path)
    except (FileNotFoundError, ET.ParseError) as error:
        print(f"ERROR  {error}", file=sys.stderr)
        return 2

    if not versions:
        print(f"WARN  {props_path} 中未找到任何 PackageVersion 条目")
        return 2

    print(f"核对 {props_path}（共 {len(versions)} 个包，数据源 nuget.org）\n")
    print(f"{'包名'.ljust(COLUMN_WIDTH)}{'当前版本'.ljust(14)}{'最新稳定版'.ljust(14)}状态")
    print("-" * (COLUMN_WIDTH + 42))

    updatable: list[tuple[str, str, str]] = []
    failed: list[str] = []

    for package_id, current in versions.items():
        try:
            latest = fetch_latest_stable(package_id)
        except Exception as error:  # 网络 / 超时 / JSON 解析，逐包容错
            failed.append(package_id)
            print(f"{package_id.ljust(COLUMN_WIDTH)}{current.ljust(14)}{'-'.ljust(14)}ERROR  {error}")
            continue

        if latest is None:
            print(f"{package_id.ljust(COLUMN_WIDTH)}{current.ljust(14)}{'(无稳定版)'.ljust(14)}WARN")
            continue

        if latest == current:
            status = "OK"
        else:
            status = "UPDATE"
            updatable.append((package_id, current, latest))
        print(f"{package_id.ljust(COLUMN_WIDTH)}{current.ljust(14)}{latest.ljust(14)}{status}")

    for warning in check_paired_consistency(versions):
        print()
        print(warning)

    print()
    if failed:
        print(f"结论：{len(failed)} 个包查询失败（{', '.join(failed)}），请检查网络后重试")
        return 2
    if updatable:
        detail = ", ".join(f"{name} {current} -> {latest}" for name, current, latest in updatable)
        print(f"结论：{len(updatable)} 个包可升级 -> {detail}")
        print("同步位置：SKILL.md 索引、assets/Directory.Packages.props、assets/src/__APP_NAME__/__APP_NAME__.csproj")
        return 1
    print("结论：全部包均为最新稳定版")
    return 0


if __name__ == "__main__":
    sys.exit(main())
