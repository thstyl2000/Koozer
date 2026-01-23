# Actions (request_method = post)
Post actions on the api 
Path | Description | needed Permissions | Required params
--- | --- | --- | ---
episode   
episode/{episode_id}/bookmark | Sets a bookmark on the episode |  manage_library  | offset  | The offset where the bookmark is set, must be between 0 and 100   
playlist   
playlist/{playlist_id} | Update the playlist  
playlist/{playlist_id}/seen | Mark the playlist as seen |  basic_access   
playlist/{playlist_id}/tracks | Add a track to the playlist |  manage_library  | songs  | A comma separated list of track ids   
playlist/{playlist_id}/tracks | Order tracks in the playlist |  manage_library  | order  | A comma separated list of track ids   
track   
track/{track_id} | Update a personal track |  manage_library   
user   
user/{user_id}/albums | Add album(s) to the user's library |  manage_library   
user/{user_id}/artists | Add artist(s) to the user's favorites |  manage_library   
user/{user_id}/followings | Follow user |  manage_community  | user_id  | The user id to follow   
user/{user_id}/notifications | message  | Notification to add in the user feed   
user/{user_id}/playlists | Create a playlist |  manage_library  | title  | The title of the new playlist   
user/{user_id}/playlists | Add playlist(s) to the user's favorites |  manage_library   
user/{user_id}/podcasts | Add a podcast to the user's favorites |  manage_library  | podcast_id  | The id of the podcast   
user/{user_id}/radios | Add a radio to the user's favorites |  manage_library  | radio_id  | The id of the radio   
user/{user_id}/tracks | Add track(s) to the user's favorites |  manage_library
