"""Generate a simple index.html for the published Kodi repository."""
from __future__ import annotations

from pathlib import Path


def write_index_html(datadir: Path, addon_id: str, addon_version: str) -> Path:
    datadir.mkdir(parents=True, exist_ok=True)
    index_path = datadir / "index.html"
    addon_zip = f"{addon_id}-{addon_version}.zip"

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


__all__ = ["write_index_html"]
