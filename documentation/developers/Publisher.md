# Publisher


The publisher that provides the functional interface to the application   
.. note:: * An instance must not be shared across threads! * One instance per thread is enough 

## Methods


### __init__


:param check_thread_owner: Check if send() is always called from the correct thread. This is debug feature and is intended to expose the situation before it leads to real trouble. Leave it on! 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
check_thread_owner |  | True





### _send




#### Parameters
name | description | default
--- | --- | ---
self |  | 
topic |  | 
message |  | 
cmd |  | 





### send


Send out a message for topic 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
topic |  | 
payload |  | 





### revoke


Revoke a single topic element (not a topic tree!) 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
topic |  | 





### resend


Instructs the PublishServer to resend current status to all subscribers   
Not necessary to call after incremental updates or new subscriptions - that will happen automatically! 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
topic |  | None





### close_server


Instructs the PublishServer to close itself down 

#### Parameters
name | description | default
--- | --- | ---
self |  | 




