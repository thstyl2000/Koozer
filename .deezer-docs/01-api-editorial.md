# Editorial
  * [EDITORIAL METHODS](https://developers.deezer.com/api/editorial#tab_connections)


An editorial object 
## Examples
[https://api.deezer.com/editorial](https://developers.deezer.com/api/explorer?url=editorial "https://api.deezer.com/editorial")[https://api.deezer.com/editorial/0](https://developers.deezer.com/api/explorer?url=editorial/0 "https://api.deezer.com/editorial/0")
## Fields
Name | Description | Type
--- | --- | ---
id | The editorial's Deezer id | int
name | The editorial's name | string
picture | The url of the editorial picture. | url
picture_small | The url of the editorial picture in size small. | url
picture_medium | The url of the editorial picture in size medium. | url
picture_big | The url of the editorial picture in size big. | url
picture_xl | The url of the editorial picture in size xl. | url
## Connections
Name | Description | Returns
--- | --- | ---
[editorial / selection](https://developers.deezer.com/api/editorial/selection "editorial / selection") | Return a list of albums selected every week by the Deezer Team. | A list of object of type [album](https://developers.deezer.com/api/album "album")
[editorial / charts](https://developers.deezer.com/api/editorial/charts "editorial / charts") | This method returns four lists : Top track, Top album, Top artist and Top playlist. | A list of object of type [track](https://developers.deezer.com/api/track "track")A list of object of type [album](https://developers.deezer.com/api/album "album")A list of object of type [artist](https://developers.deezer.com/api/artist "artist")A list of object of type [playlist](https://developers.deezer.com/api/playlist "playlist")
[editorial / releases](https://developers.deezer.com/api/editorial/releases "editorial / releases") | This method returns the new releases per genre for the current country | A list of object of type [album](https://developers.deezer.com/api/album "album")
