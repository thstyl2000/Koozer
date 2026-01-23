# Actions (request_method = delete)
Delete actions on the api 
Path | Description | needed Permissions | Required params
--- | --- | --- | ---
episode   
episode/{episode_id}/bookmark | Removes the bookmark on the episode |  manage_library   
playlist   
playlist/{playlist_id} | Delete the playlist |  delete_library   
playlist/{playlist_id}/tracks | Remove tracks from the playlist |  manage_librarydelete_library  | songs  | A comma separated list of track ids   
track   
track/{track_id} | Delete a personal track |  delete_library   
user   
user/{user_id}/albums | Remove an album from the user's library |  manage_librarydelete_library  | album_id  | The id of the album   
user/{user_id}/artists | Remove an artist from the user's favorites |  manage_librarydelete_library  | artist_id  | The id of the artist   
user/{user_id}/followings | Unfollow user |  manage_community  | user_id  | The user id to unfollow   
user/{user_id}/playlists | Remove a playlist from the user's favorites |  manage_librarydelete_library  | playlist_id  | The id of the playlist   
user/{user_id}/podcasts | Remove a podcast from the user's favorites |  manage_librarydelete_library  | podcast_id  | The id of the podcast   
user/{user_id}/radios | Remove a radio from the user's favorites |  manage_librarydelete_library  | radio_id  | The id of the radio   
user/{user_id}/tracks | Remove a track from the user's favorites |  manage_librarydelete_library  | track_id  | The id of the track
