# Chart
  * [CHART METHODS](https://developers.deezer.com/api/chart#tab_connections)


Charts of a specified genre 
## Examples
[https://api.deezer.com/chart](https://developers.deezer.com/api/explorer?url=chart "https://api.deezer.com/chart")
## Fields
Name | Description | Type
--- | --- | ---
**tracks** | list of [track](https://developers.deezer.com/api/track "track") | list
id | The track's Deezer id | int
title | The track's fulltitle | string
title_short | The track's short title | string
title_version | The track version | string
link | The url of the track on Deezer | url
duration | The track's duration in seconds | int
rank | The track's Deezer rank | int
explicit_lyrics | Whether the track contains explicit lyrics | boolean
preview | The url of track's preview file. This file contains the first 30 seconds of the track | url
position | The position of the track in the charts | int
artist | [artist](https://developers.deezer.com/api/artist "artist") object containing : id, name, link, picture, picture_small, picture_medium, picture_big, picture_xl, radio | object
album | [album](https://developers.deezer.com/api/album "album") object containing : id, title, cover, cover_small, cover_medium, cover_big, cover_xl | object
**albums** | list of [album](https://developers.deezer.com/api/album "album") | list
id | The Deezer album id | int
title | The album title | string
link | The url of the album on Deezer | url
cover | The url of the album's cover. Add 'size' parameter to the url to change size. Can be 'small', 'medium', 'big', 'xl' | url
cover_small | The url of the album's cover in size small. | url
cover_medium | The url of the album's cover in size medium. | url
cover_big | The url of the album's cover in size big. | url
cover_xl | The url of the album's cover in size xl. | url
record_type | The record type of the album (EP / ALBUM / etc..) | string
explicit_lyrics | Whether the album contains explicit lyrics | boolean
position | The position of the album in the charts | int
artist | [artist](https://developers.deezer.com/api/artist "artist") object containing : id, name, link, picture, picture_small, picture_medium, picture_big, picture_xl, radio | object
**artists** | list of [artist](https://developers.deezer.com/api/artist "artist") | list
id | The artist's Deezer id | int
name | The artist's name | string
link | The url of the artist on Deezer | url
picture | The url of the artist picture. Add 'size' parameter to the url to change size. Can be 'small', 'medium', 'big', 'xl' | url
picture_small | The url of the artist picture in size small. | url
picture_medium | The url of the artist picture in size medium. | url
picture_big | The url of the artist picture in size big. | url
picture_xl | The url of the artist picture in size xl. | url
radio | true if the artist has a smartradio | boolean
position | The position of the artist in the charts | int
**playlists** | list of [playlist](https://developers.deezer.com/api/playlist "playlist") | list
id | The playlist's Deezer id | int
title | The playlist's title | string
public | If the playlist is public or not | boolean
link | The url of the playlist on Deezer | url
picture | The url of the playlist's cover. Add 'size' parameter to the url to change size. Can be 'small', 'medium', 'big', 'xl' | url
picture_small | The url of the playlist's cover in size small. | url
picture_medium | The url of the playlist's cover in size medium. | url
picture_big | The url of the playlist's cover in size big. | url
picture_xl | The url of the playlist's cover in size xl. | url
position | The position of the playlist in the charts | int
user | [user](https://developers.deezer.com/api/user "user") object containing : id, name | object
**podcasts** | list of [podcast](https://developers.deezer.com/api/podcast "podcast") | list
id | The podcast's Deezer id | int
title | The podcast's title | string
description | The podcast's description | string
available | If the podcast is available or not | boolean
fans | The number of podcast's fans | int
link | The url of the podcast on Deezer | url
share | The share link of the podcast on Deezer | url
picture | The url of the podcast's cover. | url
picture_small | The url of the podcast's cover in size small. | url
picture_medium | The url of the podcast's cover in size medium. | url
picture_big | The url of the podcast's cover in size big. | url
picture_xl | The url of the podcast's cover in size xl. | url
position | The position of the podcasts in the charts | int
## Connections
Name | Description | Returns
--- | --- | ---
[chart / tracks](https://developers.deezer.com/api/chart/tracks "chart / tracks") | Returns the Top tracks. | A list of object of type [track](https://developers.deezer.com/api/track "track")
[chart / albums](https://developers.deezer.com/api/chart/albums "chart / albums") | Returns the Top albums. | A list of object of type [album](https://developers.deezer.com/api/album "album")
[chart / artists](https://developers.deezer.com/api/chart/artists "chart / artists") | Returns the Top artists. | A list of object of type [artist](https://developers.deezer.com/api/artist "artist")
[chart / playlists](https://developers.deezer.com/api/chart/playlists "chart / playlists") | Returns the Top playlists. | A list of object of type [playlist](https://developers.deezer.com/api/playlist "playlist")
[chart / podcasts](https://developers.deezer.com/api/chart/podcasts "chart / podcasts") | Returns the Top podcasts. | A list of object of type [podcast](https://developers.deezer.com/api/podcast "podcast")
