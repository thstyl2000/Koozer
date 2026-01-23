# Track


A track object 
## Examples
[https://api.deezer.com/track/3135556](https://developers.deezer.com/api/explorer?url=track/3135556 "https://api.deezer.com/track/3135556")
## Fields
Name | Description | Type
--- | --- | ---
id | The track's Deezer id | int
readable | true if the track is readable in the player for the current user | boolean
title | The track's fulltitle | string
title_short | The track's short title | string
title_version | The track version | string
unseen | The track unseen status | boolean
isrc | The track isrc | string
link | The url of the track on Deezer | url
share | The share link of the track on Deezer | url
duration | The track's duration in seconds | int
track_position | The position of the track in its album | int
disk_number | The track's album's disk number | int
rank | The track's Deezer rank | int
release_date | The track's release date | date
explicit_lyrics | Whether the track contains explicit lyrics | boolean
explicit_content_lyrics | The explicit content lyrics values (0:Not Explicit; 1:Explicit; 2:Unknown; 3:Edited; 6:No Advice Available) | int
explicit_content_cover | The explicit cover value (0:Not Explicit; 1:Explicit; 2:Unknown; 3:Edited; 6:No Advice Available) | int
preview | The url of track's preview file. This file contains the first 30 seconds of the track | url
bpm | Beats per minute | float
gain | Signal strength | float
available_countries | List of countries where the track is available | list
alternative | Return an alternative readable track if the current track is not readable | track
contributors | Return a list of contributors on the track | list
md5_image | string | 
track_token | The track token for media service | string
artist | [artist](https://developers.deezer.com/api/artist "artist") object containing : id, name, link, share, picture, picture_small, picture_medium, picture_big, picture_xl, nb_album, nb_fan, radio, tracklist, role | object
album | [album](https://developers.deezer.com/api/album "album") object containing : id, title, link, cover, cover_small, cover_medium, cover_big, cover_xl, release_date | object
## Actions
These actions are avaible by passing a get parameter named 'request_method' to the request.
request_method | Needed Permissions | Description | Required params
--- | --- | --- | ---
POST | manage_library | Update a personal track | 
DELETE | delete_library | Delete a personal track | 
## Related actions
You may as well perform actions related to 'track' through the following methods :
### [playlist / tracks](https://developers.deezer.com/api/playlist/tracks "playlist / tracks")
request_method | Needed Permissions | Description | Required params | Param description | Type
--- | --- | --- | --- | --- | ---
POST | manage_library | Add a track to the playlist | songs | A comma separated list of track ids | string
POST | manage_library | Order tracks in the playlist | order | A comma separated list of track ids | string
DELETE | manage_librarydelete_library | Remove tracks from the playlist | songs | A comma separated list of track ids | string
### [user / tracks](https://developers.deezer.com/api/user/tracks "user / tracks")
request_method | Needed Permissions | Description | Required params | Param description | Type
--- | --- | --- | --- | --- | ---
POST | manage_library | Add track(s) to the user's favorites |  |  | 
DELETE | manage_librarydelete_library | Remove a track from the user's favorites | track_id | The id of the track | int
