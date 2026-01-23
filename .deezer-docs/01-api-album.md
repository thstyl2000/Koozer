# Album
  * [ALBUM METHODS](https://developers.deezer.com/api/album#tab_connections)


An album object 
## Examples
[https://api.deezer.com/album/302127](https://developers.deezer.com/api/explorer?url=album/302127 "https://api.deezer.com/album/302127")
## Fields
Name | Description | Type
--- | --- | ---
id | The Deezer album id | int
title | The album title | string
upc | The album UPC | string
link | The url of the album on Deezer | url
share | The share link of the album on Deezer | url
cover | The url of the album's cover. Add 'size' parameter to the url to change size. Can be 'small', 'medium', 'big', 'xl' | url
cover_small | The url of the album's cover in size small. | url
cover_medium | The url of the album's cover in size medium. | url
cover_big | The url of the album's cover in size big. | url
cover_xl | The url of the album's cover in size xl. | url
md5_image | string | 
genre_id | The album's first genre id (You should use the genre list instead). NB : -1 for not found | int
genres | List of genre object | list
label | The album's label name | string
provider | The album's provider name | string
nb_tracks | int | 
duration | The album's duration (seconds) | int
fans | The number of album's Fans | int
release_date | The album's release date | date
record_type | The record type of the album (EP / ALBUM / etc..) | string
available | boolean | 
alternative | Return an alternative album object if the current album is not available | object
tracklist | API Link to the tracklist of this album | url
explicit_lyrics | Whether the album contains explicit lyrics | boolean
explicit_content_lyrics | The explicit content lyrics values (0:Not Explicit; 1:Explicit; 2:Unknown; 3:Edited; 4:Partially Explicit (Album "lyrics" only); 5:Partially Unknown (Album "lyrics" only); 6:No Advice Available; 7:Partially No Advice Available (Album "lyrics" only)) | int
explicit_content_cover | The explicit cover values (0:Not Explicit; 1:Explicit; 2:Unknown; 3:Edited; 4:Partially Explicit (Album "lyrics" only); 5:Partially Unknown (Album "lyrics" only); 6:No Advice Available; 7:Partially No Advice Available (Album "lyrics" only)) | int
contributors | Return a list of contributors on the album | list
fallback | Return fallback album with id and status | object
artist | [artist](https://developers.deezer.com/api/artist "artist") object containing : id, name, picture, picture_small, picture_medium, picture_big, picture_xl | object
**tracks** | list of [track](https://developers.deezer.com/api/track "track") | list
id | The track's Deezer id | int
readable | true if the track is readable in the player for the current user | boolean
title | The track's fulltitle | string
title_short | The track's short title | string
title_version | The track version | string
link | The url of the track on Deezer | url
duration | The track's duration in seconds | int
rank | The track's Deezer rank | int
explicit_lyrics | Whether the track contains explicit lyrics | boolean
preview | The url of track's preview file. This file contains the first 30 seconds of the track | url
artist | [artist](https://developers.deezer.com/api/artist "artist") object containing : id, name | object
album | [album](https://developers.deezer.com/api/album "album") object containing : id, title, cover, cover_small, cover_medium, cover_big, cover_xl | object
## Related actions
You may as well perform actions related to 'album' through the following methods :
### [user / albums](https://developers.deezer.com/api/user/albums "user / albums")
request_method | Needed Permissions | Description | Required params | Param description | Type
--- | --- | --- | --- | --- | ---
POST | manage_library | Add album(s) to the user's library |  |  | 
DELETE | manage_librarydelete_library | Remove an album from the user's library | album_id | The id of the album | int
## Connections
Name | Description | Returns
--- | --- | ---
[album / fans](https://developers.deezer.com/api/album/fans "album / fans") | Return a list of album's fans. Represented by an array of User objects | A list of object of type [user](https://developers.deezer.com/api/user "user")
[album / tracks](https://developers.deezer.com/api/album/tracks "album / tracks") | Return a list of album's tracks. Represented by an array of Track objects | A list of object of type [track](https://developers.deezer.com/api/track "track")
