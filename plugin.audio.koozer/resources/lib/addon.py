"""Kodi-facing add-on entry point and navigation helpers."""
from __future__ import annotations

import sys
from typing import Dict, List, Optional
from urllib.parse import urlencode, parse_qs

import xbmcaddon
import xbmcgui
import xbmcplugin

from resources.lib.deezer import DeezerClient, DeezerError, Track


class KoozerAddon:
    """Kodi plugin controller."""

    def __init__(
        self, base_url: str, handle: int, query: str, client: Optional[DeezerClient] = None
    ) -> None:
        self._base_url = base_url
        self._handle = handle
        self._query = query
        self._client = client or DeezerClient()
        self._addon = xbmcaddon.Addon()

    @classmethod
    def from_kodi_args(cls, argv: List[str]) -> "KoozerAddon":
        base_url = argv[0]
        handle = int(argv[1])
        query = argv[2]
        return cls(base_url, handle, query)

    def run(self) -> None:
        params = self._parse_params(self._query)
        action = params.get("action", "list_home")

        if action == "list_charts":
            self._list_charts()
        elif action == "play_preview":
            preview_url = params.get("url")
            if preview_url:
                self._play_preview(preview_url)
            else:
                self._notify(self._addon.getLocalizedString(32004))
        elif action == "open_settings":
            self._addon.openSettings()
        else:
            self._list_home()

    def _list_home(self) -> None:
        self._add_directory_item(
            heading=self._addon.getLocalizedString(32000),
            query={"action": "list_charts"},
            is_folder=True,
        )
        self._add_directory_item(
            heading=self._addon.getLocalizedString(32003),
            query={"action": "open_settings"},
            is_folder=False,
        )
        xbmcplugin.endOfDirectory(self._handle, succeeded=True)

    def _list_charts(self) -> None:
        country = self._get_setting_string("market").strip()
        limit = self._get_setting_int("chart_limit")
        if limit <= 0:
            limit = 25
        try:
            tracks = self._client.get_chart_tracks(limit=limit, country=country or None)
        except DeezerError as error:
            self._notify(str(error))
            xbmcplugin.endOfDirectory(self._handle, succeeded=False)
            return

        xbmcplugin.setContent(self._handle, "songs")
        for track in tracks:
            self._add_track_item(track)
        xbmcplugin.addSortMethod(self._handle, xbmcplugin.SORT_METHOD_LABEL)
        xbmcplugin.addSortMethod(self._handle, xbmcplugin.SORT_METHOD_DURATION)
        xbmcplugin.endOfDirectory(self._handle, succeeded=True)

    def _play_preview(self, preview_url: str) -> None:
        list_item = xbmcgui.ListItem(path=preview_url)
        list_item.setProperty("IsPlayable", "true")
        xbmcplugin.setResolvedUrl(self._handle, succeeded=True, listitem=list_item)

    def _add_track_item(self, track: Track) -> None:
        list_item = xbmcgui.ListItem(label=track.title)
        list_item.setProperty("IsPlayable", "true")
        list_item.setInfo(
            "music",
            {
                "title": track.title,
                "artist": track.artist,
                "album": track.album,
                "duration": track.duration,
            },
        )

        if track.preview_url:
            list_item.setPath(track.preview_url)
        list_item.addContextMenuItems(
            [
                (
                    self._addon.getLocalizedString(32002),
                    f"RunPlugin({self._build_url({'action': 'open_settings'})})",
                )
            ]
        )

        xbmcplugin.addDirectoryItem(
            handle=self._handle,
            url=self._build_url(
                {"action": "play_preview", "url": track.preview_url or ""}
            ),
            listitem=list_item,
            isFolder=False,
        )

    def _add_directory_item(self, heading: str, query: Dict[str, str], is_folder: bool) -> None:
        url = self._build_url(query)
        list_item = xbmcgui.ListItem(label=heading)
        xbmcplugin.addDirectoryItem(self._handle, url=url, listitem=list_item, isFolder=is_folder)

    def _build_url(self, query: Dict[str, str]) -> str:
        return f"{self._base_url}?{urlencode(query)}"

    @staticmethod
    def _parse_params(query: str) -> Dict[str, str]:
        clean_query = query[1:] if query.startswith("?") else query
        raw_params = parse_qs(clean_query)
        return {key: value[0] for key, value in raw_params.items()}

    def _notify(self, message: str) -> None:
        xbmcgui.Dialog().notification(
            heading="Koozer",
            message=message,
            icon=xbmcgui.NOTIFICATION_INFO,
            time=5000,
            sound=False,
        )

    def _get_setting_string(self, setting_id: str) -> str:
        try:
            return self._addon.getSettingString(setting_id)
        except (AttributeError, TypeError):
            return self._addon.getSetting(setting_id)

    def _get_setting_int(self, setting_id: str) -> int:
        try:
            return self._addon.getSettingInt(setting_id)
        except (AttributeError, TypeError, ValueError):
            raw_value = self._addon.getSetting(setting_id)
            try:
                return int(raw_value)
            except (TypeError, ValueError):
                return 0


def run_plugin() -> None:
    """Script entry point for Kodi."""

    addon = KoozerAddon.from_kodi_args(sys.argv)
    addon.run()


if __name__ == "__main__":
    run_plugin()
