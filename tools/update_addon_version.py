from __future__ import annotations

import argparse
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ADDON_XML = ROOT / "addon.xml"


def update_addon_version(version: str) -> None:
    tree = ET.parse(ADDON_XML)
    root = tree.getroot()

    previous_version = root.attrib.get("version")
    root.attrib["version"] = version

    try:
        ET.indent(tree)  # Python 3.9+
    except AttributeError:
        pass

    tree.write(ADDON_XML, encoding="UTF-8", xml_declaration=True)

    print(f"Updated addon.xml version from {previous_version} to {version}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Update add-on version in addon.xml")
    parser.add_argument("version", help="Version string to write")

    args = parser.parse_args()

    update_addon_version(args.version)


if __name__ == "__main__":
    main()
