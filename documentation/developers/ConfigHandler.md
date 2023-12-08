# ConfigHandler


The configuration handler class   
Don't instantiate directly. Always use :func:`get_handler`!   
**Threads:**   
All threads can read and write to the configuration data. **Proper thread-safeness must be ensured** by the the thread modifying the data by acquiring the lock Easiest and best way is to use the context handler::   
with cfg: cfg['key'] = 66 cfg.setndefault('hello', value='world')   
For a single function call, this is done implicitly. In this case, there is no need to explicitly acquire the lock.   
Alternatively, you can lock and release manually by using :func:`acquire` and :func:`release` But be very sure to release the lock even in cases of errors an exceptions! Else we have a deadlock.   
Reading may be done without acquiring a lock. But be aware that when reading multiple values without locking, another thread may intervene and modify some values in between! So, locking is still recommended. 

## Methods


### __init__




#### Parameters
name | description | default
--- | --- | ---
self |  | 
name |  | 





### acquire




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### release




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### loaded_from


Property to store filename from which the config was loaded 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### loaded_from




#### Parameters
name | description | default
--- | --- | ---
self |  | 
filename |  | 





### __enter__




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### __exit__




#### Parameters
name | description | default
--- | --- | ---
self |  | 
exc_type |  | 
exc_val |  | 
exc_tb |  | 





### __getitem__




#### Parameters
name | description | default
--- | --- | ---
self |  | 
key |  | 





### __setitem__




#### Parameters
name | description | default
--- | --- | ---
self |  | 
key |  | 
value |  | 





### __delitem__




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### get


Enforce keyword on default to avoid accidental misuse when actually getn is wanted 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
key |  | 





### setdefault


Enforce keyword on default to avoid accidental misuse when actually setndefault is wanted 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
key |  | 





### getn


Get the value at arbitrary hierarchy depth. Return ``default`` if key not present   
The *default* value is returned no matter at which hierarchy level the path aborts. A hierarchy is considered as any type with a :func:`get` method. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### setn


Set the ``key: value`` pair at arbitrary hierarchy depth   
All non-existing hierarchy levels are created.   
:param keys: Key hierarchy path through the nested levels :param value: The value to set :param hierarchy_type: The type for new hierarchy levels. If *None*, the top-level type is used 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### setndefault


Set the ``key: value`` pair at arbitrary hierarchy depth unless the key already exists   
All non-existing hierarchy levels are created.   
:param keys: Key hierarchy path through the nested levels :param value: The default value to set :param hierarchy_type: The type for new hierarchy levels. If *None*, the top-level type is used :return: The actual value or or the default value if key does not exit 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### __str__




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### __contains__




#### Parameters
name | description | default
--- | --- | ---
self |  | 
item |  | 





### __iter__




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### __len__




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### items




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### keys




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### values




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### config_dict


Initialize configuration data from dict-like data structure   
:param data: configuration data 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
data |  | 





### is_modified


Check if the data has changed since the last load/store   
.. note: This relies on the *__str__* representation of the underlying data structure In case of ruamel, this ignores comments and only looks at the data 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### clear_modified


Sets the current state as new baseline, clearing the is_modified state 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### save


Save config back to the file it was loaded from   
If you want to save to a different file, use :func:`write_yaml`. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
only_if_changed |  | False





### load


Load YAML config file into memory 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
filename |  | 




