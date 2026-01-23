# Artist
  * [ARTIST METHODS](https://developers.deezer.com/api/artist#tab_connections)


An artist object 
## Examples
[https://api.deezer.com/artist/27](https://developers.deezer.com/api/explorer?url=artist/27 "https://api.deezer.com/artist/27")
## Fields
Name | Description | Type
--- | --- | ---
id | The artist's Deezer id | int
name | The artist's name | string
link | The url of the artist on Deezer | url
share | The share link of the artist on Deezer | url
picture | The url of the artist picture. Add 'size' parameter to the url to change size. Can be 'small', 'medium', 'big', 'xl' | url
picture_small | The url of the artist picture in size small. | url
picture_medium | The url of the artist picture in size medium. | url
picture_big | The url of the artist picture in size big. | url
picture_xl | The url of the artist picture in size xl. | url
nb_album | The number of artist's albums | int
nb_fan | The number of artist's fans | int
radio | true if the artist has a smartradio | boolean
tracklist | API Link to the top of this artist | url
## Related actions
You may as well perform actions related to 'artist' through the following methods :
### [user / artists](https://developers.deezer.com/api/user/artists "user / artists")
request_method | Needed Permissions | Description | Required params | Param description | Type
--- | --- | --- | --- | --- | ---
POST | manage_library | Add artist(s) to the user's favorites |  |  | 
DELETE | manage_librarydelete_library | Remove an artist from the user's favorites | artist_id | The id of the artist | int
## Connections
Name | Description | Returns
--- | --- | ---
[artist / top](https://developers.deezer.com/api/artist/top "artist / top") | Get the top 5 tracks of an artist | A list of object of type [track](https://developers.deezer.com/api/track "track")
[artist / albums](https://developers.deezer.com/api/artist/albums "artist / albums") | Return a list of artist's albums. Represented by an array of Album objects | A list of object of type [album](https://developers.deezer.com/api/album "album")
[artist / fans](https://developers.deezer.com/api/artist/fans "artist / fans") | Return a list of artist's fans. Represented by an array of User objects | A list of object of type [user](https://developers.deezer.com/api/user "user")
[artist / related](https://developers.deezer.com/api/artist/related "artist / related") | Return a list of related artists. Represented by an array of Artist objects | A list of object of type [artist](https://developers.deezer.com/api/artist "artist")
[artist / radio](https://developers.deezer.com/api/artist/radio "artist / radio") | Return a list of tracks. Represented by an array of Track object | A list of object of type [track](https://developers.deezer.com/api/track "track")
[artist / playlists](https://developers.deezer.com/api/artist/playlists "artist / playlists") | Return a list of artist's playlists. Represented by an array of Playlist object | A list of object of type [playlist](https://developers.deezer.com/api/playlist "playlist")
