#!/usr/bin/env python3
"""Package the Kodi repository add-on using the upstream Repository Tools."""

from __future__ import annotations

import argparse
import io
import shutil
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))

import create_repository  # pylint: disable=wrong-import-position


ASSET_FILENAMES = ("icon.png", "fanart.jpg")
ASSET_TAGS = ("icon", "fanart")


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
    if not version or not str(version).strip():
        raise ValueError("Repository add-on version cannot be empty")

    version = str(version).strip()

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


def prepare_addon_zip(addon_zip: Path, temp_dir: Path) -> tuple[Path, str]:
    addon_xml_path, addon_version = get_addon_root_and_version(addon_zip)
    base_version = normalize_version(addon_version)

    if addon_version == base_version:
        return addon_zip, addon_version

    normalized_addon_zip = temp_dir / addon_zip.name
    with zipfile.ZipFile(addon_zip, compression=zipfile.ZIP_DEFLATED) as source_zip:
        with zipfile.ZipFile(
            normalized_addon_zip, "w", compression=zipfile.ZIP_DEFLATED
        ) as normalized_zip:
            for info in source_zip.infolist():
                contents = source_zip.read(info.filename)
                if info.filename == addon_xml_path:
                    contents = rewrite_addon_xml(contents, base_version)
                normalized_zip.writestr(info, contents)

    print(
        "Normalized add-on version for repository packaging: "
        f"{addon_version} -> {base_version}"
    )

    return normalized_addon_zip, base_version


def get_addon_root_and_version(addon_zip: Path) -> tuple[str, str]:
    with zipfile.ZipFile(addon_zip, compression=zipfile.ZIP_DEFLATED) as archive:
        roots = {Path(name).parts[0] for name in archive.namelist() if name}
        if len(roots) != 1:
            raise RuntimeError(f"Archive should contain one directory: {addon_zip}")
        root = roots.pop()

        addon_xml_path = f"{root}/addon.xml"
        with archive.open(addon_xml_path) as addon_xml_file:
            addon_metadata = ET.parse(addon_xml_file).getroot()
            version = addon_metadata.attrib.get("version")
            if version is None:
                raise RuntimeError(f"Missing add-on version in {addon_xml_path}")
    return addon_xml_path, version


def parse_addon_manifest(addon_zip: Path) -> tuple[str, str, dict[str, str]]:
    with zipfile.ZipFile(addon_zip, compression=zipfile.ZIP_DEFLATED) as archive:
        roots = {Path(name).parts[0] for name in archive.namelist() if name}
        if len(roots) != 1:
            raise RuntimeError(f"Archive should contain one directory: {addon_zip}")
        root_dir = roots.pop()

        addon_xml_path = f"{root_dir}/addon.xml"
        with archive.open(addon_xml_path) as addon_xml_file:
            addon_metadata = ET.parse(addon_xml_file).getroot()
        addon_id = addon_metadata.attrib.get("id")
        if not addon_id:
            raise RuntimeError(f"Missing add-on ID in {addon_xml_path}")

        assets: dict[str, str] = {}
        assets_root = addon_metadata.find(".//assets")
        if assets_root is not None:
            for tag in ASSET_TAGS:
                asset_value = assets_root.findtext(tag)
                if asset_value:
                    assets[tag] = asset_value

    return root_dir, addon_id, assets


def extract_addon_assets(addon_zip: Path, repository_output: Path) -> None:
    addon_root, addon_id, assets = parse_addon_manifest(addon_zip)
    if not assets:
        return

    addon_target_dir = repository_output / addon_id
    if not addon_target_dir.is_dir():
        raise FileNotFoundError(f"Repository add-on directory not found: {addon_target_dir}")

    with zipfile.ZipFile(addon_zip, compression=zipfile.ZIP_DEFLATED) as archive:
        for asset_path in assets.values():
            zip_asset_path = f"{addon_root}/{asset_path}"
            try:
                source_file = archive.open(zip_asset_path)
            except KeyError as exc:
                raise FileNotFoundError(
                    f"Missing asset {zip_asset_path} in {addon_zip}"
                ) from exc
            target_path = addon_target_dir / Path(asset_path).name
            with source_file, target_path.open("wb") as target_file:
                shutil.copyfileobj(source_file, target_file)


def normalize_version(version: str) -> str:
    return version.split(".dev", 1)[0]


def rewrite_addon_xml(xml_bytes: bytes, version: str) -> bytes:
    root = ET.fromstring(xml_bytes)
    root.attrib["version"] = version
    tree = ET.ElementTree(root)
    buffer = io.BytesIO()
    tree.write(buffer, encoding="UTF-8", xml_declaration=True)
    return buffer.getvalue()



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

    with tempfile.TemporaryDirectory() as temp_dir:
        addon_zip_for_repository, _addon_version_for_repository = prepare_addon_zip(
            addon_zip, Path(temp_dir)
        )

        create_repository.create_repository(
            [str(addon_zip_for_repository)],
            data_path=str(repository_output),
            info_path=str(addons_xml),
            checksum_path=str(addons_checksum),
            is_compressed=False,
            no_parallel=args.no_parallel,
        )
        extract_addon_assets(addon_zip_for_repository, repository_output)

    repository_source = Path(args.repository_source)
    if not repository_source.is_dir():
        raise FileNotFoundError(f"Repository add-on source folder not found: {repository_source}")

    repository_output_root = Path(args.output)
    repository_output_root.mkdir(parents=True, exist_ok=True)

    addon_version = args.addon_version
    if addon_version is None:
        addon_metadata = ET.parse(repository_source / "addon.xml").getroot()
        addon_version = addon_metadata.attrib.get("version")

    if not addon_version or not str(addon_version).strip():
        raise ValueError(
            "Repository add-on version is missing; provide --addon-version or set a version in addon.xml"
        )

    addon_version = str(addon_version).strip()

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
