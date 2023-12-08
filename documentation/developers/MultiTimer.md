# MultiTimer


Call a function after a specified number of seconds, repeat that iteration times   
May be cancelled during any of the wait times. Function is called with keyword parameter 'iteration' (which decreases down to 0 for the last iteration)   
If iterations is negative, an endlessly repeating timer is created (which needs to be cancelled with cancel())   
Initiates start and publishing by calling self.publish_callback   
Note: Inspired by threading.Timer and generally using the same API 

## Methods


### __init__




#### Parameters
name | description | default
--- | --- | ---
self |  | 
interval |  | 
iterations |  | 
function |  | 
args |  | None
kwargs |  | None





### cancel


Stop the timer if it hasn't finished all iterations yet. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### trigger




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### run_endless




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### run_limited




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### run




#### Parameters
name | description | default
--- | --- | ---
self |  | 




