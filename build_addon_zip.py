"""Build a distributable ZIP for the Kodi add-on.

The resulting archive matches Kodi's expected structure: a top-level folder
named after the add-on ID containing ``addon.xml`` and all supporting files.
This avoids installation errors such as Kodi failing to find ``addon.xml`` in
the ZIP payload.
"""
from __future__ import annotations

import shutil
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Iterable
import zipfile

ROOT = Path(__file__).resolve().parent
BUILD_DIR = ROOT / "build"

EXCLUDES = {
    ".git",
    ".github",
    "build",
    "tests",
    "requirements-dev.txt",
}

EXCLUDE_SUFFIXES = {".md"}


def _should_skip(path: Path, root: Path) -> bool:
    relative = path.relative_to(root)
    parts: Iterable[str] = relative.parts
    if parts and parts[0] in EXCLUDES:
        return True
    if path.suffix in EXCLUDE_SUFFIXES:
        return True
    return False


def stage_addon(addon_id: str) -> Path:
    staging_dir = BUILD_DIR / addon_id
    if staging_dir.exists():
        shutil.rmtree(staging_dir)
    staging_dir.mkdir(parents=True)

    for item in ROOT.iterdir():
        if _should_skip(item, ROOT):
            continue
        destination = staging_dir / item.name
        if item.is_dir():
            shutil.copytree(item, destination)
        else:
            shutil.copy2(item, destination)

    return staging_dir


def create_zip(addon_id: str, addon_version: str, source_dir: Path) -> Path:
    BUILD_DIR.mkdir(exist_ok=True)
    zip_path = BUILD_DIR / f"{addon_id}-{addon_version}.zip"
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for file_path in source_dir.rglob("*"):
            zf.write(file_path, file_path.relative_to(BUILD_DIR))
    return zip_path


def main() -> None:
    addon_xml = ET.parse(ROOT / "addon.xml").getroot()
    addon_id = addon_xml.attrib["id"]
    addon_version = addon_xml.attrib["version"]

    staging_dir = stage_addon(addon_id)
    zip_path = create_zip(addon_id, addon_version, staging_dir)
    print(f"Created {zip_path}")


if __name__ == "__main__":
    main()
