# SyncRfidcards


Control class for sync RFID cards functionality 

## Methods


### __init__




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### __exit__




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### _rfid_callback




#### Parameters
name | description | default
--- | --- | ---
self |  | 
card_id |  | 
state |  | 





### _play_card_callback




#### Parameters
name | description | default
--- | --- | ---
self |  | 
folder |  | 
state |  | 





### sync_change_on_rfid_scan


Change activation of 'on_rfid_scan_enabled'   
:param option: Must be one of 'enable', 'disable', 'toggle' 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
option |  | "toggle"





### sync_all


Sync all audiofolder and cardids from the remote server. Removes local entries not existing at the remote server. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### sync_card_database


Sync the card database from the remote server, if existing. If card_id is provided only this entry is updated.   
:param card_id: The cardid to update 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
card_id |  | 





### sync_folder


Sync the folder from the remote server, if existing   
:param folder: Folder path relative to music library path 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
folder |  | 





### _is_sync_enabled




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### _is_sync_enabled_on_rfid_scan




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### _sync_card_database




#### Parameters
name | description | default
--- | --- | ---
self |  | 
card_id |  | None





### _sync_folder




#### Parameters
name | description | default
--- | --- | ---
self |  | 
folder |  | 





### _sync_paths




#### Parameters
name | description | default
--- | --- | ---
self |  | 
src_path |  | 
dst_path |  | 





### _is_server_reachable




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### _is_file_remote




#### Parameters
name | description | default
--- | --- | ---
self |  | 
path |  | 





### _is_dir_remote




#### Parameters
name | description | default
--- | --- | ---
self |  | 
path |  | 




