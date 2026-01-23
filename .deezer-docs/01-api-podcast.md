# Podcast
  * [PODCAST METHODS](https://developers.deezer.com/api/podcast#tab_connections)


A podcast object 
## Examples
[https://api.deezer.com/podcast/2026](https://developers.deezer.com/api/explorer?url=podcast/2026 "https://api.deezer.com/podcast/2026")[https://api.deezer.com/podcast/2026](https://developers.deezer.com/api/explorer?url=podcast/2026 "https://api.deezer.com/podcast/2026")
## Fields
Name | Description | Type
--- | --- | ---
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
## Related actions
You may as well perform actions related to 'podcast' through the following methods :
### [user / podcasts](https://developers.deezer.com/api/user/podcasts "user / podcasts")
request_method | Needed Permissions | Description | Required params | Param description | Type
--- | --- | --- | --- | --- | ---
POST | manage_library | Add a podcast to the user's favorites | podcast_id | The id of the podcast | int
DELETE | manage_librarydelete_library | Remove a podcast from the user's favorites | podcast_id | The id of the podcast | int
## Connections
Name | Description | Returns
--- | --- | ---
[podcast / episodes](https://developers.deezer.com/api/podcast/episodes "podcast / episodes") | Returns the list of episodes about the podcast | A list of object of type [episode](https://developers.deezer.com/api/episode "episode")
