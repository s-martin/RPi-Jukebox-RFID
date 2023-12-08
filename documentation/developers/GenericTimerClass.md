# GenericTimerClass


Interface for plugin / RPC accessibility for a single event timer 

## Methods


### __init__


:param wait_seconds: The time in seconds to wait before calling function :param function: The function to call with args and kwargs. :param args: Parameters for function call :param kwargs: Parameters for function call 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
name |  | 
wait_seconds |  | 
function |  | 
args |  | None
kwargs |  | None





### start


Start the timer (with default or new parameters) 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
wait_seconds |  | None





### cancel


Cancel the timer 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### toggle


Toggle the activation of the timer 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### trigger


Trigger the next target execution before the time is up 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### is_alive


Check if timer is active 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### get_timeout


Get the configured time-out   
:return: The total wait time. (Not the remaining wait time!) 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### set_timeout


Set a new time-out in seconds. Re-starts the timer if already running! 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
wait_seconds |  | 





### publish


Publish the current state and config 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### get_state


Get the current state and config as dictionary 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### _publish_core


Internal publish function with override for enabled   
Enable override is required as this is called from inside the timer when it finishes This means the timer is still running, but it is the last thing it does. Otherwise it is not possible to detect the timer change at the end 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
enabled |  | None




