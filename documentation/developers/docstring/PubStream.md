# PubStream


" Stream handler wrapper around the publisher for logging.StreamHandler   
Allows logging to send all log information (based on logging configuration) to the Publisher.   
ATTENTION: This can lead to recursions!   
Recursions come up when (a) Publish.send / PublishServer.send also emits logs, which cause a another send, which emits a log, which causes a send, ..... (b) Publisher initialization emits logs, which need a Publisher instance to send logs   
IMPORTANT: To avoid endless recursions: The creation of a Publisher MUST NOT generate any log messages! Nor any of the functions in the send-function stack! 

## Methods


### __init__




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### flush




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### write




#### Parameters
name | description | default
--- | --- | ---
self |  | 
msg |  | 




