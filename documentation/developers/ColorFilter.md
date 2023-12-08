# ColorFilter


This filter adds colors to the logger   
It adds all colors from simplecolors by using the color name as new keyword, i.e. use %(colorname)c or {colorname} in the formatter string   
It also adds the keyword {levelnameColored} which is an auto-colored drop-in replacement for the levelname depending on severity.   
Don't forget to {reset} the color settings at the end of the string. 

## Methods


### __init__


:param enable: Enable the coloring :param color_levelname: Enable auto-coloring when using the levelname keyword 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
enable |  | True
color_levelname |  | True





### filter




#### Parameters
name | description | default
--- | --- | ---
self |  | 
record |  | 




