# PulseMonitor


A thread for monitoring and interacting with the Pulse Lib via pulsectrl   
Whenever we want to access pulsectl, we need to exit the event listen loop. This is handled by the context manager. It stops the event loop and returns the pulsectl instance to be used (it does no return the monitor thread itself!)   
The context manager also locks the module to ensure proper thread sequencing, as only a single thread may work with pulsectl at any time. Currently, an RLock is used, even if it may not be necessary 

## Methods


### __init__




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### toggle_on_connect


Returns :data:`True` if the sound card shall be changed when a new card connects/disconnects. Setting this property changes the behavior.   
.. note:: A new card is always assumed to be the secondary device from the audio configuration. At the moment there is no check it actually is the configured device. This means any new device connection will initiate the toggle. This, however, is no real issue as the RPi's audio system will be relatively stable once setup 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### toggle_on_connect


Toggle Doc 2 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
state |  | True





### __enter__




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### __exit__




#### Parameters
name | description | default
--- | --- | ---
self |  | 
exc_type |  | 
exc_val |  | 
exc_tb |  | 





### stop


Stop the pulse monitor thread 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### _get_event




#### Parameters
name | description | default
--- | --- | ---
self |  | 
event |  | 





### _handle_event




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### run


Starts the pulse monitor thread 

#### Parameters
name | description | default
--- | --- | ---
self |  | 




