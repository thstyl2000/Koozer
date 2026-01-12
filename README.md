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
- `plugin.audio.koozer/addon.xml` — add-on manifest and metadata.
- `plugin.audio.koozer/default.py` — entry point invoked by Kodi.
- `plugin.audio.koozer/resources/lib/` — Python modules containing Deezer API client and Kodi navigation code.
- `plugin.audio.koozer/resources/language/` — localized strings following Kodi's translation conventions.
- `plugin.audio.koozer/resources/settings.xml` — user-facing settings for chart behaviour.
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
- The GitHub Actions workflow distinguishes between dev and stable channels.
- Merges to `main` build alpha-tagged add-on zips (for example, `1.2.3-alpha.4`) and publish the repository feed plus add-on zips to the `dev` branch under `repository-dev/`. The `repository.koozer.dev` installer points to those raw artifacts on `raw.githubusercontent.com`.
- Stable publishing runs only on manual dispatches and version tags (`vMAJOR.MINOR.PATCH`). These runs build release artifacts and deploy the repository feed to GitHub Pages (`gh-pages`) for the stable `repository.koozer` installer.
- Repository add-on installers are treated as unversioned; their `addon.xml` versions remain fixed (currently `1.0.0`) regardless of dev/stable builds.
- Before tagging a release, update `plugin.audio.koozer/addon.xml`'s `<news>` entry and `plugin.audio.koozer/changelog.txt` with the same versioned notes to keep release metadata in sync.
- Package repository artifacts locally with the upstream Repository Tools by first creating an add-on ZIP for the repository feed (for example, `build/plugin.audio.koozer-0.0.0.zip`) and then running:
  ```bash
  python tools/package_repository_addon.py \
    --addon-zip build/plugin.audio.koozer-0.0.0.zip \
    --output build/repository-addon
  ```
  This builds `addons.xml` under `build/repository` and produces an installable repository add-on ZIP in `build/repository-addon`. The add-on ZIP used here is only for the repository feed and should not be distributed for standalone installation.

## Usage
- Install the stable repository add-on for automatic updates:
  1. Download the latest `repository.koozer-1.0.0.zip` from the GitHub Releases page (tag builds) or the workflow artifacts for manual dispatches.
  2. In Kodi, go to **Add-ons > Install from zip file** and select the downloaded repository ZIP.
  3. Once installed, open **Add-ons > Install from repository > Koozer Repository > Music add-ons > Koozer** to install the add-on itself; future updates will be delivered automatically through the stable repository.
- Install the dev repository add-on for alpha updates:
  1. Download `repository.koozer.dev-1.0.0.zip` from `https://raw.githubusercontent.com/thstyl2000/Koozer/dev/repository-dev/repository-addon/repository.koozer.dev-1.0.0.zip`.
  2. In Kodi, go to **Add-ons > Install from zip file** and select the downloaded repository ZIP.
  3. Once installed, open **Add-ons > Install from repository > Koozer Dev Repository > Music add-ons > Koozer** to install the dev build; future updates will follow the alpha feed.
- Configure the preferred country code and chart size from the add-on settings dialog.
- Browse charts from the home directory entry and play available preview URLs where offered by the Deezer API.
