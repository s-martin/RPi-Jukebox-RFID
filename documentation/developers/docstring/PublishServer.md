# PublishServer


The publish proxy server that collects and caches messages from all internal publishers and forwards them to the outside world   
Handles new subscriptions by sending out the entire cached state to **all** subscribers   
The code is structures using a `Reactor Pattern <https://zguide.zeromq.org/docs/chapter5/#Using-a-Reactor>`_ 

## Methods


### __init__




#### Parameters
name | description | default
--- | --- | ---
self |  | 
tcp_port |  | 
websocket_port |  | 





### run


Thread's activity 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### handle_message


Handle incoming messages 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
msg |  | 





### handle_subscription


Handle new subscribers 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
msg |  | 




