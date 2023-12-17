# LongPressButton


A Button that runs a single actions only when the button is pressed long enough   
:param pull_up: See `Button`_   
:param active_state: See `Button`_   
:param bounce_time: See `Button`_   
:param hold_repeat: If :data:`True` repeat the :attr:`on_press` every :attr:`hold_time` seconds. Else only action is run only once independent of the length of time the button is pressed for.   
:param hold_time: The minimum time, the button must be pressed be running :attr:`on_press` for the first time. Also the time in seconds to wait between invocations of :attr:`on_press`. 

## Methods


### __init__




#### Parameters
name | description | default
--- | --- | ---
self |  | 
pin |  | None





### on_press




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### on_press


The function to run when the device has been pressed for longer than :attr:`hold_time` 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
func |  | 





### hold_time




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### hold_repeat




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### set_rpc_actions




#### Parameters
name | description | default
--- | --- | ---
self |  | 
action_config |  | 




