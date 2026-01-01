#!/usr/bin/env python3
"""Package the Kodi repository add-on using the upstream Repository Tools."""

from __future__ import annotations

import argparse
import shutil
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))

import create_repository  # pylint: disable=wrong-import-position


ASSET_FILENAMES = ("icon.png", "fanart.jpg")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build repository artifacts with the upstream Repository Tools and "
            "package the repository add-on into a zip archive."
        )
    )
    parser.add_argument(
        "addon_zip",
        help="Path to the add-on zip that should be published in the repository",
        nargs="?",
    )
    parser.add_argument(
        "--addon-zip",
        dest="addon_zip_arg",
        help="Path to the add-on zip that should be published in the repository",
    )
    parser.add_argument(
        "--addon-version",
        help=(
            "Version to apply to the repository add-on metadata (defaults to the "
            "add-on version from the repository add-on's addon.xml)"
        ),
    )
    parser.add_argument(
        "--repository-source",
        default=Path("repository.koozer"),
        type=Path,
        help="Path to the repository add-on source folder",
    )
    parser.add_argument(
        "--output",
        default=Path("build"),
        type=Path,
        help="Base output directory for artifacts",
    )
    parser.add_argument(
        "--repository-output",
        default=Path("build/repository"),
        type=Path,
        help="Where to write the generated repository metadata",
    )
    parser.add_argument(
        "--assets-source",
        default=Path("resources/media"),
        type=Path,
        help="Directory containing the shared icon and fanart assets",
    )
    parser.add_argument(
        "--no-parallel",
        action="store_true",
        help="Build add-on sources serially via Repository Tools",
    )
    return parser.parse_args()


def update_addon_xml_version(addon_xml_path: Path, version: str) -> str:
    tree = ET.parse(addon_xml_path)
    root = tree.getroot()
    previous_version = root.attrib.get("version", "<unset>")
    root.attrib["version"] = version

    try:
        ET.indent(tree)
    except AttributeError:
        pass

    tree.write(addon_xml_path, encoding="UTF-8", xml_declaration=True)
    return previous_version


def stage_repository_addon(
    source_dir: Path,
    output_dir: Path,
    addon_version: str,
    assets_source: Path,
    repository_metadata_dir: Path,
) -> Path:
    staged_addon_dir = output_dir / source_dir.name
    if staged_addon_dir.exists():
        shutil.rmtree(staged_addon_dir)

    shutil.copytree(source_dir, staged_addon_dir)
    previous_version = update_addon_xml_version(staged_addon_dir / "addon.xml", addon_version)
    print(
        f"Updated repository add-on version from {previous_version} "
        f"to {addon_version} in {staged_addon_dir / 'addon.xml'}"
    )

    media_dir = staged_addon_dir / "resources" / "media"
    media_dir.mkdir(parents=True, exist_ok=True)
    for asset_name in ASSET_FILENAMES:
        asset_source = assets_source / asset_name
        asset_target = media_dir / asset_name
        if not asset_source.is_file():
            raise FileNotFoundError(f"Missing asset: {asset_source}")
        shutil.copy2(asset_source, asset_target)

    for metadata_file in ("addons.xml", "addons.xml.md5"):
        source_file = repository_metadata_dir / metadata_file
        if source_file.is_file():
            shutil.copy2(source_file, staged_addon_dir / metadata_file)

    return staged_addon_dir


def zip_directory(source_dir: Path, archive_path: Path) -> None:
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in source_dir.rglob("*"):
            archive.write(path, path.relative_to(source_dir.parent))



def main() -> None:
    args = parse_args()

    addon_zip_arg = args.addon_zip_arg or args.addon_zip
    if addon_zip_arg is None:
        raise ValueError("An add-on ZIP must be provided via the positional argument or --addon-zip")

    addon_zip = Path(addon_zip_arg)
    if not addon_zip.is_file():
        raise FileNotFoundError(f"Add-on ZIP not found: {addon_zip}")

    repository_output = Path(args.repository_output)
    repository_output.mkdir(parents=True, exist_ok=True)

    addons_xml = repository_output / "addons.xml"
    addons_checksum = repository_output / "addons.xml.md5"

    create_repository.create_repository(
        [str(addon_zip)],
        data_path=str(repository_output),
        info_path=str(addons_xml),
        checksum_path=str(addons_checksum),
        is_compressed=False,
        no_parallel=args.no_parallel,
    )

    repository_source = Path(args.repository_source)
    if not repository_source.is_dir():
        raise FileNotFoundError(f"Repository add-on source folder not found: {repository_source}")

    repository_output_root = Path(args.output)
    repository_output_root.mkdir(parents=True, exist_ok=True)

    addon_version = args.addon_version
    if addon_version is None:
        addon_metadata = ET.parse(repository_source / "addon.xml").getroot()
        addon_version = addon_metadata.attrib.get("version")

    staged_addon_dir = stage_repository_addon(
        repository_source,
        repository_output_root,
        addon_version,
        Path(args.assets_source),
        repository_output,
    )

    archive_path = repository_output_root / f"{staged_addon_dir.name}-{addon_version}.zip"
    if archive_path.exists():
        archive_path.unlink()

    zip_directory(staged_addon_dir, archive_path)
    print(f"Packaged repository add-on archive: {archive_path}")


if __name__ == "__main__":
    main()
