# PlayerMPD


Interface to MPD Music Player Daemon 

## Methods


### __init__




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### exit




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### connect




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### decode_2nd_swipe_option




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### mpd_retry_with_mutex


This method adds thread saftey for acceses to mpd via a mutex lock, it shall be used for each access to mpd to ensure thread safety In case of a communication error the connection will be reestablished and the pending command will be repeated 2 times   
I think this should be refactored to a decorator 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
mpd_cmd |  | 





### _mpd_status_poll


this method polls the status from mpd and stores the important inforamtion in the music_player_status, it will repeat itself in the intervall specified by self.mpd_status_poll_interval 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### get_player_type_and_version




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### update




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### update_wait




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### play




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### stop




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### pause


Enforce pause to state (1: pause, 0: resume)   
This is what you want as card removal action: pause the playback, so it can be resumed when card is placed on the reader again. What happens on re-placement depends on configured second swipe option 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
state |  | 1





### prev




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### next


Play next track in current playlist 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### seek




#### Parameters
name | description | default
--- | --- | ---
self |  | 
new_time |  | 





### shuffle




#### Parameters
name | description | default
--- | --- | ---
self |  | 
random |  | 





### rewind


Re-start current playlist from first track   
Note: Will not re-read folder config, but leave settings untouched 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### replay


Re-start playing the last-played folder   
Will reset settings to folder config 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### toggle


Toggle pause state, i.e. do a pause / resume depending on current state 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### replay_if_stopped


Re-start playing the last-played folder unless playlist is still playing   
.. note:: To me this seems much like the behaviour of play, but we keep it as it is specifically implemented in box 2.X 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### repeatmode




#### Parameters
name | description | default
--- | --- | ---
self |  | 
mode |  | 





### get_current_song




#### Parameters
name | description | default
--- | --- | ---
self |  | 
param |  | 





### map_filename_to_playlist_pos




#### Parameters
name | description | default
--- | --- | ---
self |  | 
filename |  | 





### remove




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### move




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### play_single




#### Parameters
name | description | default
--- | --- | ---
self |  | 
song_url |  | 





### resume




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### play_card


Main entry point for trigger music playing from RFID reader. Decodes second swipe options before playing folder content   
Checks for second (or multiple) trigger of the same folder and calls first swipe / second swipe action accordingly.   
:param folder: Folder path relative to music library path :param recursive: Add folder recursively 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
folder |  | 
recursive |  | False





### get_folder_content


Get the folder content as content list with meta-information. Depth is always 1.   
Call repeatedly to descend in hierarchy   
:param folder: Folder path relative to music library path 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
folder |  | 





### play_folder


Playback a music folder.   
Folder content is added to the playlist as described by :mod:`jukebox.playlistgenerator`. The playlist is cleared first.   
:param folder: Folder path relative to music library path :param recursive: Add folder recursively 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
folder |  | 
recursive |  | False





### play_album


Playback a album found in MPD database.   
All album songs are added to the playlist The playlist is cleared first.   
:param albumartist: Artist of the Album provided by MPD database :param album: Album name provided by MPD database 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
albumartist |  | 
album |  | 





### queue_load




#### Parameters
name | description | default
--- | --- | ---
self |  | 
folder |  | 





### playerstatus




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### playlistinfo




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### list_all_dirs




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### list_albums




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### list_song_by_artist_and_album




#### Parameters
name | description | default
--- | --- | ---
self |  | 
albumartist |  | 
album |  | 





### get_song_by_url




#### Parameters
name | description | default
--- | --- | ---
self |  | 
song_url |  | 





### get_volume


Get the current volume   
For volume control do not use directly, but use through the plugin 'volume', as the user may have configured a volume control manager other than MPD 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### set_volume


Set the volume   
For volume control do not use directly, but use through the plugin 'volume', as the user may have configured a volume control manager other than MPD 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
volume |  | 





### _db_wait_for_update




#### Parameters
name | description | default
--- | --- | ---
self |  | 
update_id |  | 





### _db_is_updating




#### Parameters
name | description | default
--- | --- | ---
self |  | 
update_id |  | 




