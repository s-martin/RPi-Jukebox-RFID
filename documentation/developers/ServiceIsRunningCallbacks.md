# ServiceIsRunningCallbacks


Callbacks are executed when   
* Jukebox app started * Jukebox shuts down   
This is intended to e.g. signal an LED to change state. This is integrated into this module because:   
* we need the GPIO to control a LED (it must be available when the status callback comes) * the plugin callback functions provide all the functionality to control the status of the LED * which means no need to adapt other modules 

## Methods


### register


Add a new callback function :attr:`func`.   
Callback signature is   
.. py:function:: func(status: int) :noindex:   
:param status: 1 if app started, 0 if app shuts down 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
func |  | 





### run_callbacks


:meta private: 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
status |  | 




