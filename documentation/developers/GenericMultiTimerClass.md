# GenericMultiTimerClass


Interface for plugin / RPC accessibility for an event timer that performs an action n times every m seconds 

## Methods


### __init__


:param iterations: Number of times callee is called :param wait_seconds_per_iteration: Wait in seconds before each iteration :param callee: A builder class that gets instantiated once as callee(*args, iterations=iterations, **kwargs). Then with every time out iteration __call__(*args, iteration=iteration, **kwargs) is called. 'iteration' is the current iteration count in decreasing order! :param args: :param kwargs: 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
name |  | 
iterations |  | 
wait_seconds_per_iteration |  | 
callee |  | 
args |  | None
kwargs |  | None





### start


Start the timer (with default or new parameters) 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
iterations |  | None
wait_seconds_per_iteration |  | None





### get_state




#### Parameters
name | description | default
--- | --- | ---
self |  | 




