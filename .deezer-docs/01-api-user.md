# User
  * [USER METHODS](https://developers.deezer.com/api/user#tab_connections)


A user object 
## Examples
[https://api.deezer.com/user/me](https://developers.deezer.com/api/explorer?url=user/me "https://api.deezer.com/user/me")
## Fields
Name | Description | Type
--- | --- | ---
id | The user's Deezer ID | int
name | The user's Deezer nickname | string
lastname | The user's last name | string
firstname | The user's first name | string
email | The user's email | string
status | The user's status | int
birthday | The user's birthday | date
inscription_date | The user's inscription date | date
gender | The user's gender : **F** or **M** | string
link | The url of the profil for the user on Deezer | url
picture | The url of the user's profil picture. Add 'size' parameter to the url to change size. Can be 'small', 'medium', 'big', 'xl' | url
picture_small | The url of the user's profil picture in size small. | url
picture_medium | The url of the user's profil picture in size medium. | url
picture_big | The url of the user's profil picture in size big. | url
picture_xl | The url of the user's profil picture in size xl. | url
country | The user's country | string
lang | The user's language | string
is_kid | If the user is a kid or not | boolean
explicit_content_level | The user's explicit content level according to his country | string
explicit_content_levels_available | The user's available explicit content levels according to his country. Possible values are: explicit_display, explicit_no_recommendation and explicit_hide | array
tracklist | API Link to the flow of this user | url
## Connections
Name | Description | Returns
--- | --- | ---
[user / albums](https://developers.deezer.com/api/user/albums "user / albums") | Return a list of user's favorite albums. Represented by an array of Album object | A list of object of type [album](https://developers.deezer.com/api/album "album")
[user / artists](https://developers.deezer.com/api/user/artists "user / artists") | Return a list of user's favorite artists. Represented by an array of Artist object | A list of object of type [artist](https://developers.deezer.com/api/artist "artist")
[user / charts](https://developers.deezer.com/api/user/charts "user / charts") | Use charts/albums, charts/playlists or charts/tracks. | 
[user / flow](https://developers.deezer.com/api/user/flow "user / flow") | Returns a list of user's flow tracks, represented by an array of Track object. | A list of object of type [track](https://developers.deezer.com/api/track "track")
[user / followings](https://developers.deezer.com/api/user/followings "user / followings") | Return a list of user's Friends, represented by an array of User object | A list of object of type [user](https://developers.deezer.com/api/user "user")
[user / followers](https://developers.deezer.com/api/user/followers "user / followers") | Return a list of user's Friends, represented by an array of User object | A list of object of type [user](https://developers.deezer.com/api/user "user")
[user / history](https://developers.deezer.com/api/user/history "user / history") | Returns a list of the recently played tracks | A list of object of type [track](https://developers.deezer.com/api/track "track")
[user / notifications](https://developers.deezer.com/api/user/notifications "user / notifications") | Use this method in post only, to add notifications in user feed | 
[user / permissions](https://developers.deezer.com/api/user/permissions "user / permissions") | Return the user's Permissions granted to the application | An object of type variable
[user / options](https://developers.deezer.com/api/user/options "user / options") | Alias of /options | An object of type [options](https://developers.deezer.com/api/options "options")
[user / personal_songs](https://developers.deezer.com/api/user/personal_songs "user / personal_songs") | Return a list of user's personnal song, represented by an array of Tracks | A list of object of type [track](https://developers.deezer.com/api/track "track")
[user / playlists](https://developers.deezer.com/api/user/playlists "user / playlists") | Return a list of user's public Playlist, represented by an array of Playlist object.Permission is needed to return private playlists | A list of object of type [playlist](https://developers.deezer.com/api/playlist "playlist")
[user / podcasts](https://developers.deezer.com/api/user/podcasts "user / podcasts") | Return a list of user's favorite podcasts. Represented by an array of Podcast object | A list of object of type [podcast](https://developers.deezer.com/api/podcast "podcast")
[user / radios](https://developers.deezer.com/api/user/radios "user / radios") | Return a list of user's favorite Radios, represented by an array of Radio object. | A list of object of type [radio](https://developers.deezer.com/api/radio "radio")
[user / recommendations](https://developers.deezer.com/api/user/recommendations "user / recommendations") | Use recommendations/albums, recommendations/artists, recommendations/playlists, recommendations/tracks, recommendations/radios or recommendations/releases. | 
[user / tracks](https://developers.deezer.com/api/user/tracks "user / tracks") | Return a list of user's favorite tracks. Represented by an array of Track object | A list of object of type [track](https://developers.deezer.com/api/track "track")
