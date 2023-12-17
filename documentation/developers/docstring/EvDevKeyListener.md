# EvDevKeyListener


Opens and event input device from ``/dev/inputs``, and runs callbacks upon the button presses. Input devices could be .e.g. Keyboard, Bluetooth audio buttons, USB buttons   
Runs as a separate thread. When device disconnects or disappears, thread exists. A new thread must be started when device re-connects.   
Assign callbacks to :attr:`EvDevKeyListener.button_callbacks` 

## Methods


### __init__


:param device_name_request: The device name to look for :param exact_name: If true, device_name must mach exactly, else a match is returned if device_name is a substring of the reported device name :param thread_name: Name of the listener thread 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
device_name_request |  | 
exact_name |  | 
thread_name |  | 





### stop




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### _connect




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### _listen




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### run




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### start


Start the tread and start listening 

#### Parameters
name | description | default
--- | --- | ---
self |  | 




