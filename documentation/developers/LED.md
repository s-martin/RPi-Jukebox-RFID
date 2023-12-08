# LED


A binary LED   
:param pin: The GPIO pin which the LED is connected   
:param active_high: If :data:`true` the output pin will have a high logic level when the device is turned on.   
:param pin_factory: The GPIOZero pin factory. This parameter cannot be set through the configuration file   
:type name: str :param name: The name of the button for use in error messages. This parameter cannot be set explicitly through the configuration file 

## Methods


### __init__




#### Parameters
name | description | default
--- | --- | ---
self |  | 
pin |  | None
active_high |  | True
initial_value |  | False
pin_factory |  | None
name |  | None





### flash


Exactly like :func:`blink` but restores the original state after flashing the device   
:param float on_time: Number of seconds on. Defaults to 1 second.   
:param float off_time: Number of seconds off. Defaults to 1 second.   
:param n: Number of times to blink; :data:`None` means forever.   
:param bool background: If :data:`True` (the default), start a background thread to continue blinking and return immediately. If :data:`False`, only return when the blink is finished   
:param ignored_kwargs: Ignore all other keywords so this function can be called with identical parameters also for all other output devices 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
on_time |  | 1
off_time |  | 1
n |  | 1





### _flash_device




#### Parameters
name | description | default
--- | --- | ---
self |  | 




