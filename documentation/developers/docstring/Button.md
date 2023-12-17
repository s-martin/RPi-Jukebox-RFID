# Button


A basic Button that runs a single actions on button press   
:type pull_up: bool :param pull_up: If :data:`True`, the device uses an internal pull-up resistor to set the GPIO pin “high” by default. If :data:`False` the internal pull-down resistor is used. If :data:`None`, the pin will be floating and an external resistor must be used and the :attr:`active_state` must be set.   
:type active_state: bool or None :param active_state: If :data:`True`, when the hardware pin state is ``HIGH``, the software pin is ``HIGH``. If :data:`False`, the input polarity is reversed: when the hardware pin state is ``HIGH``, the software pin state is ``LOW``. Use this parameter to set the active state of the underlying pin when configuring it as not pulled (when *pull_up* is :data:`None`). When *pull_up* is :data:`True` or :data:`False`, the active state is automatically set to the proper value.   
:type bounce_time: float or None :param bounce_time: Specifies the length of time (in seconds) that the component will ignore changes in state after an initial change. This defaults to :data:`None` which indicates that no bounce compensation will be performed.   
:type hold_repeat: bool :param hold_repeat: If :data:`True` repeat the :attr:`on_press` every :attr:`hold_time` seconds. Else action is run only once independent of the length of time the button is pressed for.   
:type hold_time: float :param hold_time: Time in seconds to wait between invocations of :attr:`on_press`.   
:param pin_factory: The GPIOZero pin factory. This parameter cannot be set through the configuration file   
:type name: str :param name: The name of the button for use in error messages. This parameter cannot be set explicitly through the configuration file   
.. copied from GPIOZero's documentation: active_state, bounce_time .. Copyright Ben Nuttall / SPDX-License-Identifier: BSD-3-Clause 

## Methods


### __init__




#### Parameters
name | description | default
--- | --- | ---
self |  | 
pin |  | None





### on_press


The function to run when the device has been pressed 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### on_press




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




