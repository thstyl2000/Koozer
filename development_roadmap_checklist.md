# Koozer (Deezer add-on for Kodi Omega) — Development Checklist

> This is a living checklist. Treat it as the build order + “don’t forget” list.

---

## 0) Product shape (locked for finished product)

- [x] **Playback modes:** support both
  - [ ] Metadata-only browsing + Deezer preview playback (where applicable)
  - [ ] Full playback (authenticated / session-based as required)
- [x] **Auth model:** support both
  - [ ] Anonymous mode (limited features where Deezer allows)
  - [ ] Logged-in mode (user auth/session)
- [x] **Library integration:** none (pure plugin browsing)
- [x] **Offline caching:** metadata-only (no audio caching)
  - [ ] Metadata/JSON cache with TTL
  - [ ] Artwork URL caching (no local audio files)

---

## 1) Must exist from day 1 (scaffolding / architecture)

### Add-on skeleton & navigation
- [ ] Root menu routes: Home / Search / My Music / Charts / Settings / Help
- [ ] Consistent list page builder (artists / albums / playlists / tracks)
- [ ] Consistent item detail pages (album/artist/playlist)
- [ ] Pagination pattern (“Next page” item) for all list endpoints

### Deezer API client layer (single source of truth)
- [ ] Central `deezer/client.py` owning:
  - [ ] Base URL construction (no URL building in UI handlers)
  - [ ] HTTP session + headers + timeouts
  - [ ] Retry/backoff for transient errors
  - [ ] Basic rate limiting / pacing
  - [ ] Pagination helpers
  - [ ] Error mapping: 401/403/429/5xx → user-friendly error categories

### Playback pipeline isolation
- [ ] Single `deezer/playback.py` responsible for:
  - [ ] Turning a track object/id into a Kodi playable ListItem
  - [ ] Handling preview vs full playback mode selection
  - [ ] Handling auth-required playback errors cleanly
- [ ] Context menu actions: Play / Queue / Play next (where Kodi supports)

### Caching strategy (metadata only)
- [ ] TTL cache for API responses (endpoint+params+user-context keying)
  - [ ] Short TTL: charts/search
  - [ ] Long TTL: artist/album/playlist details
- [ ] Cache invalidation strategy:
  - [ ] Manual “Clear cache” action in settings
  - [ ] Automatic TTL expiry

### Settings & secret storage policy
- [ ] Settings for:
  - [ ] Playback mode: preview vs full (or auto/fallback strategy)
  - [ ] Auth: login/logout + status indicator
  - [ ] Debug logging toggle
  - [ ] Clear cache button
- [ ] Logout/reset:
  - [ ] Clears session tokens/cookies/state reliably
  - [ ] Removes user-context cache entries

### Logging & diagnostics
- [ ] Logger wrapper with levels (DEBUG/INFO/WARN/ERROR)
- [ ] Request logs: endpoint + status + duration (no secrets)
- [ ] User-friendly error dialogs/pages (no stack traces shown to user)

### Failure UX (non-negotiable)
- [ ] Every route handles:
  - [ ] No network
  - [ ] Auth expired / missing
  - [ ] Rate limited (429)
  - [ ] Empty results
  - [ ] Partial/missing fields in JSON

---

## 2) Milestones

### Milestone 1 — MVP browsing + basic playback
- [ ] Root menu + routing framework
- [ ] Charts (Top tracks / albums) list pages
- [ ] Album details → track list
- [ ] Track actions: Play / Queue / Play next
- [ ] Search:
  - [ ] Tracks
  - [ ] Albums
  - [ ] Artists
- [ ] Playback works in **preview mode** end-to-end

### Milestone 2 — Auth + “My Music” + full playback
- [ ] Login flow/session bootstrap
- [ ] Auth status indicator (logged in / anonymous)
- [ ] My Music:
  - [ ] Favorite artists
  - [ ] Favorite albums
  - [ ] Favorite playlists
- [ ] Full playback path end-to-end (with clean fallback/error handling)

### Milestone 3 — Kodi polish & metadata quality
- [ ] Metadata mapping quality:
  - [ ] title, artist, album, track number, duration, year
  - [ ] artwork: thumb/fanart where available
- [ ] Artist page → albums/top tracks
- [ ] Playlist page → tracks
- [ ] Sorting options (name/year/popularity where available)
- [ ] Search UX improvements (history, “search again”, optional filters)
- [ ] Localization scaffolding (`strings.po`) from early on

### Milestone 4 — Hardening & maintainability
- [ ] Centralized error/reporting screens
- [ ] Minimal tests:
  - [ ] API client unit tests (mocked responses)
  - [ ] Route handlers tolerate missing fields
- [ ] CI sanity checks (lint/package structure)
- [ ] Performance review:
  - [ ] Avoid N+1 requests
  - [ ] Cache tuning
  - [ ] Batch requests where feasible

---

## 3) Definition of Done (release-ready)

- [ ] Both playback modes work reliably:
  - [ ] Preview playback works without login (where Deezer allows)
  - [ ] Full playback works when logged in (or appropriate session present)
- [ ] Both auth modes supported:
  - [ ] Anonymous browsing works
  - [ ] Logged-in browsing + My Music works
- [ ] Metadata-only caching implemented (no audio caching)
- [ ] No library integration / no Kodi library writes
- [ ] No secrets appear in logs
- [ ] Clear cache + logout/reset are reliable
- [ ] All routes fail gracefully with user-friendly messaging
