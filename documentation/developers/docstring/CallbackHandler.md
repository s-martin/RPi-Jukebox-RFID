# CallbackHandler


Generic Callback Handler to collect callbacks functions through :func:`register` and execute them with :func:`run_callbacks`   
A lock is used to sequence registering of new functions and running callbacks.   
:param name: A name of this handler for usage in log messages :param logger: The logger instance to use for logging :param context: A custom context handler to use as lock. If none, a local :class:`threading.Lock()` will be created 

## Methods


### __init__




#### Parameters
name | description | default
--- | --- | ---
self |  | 
name |  | 
logger |  | 
context |  | None





### register


Register a new function to be executed when the callback event happens   
:param func: The function to register. If set to :data:`None`, this register request is silently ignored. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
func |  | 





### _run_callbacks


Run all callbacks w/o acquiring the context first.   
Comes in useful in scenarios where the calling function has already acquired the context. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### run_callbacks


Run all registered callbacks.   
*ALL* exceptions from callback functions will be caught and logged only. Exceptions are not raised upwards! 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### has_callbacks


:data:`True` if there are any registered callbacks. Read-only property 

#### Parameters
name | description | default
--- | --- | ---
self |  | 




