# JukeBox




## Methods


### __init__




#### Parameters
name | description | default
--- | --- | ---
self |  | 
configuration_file |  | 
write_artifacts |  | 





### start_time




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### git_state




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### signal_handler


Signal handler for orderly shutdown   
On first Ctrl-C (or SIGTERM) orderly shutdown procedure is embarked upon. It gets allocated a time-out! On third Ctrl-C (or SIGTERM), this is interrupted and there will be a hard exit! 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
esignal |  | 
frame |  | 





### exit_gracefully




#### Parameters
name | description | default
--- | --- | ---
self |  | 
esignal |  | 
timeout |  | 





### run




#### Parameters
name | description | default
--- | --- | ---
self |  | 




