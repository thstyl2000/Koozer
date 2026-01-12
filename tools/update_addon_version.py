from __future__ import annotations

import argparse
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ADDON_XML = [
    ROOT / "plugin.audio.koozer" / "addon.xml",
    ROOT / "repository.koozer" / "addon.xml",
]


def update_addon_version(version: str) -> None:
    updates: list[str] = []
    for path in ADDON_XML:
        tree = ET.parse(path)
        root = tree.getroot()

        previous_version = root.attrib.get("version")
        root.attrib["version"] = version

        try:
            ET.indent(tree)  # Python 3.9+
        except AttributeError:
            pass

        tree.write(path, encoding="UTF-8", xml_declaration=True)
        updates.append(f"{path} {previous_version} -> {version}")

    print("Updated addon.xml versions: " + ", ".join(updates))


def main() -> None:
    parser = argparse.ArgumentParser(description="Update add-on version in addon.xml")
    parser.add_argument("version", help="Version string to write")

    args = parser.parse_args()

    update_addon_version(args.version)


if __name__ == "__main__":
    main()
