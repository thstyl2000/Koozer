from pathlib import Path
import xml.etree.ElementTree as ET

import pytest

from textwrap import dedent

from tools.package_repository_addon import update_addon_xml_version


def _write_sample_addon_xml(path: Path, version: str) -> None:
    xml_content = dedent(
        f"""
        <?xml version='1.0' encoding='UTF-8'?>
        <addon id='repository.koozer' version='{version}' name='Test Repo'>
          <extension point='xbmc.addon.repository'/>
        </addon>
        """
    ).strip()

    path.write_text(f"{xml_content}\n", encoding="utf-8")


def test_update_addon_xml_version_sets_version(tmp_path: Path) -> None:
    addon_xml = tmp_path / "addon.xml"
    _write_sample_addon_xml(addon_xml, "1.0.0")

    previous = update_addon_xml_version(addon_xml, "2.0.0")

    assert previous == "1.0.0"
    content = addon_xml.read_text(encoding="utf-8")
    assert content.startswith("<?xml version='1.0' encoding='UTF-8'?>")

    updated_version = (
        ET.parse(addon_xml).getroot().attrib.get("version")  # type: ignore[arg-type]
    )
    assert updated_version == "2.0.0"


@pytest.mark.parametrize("version", ["", None, "   "])
def test_update_addon_xml_version_rejects_empty_values(tmp_path: Path, version: str | None) -> None:
    addon_xml = tmp_path / "addon.xml"
    _write_sample_addon_xml(addon_xml, "1.0.0")

    with pytest.raises(ValueError):
        update_addon_xml_version(addon_xml, version or "")
