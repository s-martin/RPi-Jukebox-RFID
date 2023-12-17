# ReaderClass


The actual reader class that is used to read RFID cards.   
It will be instantiated once and then read_card() is called in an endless loop.   
It will be used in a  manner with Reader(reader_cfg_key) as reader: for card_id in reader: ... which ensures proper resource de-allocation. For this to work derive this class from ReaderBaseClass. All the required interfaces are implemented there.   
Put your code into these functions (see below for more information) - __init__ - read_card - cleanup - stop 

## Methods


### __init__


In the constructor, you will get the `reader_cfg_key` with which you can access the configuration data   
As you are dealing directly with potentially user-manipulated config information, it is advisable to do some sanity checks and give useful error messages. Even if you cannot recover gracefully, a good error message helps :-) 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
reader_cfg_key |  | 





### cleanup


The cleanup function: free and release all resources used by this card reader (if any).   
Put all your cleanup code here, e.g. if you are using the serial bus or GPIO pins. Will be called implicitly via the __exit__ function This function must exist! If there is nothing to do, just leave the pass statement in place below 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### stop


This function is called to tell the reader to exist it's reading function.   
This function is called before cleanup is called.   
.. note: This is usually called from a different thread than the reader's thread! And this is the reason for the two-step exit strategy. This function works across threads to indicate to the reader that is should stop attempt to read a card. Once called, the function read_card will not be called again. When the reader thread exits cleanup is called from the reader thread itself. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### read_card


Blocking or non-blocking function that waits for a new card to appear and return the card's UID as string   
This is were your main code goes :-) This function must return a string with the card id In case of error, it may return None or an empty string   
The function should break and return with an empty string, once stop() is called 

#### Parameters
name | description | default
--- | --- | ---
self |  | 




