# VolumeToRGB


Converts linear volume level to an RGB color value running through the color spectrum   
:param max_input: Maximum input value of linear input data :param offset: Offset in degrees in the color circle. Color circle traverses blue (0), cyan(60), green (120), yellow(180), red (240), magenta (340) :param section: The section of the full color circle to use in degrees   
Map input :data:`0...100` to color range :data:`green...magenta` and get the color for level 50   
.. code-block:: python   
conv = VolumeToRGB(100, offset=120, section=180) (r, g, b) = conv(50)   
The three components of an RGB LEDs do not have the same luminosity. Weight factors are used to get a balanced color output 

## Methods


### __init__




#### Parameters
name | description | default
--- | --- | ---
self |  | 
max_input |  | 
offset |  | 0
section |  | 360





### __call__


Perform conversion for single volume level   
:return: Tuple(red, green, blue) :meta public: 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
volume |  | 





### luminize


Apply the color weight factors to the input color values 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
r |  | 
g |  | 
b |  | 




