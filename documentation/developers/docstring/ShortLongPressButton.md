# ShortLongPressButton


A single button that runs two different actions depending if the button is pressed for a short or long time.   
The shortest possible time is used to ensure a unique identification to an action can be made. For example a short press can only be identified, when a button is released before :attr:`hold_time`, i.e. not directly on button press. But a long press can be identified as soon as :attr:`hold_time` is reached and there is no need to wait for the release event. Furthermore, if there is a long hold, only the long hold action is executed - the short press action is not run in this case!   
:param pull_up: See `Button`_   
:param active_state: See `Button`_   
:param bounce_time: See `Button`_   
:param hold_time: The time in seconds to differentiate if it is a short or long press. If the button is released before this time, it is a short press. As soon as the button is held for :attr:`hold_time` it is a long press and the short press action is ignored   
:param hold_repeat: If :data:`True` repeat the long press action every :attr:`hold_time` seconds after first long press action   
:param pin_factory: See `Button`_   
:param name: See `Button`_ 

## Methods


### __init__




#### Parameters
name | description | default
--- | --- | ---
self |  | 
pin |  | None





### _on_activation




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### _on_long_activation




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### _on_deactivation




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### on_short_press




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### on_short_press




#### Parameters
name | description | default
--- | --- | ---
self |  | 
func |  | 





### on_long_press




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### on_long_press




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




