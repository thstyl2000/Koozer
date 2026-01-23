# Radio
  * [RADIO METHODS](https://developers.deezer.com/api/radio#tab_connections)


A radio object 
## Examples
[https://api.deezer.com/radio](https://developers.deezer.com/api/explorer?url=radio "https://api.deezer.com/radio")[https://api.deezer.com/radio/6](https://developers.deezer.com/api/explorer?url=radio/6 "https://api.deezer.com/radio/6")
## Fields
Name | Description | Type
--- | --- | ---
id | The radio deezer ID | int
title | The radio title | string
description | The radio title | string
share | The share link of the radio on Deezer | url
picture | The url of the radio picture. Add 'size' parameter to the url to change size. Can be 'small', 'medium', 'big', 'xl' | 
picture_small | The url of the radio picture in size small. | 
picture_medium | The url of the radio picture in size medium. | 
picture_big | The url of the radio picture in size big. | 
picture_xl | The url of the radio picture in size xl. | 
tracklist | API Link to the tracklist of this radio | url
md5_image | string | 
## Related actions
You may as well perform actions related to 'radio' through the following methods :
### [user / radios](https://developers.deezer.com/api/user/radios "user / radios")
request_method | Needed Permissions | Description | Required params | Param description | Type
--- | --- | --- | --- | --- | ---
POST | manage_library | Add a radio to the user's favorites | radio_id | The id of the radio | int
DELETE | manage_librarydelete_library | Remove a radio from the user's favorites | radio_id | The id of the radio | int
## Connections
Name | Description | Returns
--- | --- | ---
[radio / genres](https://developers.deezer.com/api/radio/genres "radio / genres") | Returns a list of radio splitted by genre | A list of object of type [radio](https://developers.deezer.com/api/radio "radio")
[radio / top](https://developers.deezer.com/api/radio/top "radio / top") | Return the top radios (default to 25 radios) | A list of object of type [radio](https://developers.deezer.com/api/radio "radio")
[radio / tracks](https://developers.deezer.com/api/radio/tracks "radio / tracks") | Get first 40 tracks in the radio | A list of object of type [track](https://developers.deezer.com/api/track "track")
[radio / lists](https://developers.deezer.com/api/radio/lists "radio / lists") | Returns a list of personal radio splitted by genre (as MIX in website) | A list of object of type [radio](https://developers.deezer.com/api/radio "radio")
