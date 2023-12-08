# RfidCardDetectCallbacks


Callbacks are executed if rfid card is detected 

## Methods


### register


Add a new callback function :attr:`func`.   
Callback signature is   
.. py:function:: func(card_id: str, state: int) :noindex:   
:param card_id: Card ID :param state: See :class:`RfidCardDetectState` 

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
card_id |  | 
state |  | 




