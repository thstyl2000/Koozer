# Genre
  * [GENRE METHODS](https://developers.deezer.com/api/genre#tab_connections)


A genre object 
## Examples
[https://api.deezer.com/genre/0](https://developers.deezer.com/api/explorer?url=genre/0 "https://api.deezer.com/genre/0")[https://api.deezer.com/genre/0](https://developers.deezer.com/api/explorer?url=genre/0 "https://api.deezer.com/genre/0")
## Fields
Name | Description | Type
--- | --- | ---
id | The editorial's Deezer id | int
name | The editorial's name | string
picture | The url of the genre picture. Add 'size' parameter to the url to change size. Can be 'small', 'medium', 'big', 'xl' | url
picture_small | The url of the genre picture in size small. | url
picture_medium | The url of the genre picture in size medium. | url
picture_big | The url of the genre picture in size big. | url
picture_xl | The url of the genre picture in size xl. | url
## Connections
Name | Description | Returns
--- | --- | ---
[genre / artists](https://developers.deezer.com/api/genre/artists "genre / artists") | Returns all artists for a genre | An object of type [artist](https://developers.deezer.com/api/artist "artist")
[genre / podcasts](https://developers.deezer.com/api/genre/podcasts "genre / podcasts") | Returns all podcasts for a genre | A list of object of type [podcast](https://developers.deezer.com/api/podcast "podcast")
[genre / radios](https://developers.deezer.com/api/genre/radios "genre / radios") | Returns all radios for a genre | An object of type [radio](https://developers.deezer.com/api/radio "radio")
