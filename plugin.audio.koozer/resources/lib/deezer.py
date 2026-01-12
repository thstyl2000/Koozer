"""HTTP client for Deezer's public API.

The implementation keeps Kodi-specific logic out of the transport layer so
it can be unit tested without a running Kodi instance.
"""
from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional


class DeezerError(RuntimeError):
    """Raised when the Deezer API responds with an error."""


@dataclass
class Track:
    """Represents a Deezer track used by the plugin UI."""

    identifier: str
    title: str
    artist: str
    album: str
    duration: int
    preview_url: Optional[str]


class DeezerClient:
    """Minimal Deezer API client tailored for the plugin workflow.

    The client purposefully keeps Kodi imports out of the transport layer and
    follows the public Deezer API contract documented at
    https://developers.deezer.com/api. The documentation link is preserved for
    developer reference when updating endpoints or payload parsing.
    """

    def __init__(
        self,
        opener: Optional[urllib.request.OpenerDirector] = None,
        base_url: str = "https://api.deezer.com",
    ) -> None:
        self._opener = opener or urllib.request.build_opener()
        self._base_url = base_url

    def get_chart_tracks(self, limit: int = 25, country: Optional[str] = None) -> List[Track]:
        """Return popular tracks for the configured market."""

        params: Dict[str, str | int] = {"limit": limit}
        if country:
            params["country"] = country

        query = urllib.parse.urlencode(params)
        url = f"{self._base_url}/chart?{query}"
        payload = self._request_json(url)
        tracks_payload = payload.get("tracks")
        if not isinstance(tracks_payload, dict):
            return []
        track_nodes = tracks_payload.get("data", [])
        if not isinstance(track_nodes, list):
            return []
        return [self._parse_track(node) for node in track_nodes if isinstance(node, dict)]

    def _request_json(self, url: str) -> Dict[str, object]:
        try:
            with self._opener.open(url, timeout=10) as response:  # type: ignore[attr-defined]
                body = response.read()
        except urllib.error.HTTPError as error:
            message = self._extract_error_message(error)
            raise DeezerError(message) from error
        except urllib.error.URLError as error:
            reason = getattr(error, "reason", "Network error")
            raise DeezerError(str(reason)) from error
        return json.loads(body.decode("utf-8"))

    def _extract_error_message(self, error: urllib.error.HTTPError) -> str:
        try:
            body = error.read()
            payload = json.loads(body.decode("utf-8"))
        except Exception:  # Kodi style: fallback to HTTP status text when parsing fails
            return error.reason if hasattr(error, "reason") else "Unexpected Deezer error"

        error_details = payload.get("error") if isinstance(payload, dict) else None
        if isinstance(error_details, dict):
            return str(error_details.get("message", "Unexpected Deezer error"))
        return "Unexpected Deezer error"

    def _parse_track(self, node: Dict[str, object]) -> Track:
        album = self._extract_nested_title(node, "album")
        artist = self._extract_nested_title(node, "artist")
        preview = node.get("preview")
        preview_url = preview if isinstance(preview, str) and preview else None
        duration = self._coerce_int(node.get("duration"))

        return Track(
            identifier=str(node.get("id", "")),
            title=str(node.get("title", "")),
            artist=artist,
            album=album,
            duration=duration,
            preview_url=preview_url,
        )

    @staticmethod
    def _coerce_int(value: object, default: int = 0) -> int:
        if isinstance(value, bool):
            return int(value)
        if isinstance(value, int):
            return value
        if isinstance(value, float):
            return int(value)
        if isinstance(value, str):
            try:
                return int(value)
            except ValueError:
                return default
        return default

    @staticmethod
    def _extract_nested_title(node: Dict[str, object], key: str) -> str:
        nested = node.get(key)
        if isinstance(nested, dict):
            title = nested.get("title")
            if isinstance(title, str):
                return title
        return ""
