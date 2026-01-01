# Koozer
> :warning: **Under Construction**: Nothing really works (yet...)

## Guidelines
- [Official Kodi Add-on development guidelines](https://kodi.wiki/view/Add-on_development)
- [Official Kodi Add-on repository guidelines](https://kodi.wiki/view/Add-on_repositories)
- [Official Kodi Add-on repository rules](https://kodi.wiki/view/Add-on_rules)
- [Official Kodi Add-on repository structure](https://kodi.wiki/view/Add-on_structure)
- [Official Deezer development guidelines](https://developers.deezer.com/guidelines)
- [Deezer API](https://developers.deezer.com/api)

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
- A GitHub Actions workflow builds repository artifacts and deploys them to GitHub Pages.
- Nightly builds run on every push to `main` and append a `.dev<run_number>` suffix to the add-on version so Kodi can detect updates between releases automatically.
- Tagged release runs are triggered only from tags that strictly follow the `vMAJOR.MINOR.PATCH` pattern; these runs publish artifacts using the exact tag version without a `.dev` suffix.
- Both nightly and release runs expect a clean working tree before publishing. Create and push a properly formatted tag to bump the version for a release instead of editing `addon.xml`; the workflow will inject the tag-derived version (or the version from `addon.xml` if none exist) into the packaged artifacts automatically.
- Before tagging a release, update `addon.xml`'s `<news>` entry and the root-level `changelog.txt` with the same versioned notes to keep release metadata in sync.
- Enable GitHub Pages for the repository (using the `gh-pages` branch created by the workflow) and point Kodi to the published URL to receive updates.

## Usage
- Install the add-on via the GitHub-hosted repository (auto-updates):
  1. In Kodi, add a new file source that points to `https://thstyl2000.github.io/Koozer/`.
  2. Install the repository ZIP from that source; Kodi will pick up future updates automatically whenever commits land on `main`.
- Install manually as a ZIP from the Kodi add-on browser if you prefer a one-off install.
- Configure the preferred country code and chart size from the add-on settings dialog.
- Browse charts from the home directory entry and play available preview URLs where offered by the Deezer API.
