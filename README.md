# Koozer

Kodi Deezer Add-on built following [official Kodi development guidelines](https://kodi.wiki/view/Development:Main_Page). It uses the public [Deezer API](https://developers.deezer.com/api) for chart data.

## Features
- Browse Deezer public charts and list popular tracks.
- Configure preferred market and chart size through add-on settings.
- Play available preview URLs directly inside Kodi.

## Structure
- `addon.xml` — add-on manifest and metadata.
- `default.py` — entry point invoked by Kodi.
- `resources/lib/` — Python modules containing Deezer API client and Kodi navigation code.
- `resources/language/` — localized strings following Kodi's translation conventions.
- `resources/settings.xml` — user-facing settings for chart behaviour.
- `tests/` — pytest-based unit tests for the transport layer.

## Development
1. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
2. Run unit tests:
   ```bash
   pytest
   ```

Keep Kodi-specific imports contained to the plugin entry modules so that tests can run without Kodi present. Follow PEP 8 and the Kodi Python style guidance for new code.

## Usage
- Install the add-on as a ZIP from the Kodi add-on browser.
- Configure the preferred country code and chart size from the add-on settings dialog.
- Browse charts from the home directory entry and play available preview URLs where offered by the Deezer API.
