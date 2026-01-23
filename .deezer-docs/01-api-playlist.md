# Playlist
  * [PLAYLIST METHODS](https://developers.deezer.com/api/playlist#tab_connections)


A playlist object 
## Examples
[https://api.deezer.com/playlist/908622995](https://developers.deezer.com/api/explorer?url=playlist/908622995 "https://api.deezer.com/playlist/908622995")
## Fields
Name | Description | Type
--- | --- | ---
id | The playlist's Deezer id | int
title | The playlist's title | string
description | The playlist description | string
duration | The playlist's duration (seconds) | int
public | If the playlist is public or not | boolean
is_loved_track | If the playlist is the love tracks playlist | boolean
collaborative | If the playlist is collaborative or not | boolean
nb_tracks | Nb tracks in the playlist | int
unseen_track_count | Nb tracks not seen | int
fans | The number of playlist's fans | int
link | The url of the playlist on Deezer | url
share | The share link of the playlist on Deezer | url
picture | The url of the playlist's cover. Add 'size' parameter to the url to change size. Can be 'small', 'medium', 'big', 'xl' | url
picture_small | The url of the playlist's cover in size small. | url
picture_medium | The url of the playlist's cover in size medium. | url
picture_big | The url of the playlist's cover in size big. | url
picture_xl | The url of the playlist's cover in size xl. | url
checksum | The checksum for the track list | string
creator | [user](https://developers.deezer.com/api/user "user") object containing : id, name | object
**tracks** | list of [track](https://developers.deezer.com/api/track "track") | list
id | The track's Deezer id | int
readable | true if the track is readable in the player for the current user | boolean
title | The track's fulltitle | string
title_short | The track's short title | string
title_version | The track version | string
unseen | The track unseen status | boolean
isrc | The track isrc | string
link | The url of the track on Deezer | url
duration | The track's duration in seconds | int
rank | The track's Deezer rank | int
explicit_lyrics | Whether the track contains explicit lyrics | boolean
preview | The url of track's preview file. This file contains the first 30 seconds of the track | url
time_add | The time when the track has been added to the playlist | timestamp
artist | [artist](https://developers.deezer.com/api/artist "artist") object containing : id, name, link | object
album | [album](https://developers.deezer.com/api/album "album") object containing : id, title, upc, cover, cover_small, cover_medium, cover_big, cover_xl | object
## Actions
These actions are avaible by passing a get parameter named 'request_method' to the request.
request_method | Needed Permissions | Description | Required params
--- | --- | --- | ---
POST | manage_library | Update the playlist | 
DELETE | delete_library | Delete the playlist | 
## Related actions
You may as well perform actions related to 'playlist' through the following methods :
### [user / playlists](https://developers.deezer.com/api/user/playlists "user / playlists")
request_method | Needed Permissions | Description | Required params | Param description | Type
--- | --- | --- | --- | --- | ---
POST | manage_library | Create a playlist | title | The title of the new playlist | string
POST | manage_library | Add playlist(s) to the user's favorites |  |  | 
DELETE | manage_librarydelete_library | Remove a playlist from the user's favorites | playlist_id | The id of the playlist | int
## Connections
Name | Description | Returns
--- | --- | ---
[playlist / seen](https://developers.deezer.com/api/playlist/seen "playlist / seen") | GET method is not available. Please check POST methods. | 
[playlist / fans](https://developers.deezer.com/api/playlist/fans "playlist / fans") | Return a list of playlist's fans. Represented by an array of User objects | A list of object of type [user](https://developers.deezer.com/api/user "user")
[playlist / tracks](https://developers.deezer.com/api/playlist/tracks "playlist / tracks") | Return a list of playlist's tracks. Represented by an array of Track object | A list of object of type [track](https://developers.deezer.com/api/track "track")
[playlist / radio](https://developers.deezer.com/api/playlist/radio "playlist / radio") | Return a list of playlist's recommendation tracks. Represented by an array of Track object | A list of object of type [track](https://developers.deezer.com/api/track "track")
