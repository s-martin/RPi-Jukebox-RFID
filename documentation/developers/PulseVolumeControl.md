# PulseVolumeControl


Volume control manager for PulseAudio   
When accessing the pulse library, it needs to be put into a special state. Which is ensured by the context manager   
.. code-block: python   
with pulse_monitor as pulse ...   
  
All private functions starting with `_function_name` assume that this is ensured by the calling function. All user functions acquire proper context! 

## Methods


### __init__




#### Parameters
name | description | default
--- | --- | ---
self |  | 
sink_list |  | 





### _set_volume




#### Parameters
name | description | default
--- | --- | ---
self |  | 
pulse_inst |  | 
volume |  | 
sink_name |  | None





### _get_volume_and_mute




#### Parameters
name | description | default
--- | --- | ---
self |  | 
pulse_inst |  | 
sink_name |  | None





### _publish_volume




#### Parameters
name | description | default
--- | --- | ---
self |  | 
pulse_inst |  | 





### _get_outputs




#### Parameters
name | description | default
--- | --- | ---
self |  | 
pulse_inst |  | 





### _publish_outputs




#### Parameters
name | description | default
--- | --- | ---
self |  | 
pulse_inst |  | 





### _set_output




#### Parameters
name | description | default
--- | --- | ---
self |  | 
pulse_inst |  | 
sink_index |  | 





### _toggle_output




#### Parameters
name | description | default
--- | --- | ---
self |  | 
pulse_inst |  | 





### toggle_output


Toggle the audio output sink 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### get_outputs


Get current output and list of outputs 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### publish_volume


Publish (volume, mute) 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### publish_outputs


Publish current output and list of outputs 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### set_volume


Set the volume (0-100) for the currently active output 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
volume |  | 





### get_volume


Get the volume 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### change_volume


Increase/decrease the volume by step for the currently active output 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
step |  | 





### get_mute


Return mute status for the currently active output 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### mute


Set mute status for the currently active output 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
mute |  | True





### set_output


Set the active output (sink_index = 0: primary, 1: secondary) 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
sink_index |  | 





### set_soft_max_volume


Limit the maximum volume to max_volume for the currently active output 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
max_volume |  | 





### get_soft_max_volume


Return the maximum volume limit for the currently active output 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### card_list


Return the list of present sound card 

#### Parameters
name | description | default
--- | --- | ---
self |  | 




