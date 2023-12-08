# TwinButton


A two-button device which can run up to six different actions, a.k.a the six function beast.   
Per user press "input" of the TwinButton, only a single callback is executed (but this callback may be executed several times). The shortest possible time is used to ensure a unique identification to an action can be made. For example a short press can only be identified, when a button is released before :attr:`hold_time`, i.e. not directly on button press. But a long press can be identified as soon as :attr:`hold_time` is reached and there is no need to wait for the release event. Furthermore, if there is a long hold, only the long hold action is executed - the short press action is not run in this case!   
It is not necessary to configure all actions.   
:param pull_up: See `Button`_   
:param active_state: See `Button`_   
:param bounce_time: See `Button`_   
:param hold_time: The time in seconds to differentiate if it is a short or long press. If the button is released before this time, it is a short press. As soon as the button is held for :attr:`hold_time` it is a long press and the short press action is ignored.   
:param hold_repeat: If :data:`True` repeat the long press action every :attr:`hold_time` seconds after first long press action. A long dual press is never repeated independent of this setting   
:param pin_factory: See `Button`_   
:param name: See `Button`_ 

## Methods


### __init__




#### Parameters
name | description | default
--- | --- | ---
self |  | 
a |  | 
b |  | 





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





### close


Close the device and release the pins 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### _change_state




#### Parameters
name | description | default
--- | --- | ---
self |  | 
edge_a |  | 0
edge_b |  | 0
hold_a |  | 0
hold_b |  | 0





### _fire_press_a




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### _fire_press_b




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### _fire_press_ab




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### _fire_hold_ab




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### _fire_hold_a




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### _fire_hold_b




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### value


2 bit integer indicating if and which button is currently pressed. Button A is the LSB. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### is_active


:data:`True` if one or both buttons are currently pressed 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### hold_repeat




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### hold_time




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




