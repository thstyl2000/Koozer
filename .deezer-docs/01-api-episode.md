# Episode
  * [EPISODE METHODS](https://developers.deezer.com/api/episode#tab_connections)


An episode object 
## Examples
[https://api.deezer.com/episode/56468](https://developers.deezer.com/api/explorer?url=episode/56468 "https://api.deezer.com/episode/56468")
## Fields
Name | Description | Type
--- | --- | ---
id | The episode's Deezer id | int
title | The episode's title | string
description | The episode's description | string
available | If the episode is available or not | boolean
release_date | The episode's release date | date
duration | The episode's duration (seconds) | int
link | The url of the episode on Deezer | url
share | The share link of the episode on Deezer | url
picture | The url of the episode's cover. | url
picture_small | The url of the episode's cover in size small. | url
picture_medium | The url of the episode's cover in size medium. | url
picture_big | The url of the episode's cover in size big. | url
picture_xl | The url of the episode's cover in size xl. | url
track_token | The track token for media service | string
podcast | [podcast](https://developers.deezer.com/api/podcast "podcast") object containing : id, title, link, picture, picture_small, picture_medium, picture_big, picture_xl | object
## Connections
Name | Description | Returns
--- | --- | ---
[episode / bookmark](https://developers.deezer.com/api/episode/bookmark "episode / bookmark") | Handles a bookmark on the episode |
