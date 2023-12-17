# battmon_ads1015


Battery Monitor based on a ADS1015   
CAUTION - WARNING ======================================================================== Lithium and other batteries are dangerous and must be treated with care. Rechargeable Lithium Ion batteries are potentially hazardous and can present a serious FIRE HAZARD if damaged, defective or improperly used. Do not use this circuit to a lithium ion battery without expertise and training in handling and use of batteries of this type. Use appropriate test equipment and safety protocols during development.   
There is no warranty, this may not work as expected or at all! =========================================================================   
This script is intended to read out the Voltage of a single Cell LiIon Battery using a CY-ADS1015 Board:   
3.3V + | .----o----. ___                   |         |  SDA .--------|___|---o----o---------o AIN0    o------ |         2MΩ    |    |         |         |  SCL |               .-.   |         | ADS1015 o------ ---              | |  ---        |         | Battery  -          1.5MΩ| |  ---100nF   '----o----' 2.9V-4.2V|               '-'   |              | |                |    |              | ===              ===  ===            ===   
Attention: - the circuit is constantly draining the battery! (leak current up to: 2.1µA) - the time between sample needs to be a minimum 1sec with this high impedance voltage divider don't use the continuous conversion method! 

## Methods


### __init__




#### Parameters
name | description | default
--- | --- | ---
self |  | 
cfg |  | 





### init_batt_mon_hw




#### Parameters
name | description | default
--- | --- | ---
self |  | 
num |  | 
denom |  | 





### get_batt_voltage




#### Parameters
name | description | default
--- | --- | ---
self |  | 




