# PlaylistCollector


Build a playlist from directory(s)   
This class is intended to be used with an absolute path to the music library::   
plc = PlaylistCollector('/home/chris/music') plc.parse('Traumfaenger') print(f"res = {plc}")   
But it can also be used with relative paths from current working directory::   
plc = PlaylistCollector('.') plc.parse('../../../../music/Traumfaenger') print(f"res = {plc}")   
The file ending exclusion list :attr:`PlaylistCollector._exclude_endings` is a class variable for performance reasons. If changed it will affect all instances. For modifications always call :func:`set_exclusion_endings`. 

## Methods


### __init__


Initialize the playlist generator with music_library_base_path   
:param music_library_base_path: Base path the the music library. This is used to locate the file in the disk but is omitted when generating the playlist entries. I.e. all files in the playlist are relative to this base dir 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
music_library_base_path |  | "/"





### _is_valid


Check if filename is valid 

#### Parameters
name | description | default
--- | --- | ---
cls |  | 
direntry |  | 





### set_exclusion_endings


Set the class-wide file ending exclusion list   
See :attr:`PlaylistCollector._exclude_endings` 

#### Parameters
name | description | default
--- | --- | ---
cls |  | 
endings |  | 





### _get_directory_content




#### Parameters
name | description | default
--- | --- | ---
self |  | 
path |  | "."





### get_directory_content


Parse the folder ``path`` and create a content list. Depth is always the current level   
:param path: Path to folder **relative** to ``music_library_base_path`` :return: [ { type: 'directory', name: 'Simone', path: '/some/path/to/Simone' }, {...} ] where type is one of :attr:`TYPE_DECODE` 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
path |  | "."





### _parse_nonrecusive




#### Parameters
name | description | default
--- | --- | ---
self |  | 
path |  | "."





### _parse_recursive




#### Parameters
name | description | default
--- | --- | ---
self |  | 
path |  | "."





### parse


Parse the folder ``path`` and create a playlist from it's content   
:param path: Path to folder **relative** to ``music_library_base_path`` :param recursive: Parse folder recursivley, or stay in top-level folder 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
path |  | "."
recursive |  | False





### __iter__




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### __str__




#### Parameters
name | description | default
--- | --- | ---
self |  | 




