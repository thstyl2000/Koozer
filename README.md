# Koozer
> :warning: **Under Construction**: Nothing really works (yet...)

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

### Repository publishing
- A GitHub Actions workflow builds repository artifacts from `main` on every push and deploys them to GitHub Pages.
- Nightly builds append a `.dev<run_number>` suffix to the add-on version so Kodi can see new updates automatically.
- Enable GitHub Pages for the repository (using the `gh-pages` branch created by the workflow) and point Kodi to the published URL to receive updates.
- Add-on versions are sourced from Git tags that follow the `vMAJOR.MINOR.PATCH` pattern. Create a tag to bump the version for a release instead of editing `addon.xml`; the workflow will inject the tag-derived version (or `0.0.0` if none exist) into the packaged artifacts automatically.
- Release publishing is gated by a preflight check that requires a clean working tree and a properly formatted release tag, so ensure commits are pushed and tagged before triggering a release run.

## Usage
- Install the add-on via the GitHub-hosted repository (auto-updates):
  1. In Kodi, add a new file source that points to `https://thstyl2000.github.io/Koozer/`.
  2. Install the repository ZIP from that source; Kodi will pick up future updates automatically whenever commits land on `main`.
- Install manually as a ZIP from the Kodi add-on browser if you prefer a one-off install.
- Configure the preferred country code and chart size from the add-on settings dialog.
- Browse charts from the home directory entry and play available preview URLs where offered by the Deezer API.
