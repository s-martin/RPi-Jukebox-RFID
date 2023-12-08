# ButtonBase


Common stuff for single button devices   
:meta private: 

## Methods


### __init__




#### Parameters
name | description | default
--- | --- | ---
self |  | 
pin |  | None
pull_up |  | True
active_state |  | None
bounce_time |  | None
pin_factory |  | None





### value


Returns 1 if the button is currently pressed, and 0 if it is not. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### pin


Returns the underlying pin class from GPIOZero. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### pull_up


If :data:`True`, the device uses an internal pull-up resistor to set the GPIO pin “high” by default. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### close


Close the device and release the pin 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





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




