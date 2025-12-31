from __future__ import annotations

import io
import json
import urllib.error
from typing import Dict, List

import pytest

from resources.lib.deezer import DeezerClient, DeezerError, Track


class _StubResponse:
    def __init__(self, payload: Dict[str, object]):
        self._body = json.dumps(payload).encode("utf-8")

    def read(self) -> bytes:  # pragma: no cover - trivial
        return self._body

    def __enter__(self) -> "_StubResponse":  # pragma: no cover - trivial
        return self

    def __exit__(self, exc_type, exc, tb) -> None:  # pragma: no cover - trivial
        return None


class _StubOpener:
    def __init__(self, response):
        self.response = response
        self.last_url = None

    def open(self, url: str, timeout: int = 0):
        self.last_url = url
        if isinstance(self.response, Exception):
            raise self.response
        return self.response


def test_get_chart_tracks_parses_tracks() -> None:
    payload = {
        "tracks": {
            "data": [
                {
                    "id": "1",
                    "title": "Song",
                    "artist": {"title": "Artist"},
                    "album": {"title": "Album"},
                    "duration": 180,
                    "preview": "https://example.test/preview.mp3",
                }
            ]
        }
    }
    response = _StubResponse(payload)
    opener = _StubOpener(response)

    client = DeezerClient(opener=opener)

    tracks: List[Track] = client.get_chart_tracks(limit=10, country="GB")

    assert opener.last_url == "https://api.deezer.com/chart?limit=10&country=GB"
    assert len(tracks) == 1
    track = tracks[0]
    assert track.title == "Song"
    assert track.artist == "Artist"
    assert track.album == "Album"
    assert track.duration == 180
    assert track.preview_url == "https://example.test/preview.mp3"


def test_get_chart_tracks_raises_deezer_error_on_failure() -> None:
    payload = {"error": {"message": "Invalid query"}}
    error_body = io.BytesIO(json.dumps(payload).encode("utf-8"))
    http_error = urllib.error.HTTPError(
        url="https://api.deezer.com/chart",
        code=403,
        msg="Forbidden",
        hdrs=None,
        fp=error_body,
    )
    opener = _StubOpener(http_error)

    client = DeezerClient(opener=opener)

    with pytest.raises(DeezerError) as error:
        client.get_chart_tracks()

    assert "Invalid query" in str(error.value)


def test_get_chart_tracks_handles_url_error() -> None:
    opener = _StubOpener(urllib.error.URLError(reason="Timeout"))

    client = DeezerClient(opener=opener)

    with pytest.raises(DeezerError) as error:
        client.get_chart_tracks()

    assert "Timeout" in str(error.value)
