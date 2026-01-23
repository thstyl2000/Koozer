# Search
  * [SEARCH METHODS](https://developers.deezer.com/api/search#tab_connections)


Search tracks 
## Examples
[https://api.deezer.com/search?q=eminem](https://developers.deezer.com/api/explorer?url=search%3Fq%3Deminem "https://api.deezer.com/search?q=eminem")
## Optionnal Parameters (for all methods)
Name | Description
--- | ---
strict | Disable the fuzzy mode (?strict=on)
order | Possible values : RANKING, TRACK_ASC, TRACK_DESC, ARTIST_ASC, ARTIST_DESC, ALBUM_ASC, ALBUM_DESC, RATING_ASC, RATING_DESC, DURATION_ASC, DURATION_DESC
## Fields
Name | Description | Type
--- | --- | ---
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
artist | [artist](https://developers.deezer.com/api/artist "artist") object containing : id, name, link, picture, picture_small, picture_medium, picture_big, picture_xl | object
album | [album](https://developers.deezer.com/api/album "album") object containing : id, title, cover, cover_small, cover_medium, cover_big, cover_xl | object
Advanced search
Deezer provides a hidden feature that could help you to find artists, albums or a tracks. This feature is called Advanced Search. The only thing you have to do is to specify the need that you expect.
Here is the list of what you can specify: 
Name | Description | Type | Example
--- | --- | --- | ---
artist | The artist name | string | [https://api.deezer.com/search?q=artist:"aloe blacc"](https://developers.deezer.com/api/explorer?url=search%3Fq=artist:"aloe%20blacc" "https://developers.deezer.com/api/explorer?url=search%3Fq=artist:"aloe%20blacc"")
album | The album's title | string | [https://api.deezer.com/search?q=album:"good things"](https://developers.deezer.com/api/explorer?url=search%3Fq=album:"good%20things" "https://developers.deezer.com/api/explorer?url=search%3Fq=album:"good%20things"")
track | The track's title | string | [https://api.deezer.com/search?q=track:"i need a dollar"](https://developers.deezer.com/api/explorer?url=search%3Fq=track:"i%20need%20a%20dollar" "https://developers.deezer.com/api/explorer?url=search%3Fq=track:"i%20need%20a%20dollar"")
label | The label name | string | [https://api.deezer.com/search?q=label:"because music"](https://developers.deezer.com/api/explorer?url=search%3Fq=label:"because%20music" "https://developers.deezer.com/api/explorer?url=search%3Fq=label:"because%20music"")
dur_min | The track's minimum duration in seconds | int | [https://api.deezer.com/search?q=dur_min:300](https://developers.deezer.com/api/explorer?url=search%3Fq=dur_min:300 "https://developers.deezer.com/api/explorer?url=search%3Fq=dur_min:300")
dur_max | The track's maximum duration in seconds | int | [https://api.deezer.com/search?q=dur_max:500](https://developers.deezer.com/api/explorer?url=search%3Fq=dur_max:500 "https://developers.deezer.com/api/explorer?url=search%3Fq=dur_max:500")
bpm_min | The track's minimum bpm | int | [https://api.deezer.com/search?q=bpm_min:120](https://developers.deezer.com/api/explorer?url=search%3Fq=bpm_min:120 "https://developers.deezer.com/api/explorer?url=search%3Fq=bpm_min:120")
bpm_max | The track's maximum bpm | int | [https://api.deezer.com/search?q=bpm_max:200](https://developers.deezer.com/api/explorer?url=search%3Fq=bpm_max:200 "https://developers.deezer.com/api/explorer?url=search%3Fq=bpm_max:200")
You can also mixed your search, by adding a space between each field, to be more specific.
## Examples
[https://api.deezer.com/search?q=artist:"aloe blacc" track:"i need a dollar"](https://developers.deezer.com/api/explorer?url=search%3Fq=artist:"aloe%20blacc"%20track:"i%20need%20a%20dollar" "https://developers.deezer.com/api/explorer?url=search%3Fq=artist:"aloe%20blacc"%20track:"i%20need%20a%20dollar"")
[https://api.deezer.com/search?q=bpm_min:120 dur_min:300](https://developers.deezer.com/api/explorer?url=search%3Fq=bpm_min:120%20dur_min:300 "https://developers.deezer.com/api/explorer?url=search%3Fq=bpm_min:120%20dur_min:300")
## Connections
Name | Description | Returns
--- | --- | ---
[search / album](https://developers.deezer.com/api/search/album "search / album") | Search albums | A list of object of type [album](https://developers.deezer.com/api/album "album")
[search / artist](https://developers.deezer.com/api/search/artist "search / artist") | Search artists | A list of object of type [artist](https://developers.deezer.com/api/artist "artist")
[search / history](https://developers.deezer.com/api/search/history "search / history") | Get user search history | A list of object of type [track](https://developers.deezer.com/api/track "track")A list of object of type [album](https://developers.deezer.com/api/album "album")A list of object of type [artist](https://developers.deezer.com/api/artist "artist")A list of object of type [playlist](https://developers.deezer.com/api/playlist "playlist")A list of object of type [podcast](https://developers.deezer.com/api/podcast "podcast")A list of object of type [radio](https://developers.deezer.com/api/radio "radio")
[search / playlist](https://developers.deezer.com/api/search/playlist "search / playlist") | Search playlists | A list of object of type [playlist](https://developers.deezer.com/api/playlist "playlist")
[search / podcast](https://developers.deezer.com/api/search/podcast "search / podcast") | Search podcasts | A list of object of type [podcast](https://developers.deezer.com/api/podcast "podcast")
[search / radio](https://developers.deezer.com/api/search/radio "search / radio") | Search radio | A list of object of type [radio](https://developers.deezer.com/api/radio "radio")
[search / track](https://developers.deezer.com/api/search/track "search / track") | Search tracks | A list of object of type [track](https://developers.deezer.com/api/track "track")
[search / user](https://developers.deezer.com/api/search/user "search / user") | Search users | A list of object of type [user](https://developers.deezer.com/api/user "user")
