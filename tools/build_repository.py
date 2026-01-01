from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Iterable, List

ROOT = Path(__file__).resolve().parent.parent
ADDON_XML = ROOT / "addon.xml"
REPO_ROOT = ROOT / "build" / "repository"


def load_addon_metadata(addon_xml: Path) -> ET.Element:
    tree = ET.parse(addon_xml)
    return tree.getroot()


def apply_version_override(
    addon_root: ET.Element, override_version: str | None, suffix: str | None
) -> str:
    base_version = override_version or addon_root.attrib["version"]
    addon_root.attrib["version"] = f"{base_version}{suffix or ''}"
    return addon_root.attrib["version"]


def copy_addon_tree(dest: Path, exclusions: Iterable[str]) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    shutil.copytree(ROOT, dest, dirs_exist_ok=True, ignore=shutil.ignore_patterns(*exclusions))


def write_addon_xml(dest_dir: Path, addon_root: ET.Element) -> Path:
    addon_xml_path = dest_dir / "addon.xml"
    tree = ET.ElementTree(addon_root)
    try:
        ET.indent(tree)  # Python 3.9+
    except AttributeError:
        pass
    tree.write(addon_xml_path, encoding="UTF-8", xml_declaration=True)
    return addon_xml_path


def create_zip(addon_dir: Path, addon_id: str, addon_version: str) -> Path:
    zip_name = f"{addon_id}-{addon_version}.zip"
    zip_path = addon_dir.parent / zip_name
    shutil.make_archive(zip_path.with_suffix(""), "zip", addon_dir)
    return zip_path


def build_addons_xml(addon_xml_files: List[Path]) -> Path:
    addons_root = ET.Element("addons")

    for addon_xml in addon_xml_files:
        addon_tree = ET.parse(addon_xml)
        addons_root.append(addon_tree.getroot())

    addons_tree = ET.ElementTree(addons_root)
    try:
        ET.indent(addons_tree)
    except AttributeError:
        pass

    addons_xml_path = REPO_ROOT / "addons.xml"
    addons_tree.write(addons_xml_path, encoding="UTF-8", xml_declaration=True)
    return addons_xml_path


def write_md5(source_file: Path) -> Path:
    digest = hashlib.md5()
    digest.update(source_file.read_bytes())
    md5_path = source_file.with_suffix(source_file.suffix + ".md5")
    md5_path.write_text(digest.hexdigest())
    return md5_path


def write_index_html(addon_id: str, repo_version: str) -> Path:
    index_path = REPO_ROOT / "index.html"
    addon_zip = f"{addon_id}-{repo_version}.zip"

    index_path.write_text(
        """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Koozer Kodi Repository</title>
    <style>
      body { font-family: sans-serif; margin: 2rem; line-height: 1.5; }
      code { background: #f6f8fa; padding: 0.2rem 0.4rem; border-radius: 4px; }
      ul { padding-left: 1.25rem; }
    </style>
  </head>
  <body>
    <h1>Koozer Kodi Repository</h1>
    <p>
      Add <code>https://thstyl2000.github.io/Koozer/</code> as a file source in Kodi
      to install the Koozer repository. Kodi will read <code>addons.xml</code> from
      this location and download updates automatically.
    </p>

    <h2>Direct Downloads</h2>
    <ul>
      <li><a href="addons.xml">addons.xml</a> (<a href="addons.xml.md5">md5</a>)</li>
      <li><a href="{addon_zip}">{addon_zip}</a></li>
    </ul>
  </body>
</html>
        """.strip()
    )

    return index_path


def main() -> None:
    exclusions = [".git", ".github", "build", "tests", "requirements-dev.txt", "*.md"]

    parser = argparse.ArgumentParser(description="Build Kodi repository artifacts")
    parser.add_argument("--version", help="Version to write into staged addon.xml")
    parser.add_argument(
        "--suffix",
        help=(
            "Optional suffix appended to the version (defaults to NIGHTLY_VERSION_SUFFIX"
            " env value)"
        ),
    )
    args = parser.parse_args()

    addon_root = load_addon_metadata(ADDON_XML)
    addon_id = addon_root.attrib["id"]
    suffix = args.suffix if args.suffix is not None else os.getenv("NIGHTLY_VERSION_SUFFIX")
    repo_version = apply_version_override(addon_root, args.version, suffix)

    staging_dir = REPO_ROOT / addon_id
    if staging_dir.exists():
        shutil.rmtree(staging_dir)

    copy_addon_tree(staging_dir, exclusions)

    staged_addon_xml = write_addon_xml(staging_dir, addon_root)
    addon_zip = create_zip(staging_dir, addon_id, repo_version)

    addons_xml = build_addons_xml([staged_addon_xml])
    md5_file = write_md5(addons_xml)
    index_html = write_index_html(addon_id, repo_version)

    print(f"Repository built at {REPO_ROOT}")
    print(f"Addon package: {addon_zip.relative_to(ROOT)}")
    print(f"addons.xml: {addons_xml.relative_to(ROOT)}")
    print(f"addons.xml.md5: {md5_file.relative_to(ROOT)}")
    print(f"index.html: {index_html.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
