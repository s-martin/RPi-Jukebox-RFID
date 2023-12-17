# RotaryEncoder


A rotary encoder to run one of two actions depending on the rotation direction.   
:param bounce_time: See `Button`_   
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





### pin_a


Returns the underlying pin A 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### pin_b


Returns the underlying pin B 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### on_rotate_clockwise


The function to run when the encoder is rotated clockwise 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### on_rotate_clockwise




#### Parameters
name | description | default
--- | --- | ---
self |  | 
func |  | 





### on_rotate_counter_clockwise


The function to run when the encoder is rotated counter clockwise 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### on_rotate_counter_clockwise




#### Parameters
name | description | default
--- | --- | ---
self |  | 
func |  | 





### set_rpc_actions




#### Parameters
name | description | default
--- | --- | ---
self |  | 
action_config |  | 





### close


Close the device and release the pin 

#### Parameters
name | description | default
--- | --- | ---
self |  | 




