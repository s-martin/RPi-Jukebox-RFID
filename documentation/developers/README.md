# Python Documentation

## Classes

**[PaConfigClass](PaConfigClass.md)**: 

**[ConfigHandler](ConfigHandler.md)**: The configuration handler class   
Don't instantiate directly. Always use :func:`get_handler`!   
**Threads:**   
All threads can read and write to the configuration data. **Proper thread-safeness must be ensured** by the the thread modifying the data by acquiring the lock Easiest and best way is to use the context handler::   
with cfg: cfg['key'] = 66 cfg.setndefault('hello', value='world')   
For a single function call, this is done implicitly. In this case, there is no need to explicitly acquire the lock.   
Alternatively, you can lock and release manually by using :func:`acquire` and :func:`release` But be very sure to release the lock even in cases of errors an exceptions! Else we have a deadlock.   
Reading may be done without acquiring a lock. But be aware that when reading multiple values without locking, another thread may intervene and modify some values in between! So, locking is still recommended. 

**[PlaylistEntry](PlaylistEntry.md)**: 

**[PlaylistCollector](PlaylistCollector.md)**: Build a playlist from directory(s)   
This class is intended to be used with an absolute path to the music library::   
plc = PlaylistCollector('/home/chris/music') plc.parse('Traumfaenger') print(f"res = {plc}")   
But it can also be used with relative paths from current working directory::   
plc = PlaylistCollector('.') plc.parse('../../../../music/Traumfaenger') print(f"res = {plc}")   
The file ending exclusion list :attr:`PlaylistCollector._exclude_endings` is a class variable for performance reasons. If changed it will affect all instances. For modifications always call :func:`set_exclusion_endings`. 

**[JukeBox](JukeBox.md)**: 

**[JukeBoxBuilder](JukeBoxBuilder.md)**: 

**[CallbackHandler](CallbackHandler.md)**: Generic Callback Handler to collect callbacks functions through :func:`register` and execute them with :func:`run_callbacks`   
A lock is used to sequence registering of new functions and running callbacks.   
:param name: A name of this handler for usage in log messages :param logger: The logger instance to use for logging :param context: A custom context handler to use as lock. If none, a local :class:`threading.Lock()` will be created 

**[MultiTimer](MultiTimer.md)**: Call a function after a specified number of seconds, repeat that iteration times   
May be cancelled during any of the wait times. Function is called with keyword parameter 'iteration' (which decreases down to 0 for the last iteration)   
If iterations is negative, an endlessly repeating timer is created (which needs to be cancelled with cancel())   
Initiates start and publishing by calling self.publish_callback   
Note: Inspired by threading.Timer and generally using the same API 

**[GenericTimerClass](GenericTimerClass.md)**: Interface for plugin / RPC accessibility for a single event timer 

**[GenericEndlessTimerClass](GenericEndlessTimerClass.md)**: Interface for plugin / RPC accessibility for an event timer call function endlessly every m seconds 

**[GenericMultiTimerClass](GenericMultiTimerClass.md)**: Interface for plugin / RPC accessibility for an event timer that performs an action n times every m seconds 

**[nv_manager](nv_manager.md)**: 

**[nv_dict](nv_dict.md)**: 

**[PluginPackageClass](PluginPackageClass.md)**: A local data class for holding all information about a loaded plugin package 

**[LastValueCache](LastValueCache.md)**: 

**[PublishServer](PublishServer.md)**: The publish proxy server that collects and caches messages from all internal publishers and forwards them to the outside world   
Handles new subscriptions by sending out the entire cached state to **all** subscribers   
The code is structures using a `Reactor Pattern <https://zguide.zeromq.org/docs/chapter5/#Using-a-Reactor>`_ 

**[Publisher](Publisher.md)**: The publisher that provides the functional interface to the application   
.. note:: * An instance must not be shared across threads! * One instance per thread is enough 

**[Subscriber](Subscriber.md)**: 

**[RpcServer](RpcServer.md)**: The RPC Server Class 

**[RpcClient](RpcClient.md)**: 

**[ColorFilter](ColorFilter.md)**: This filter adds colors to the logger   
It adds all colors from simplecolors by using the color name as new keyword, i.e. use %(colorname)c or {colorname} in the formatter string   
It also adds the keyword {levelnameColored} which is an auto-colored drop-in replacement for the levelname depending on severity.   
Don't forget to {reset} the color settings at the end of the string. 

**[PubStream](PubStream.md)**: " Stream handler wrapper around the publisher for logging.StreamHandler   
Allows logging to send all log information (based on logging configuration) to the Publisher.   
ATTENTION: This can lead to recursions!   
Recursions come up when (a) Publish.send / PublishServer.send also emits logs, which cause a another send, which emits a log, which causes a send, ..... (b) Publisher initialization emits logs, which need a Publisher instance to send logs   
IMPORTANT: To avoid endless recursions: The creation of a Publisher MUST NOT generate any log messages! Nor any of the functions in the send-function stack! 

**[PubStreamHandler](PubStreamHandler.md)**: Wrapper for logging.StreamHandler with stream = PubStream   
This serves one purpose: In logger.yaml custom handlers can be configured (which are automatically instantiated). Using this Handler, we can output to PubStream whithout support code to instantiate PubStream keeping this file generic 

**[Colors](Colors.md)**: Container class for all the colors as constants 

**[MpdLock](MpdLock.md)**: 

**[PlayerMPD](PlayerMPD.md)**: Interface to MPD Music Player Daemon 

**[PlayCardState](PlayCardState.md)**: 

**[PlayContentCallbacks](PlayContentCallbacks.md)**: Callbacks are executed in various play functions 

**[EvDevKeyListener](EvDevKeyListener.md)**: Opens and event input device from ``/dev/inputs``, and runs callbacks upon the button presses. Input devices could be .e.g. Keyboard, Bluetooth audio buttons, USB buttons   
Runs as a separate thread. When device disconnects or disappears, thread exists. A new thread must be started when device re-connects.   
Assign callbacks to :attr:`EvDevKeyListener.button_callbacks` 

**[NameMixin](NameMixin.md)**: 

**[LED](LED.md)**: A binary LED   
:param pin: The GPIO pin which the LED is connected   
:param active_high: If :data:`true` the output pin will have a high logic level when the device is turned on.   
:param pin_factory: The GPIOZero pin factory. This parameter cannot be set through the configuration file   
:type name: str :param name: The name of the button for use in error messages. This parameter cannot be set explicitly through the configuration file 

**[Buzzer](Buzzer.md)**: 

**[PWMLED](PWMLED.md)**: 

**[RGBLED](RGBLED.md)**: 

**[TonalBuzzer](TonalBuzzer.md)**: 

**[NameMixin](NameMixin.md)**: Provides name property and RPC decode function   
:meta private: 

**[EventProperty](EventProperty.md)**: Event callback property   
:meta private: 

**[ButtonBase](ButtonBase.md)**: Common stuff for single button devices   
:meta private: 

**[Button](Button.md)**: A basic Button that runs a single actions on button press   
:type pull_up: bool :param pull_up: If :data:`True`, the device uses an internal pull-up resistor to set the GPIO pin “high” by default. If :data:`False` the internal pull-down resistor is used. If :data:`None`, the pin will be floating and an external resistor must be used and the :attr:`active_state` must be set.   
:type active_state: bool or None :param active_state: If :data:`True`, when the hardware pin state is ``HIGH``, the software pin is ``HIGH``. If :data:`False`, the input polarity is reversed: when the hardware pin state is ``HIGH``, the software pin state is ``LOW``. Use this parameter to set the active state of the underlying pin when configuring it as not pulled (when *pull_up* is :data:`None`). When *pull_up* is :data:`True` or :data:`False`, the active state is automatically set to the proper value.   
:type bounce_time: float or None :param bounce_time: Specifies the length of time (in seconds) that the component will ignore changes in state after an initial change. This defaults to :data:`None` which indicates that no bounce compensation will be performed.   
:type hold_repeat: bool :param hold_repeat: If :data:`True` repeat the :attr:`on_press` every :attr:`hold_time` seconds. Else action is run only once independent of the length of time the button is pressed for.   
:type hold_time: float :param hold_time: Time in seconds to wait between invocations of :attr:`on_press`.   
:param pin_factory: The GPIOZero pin factory. This parameter cannot be set through the configuration file   
:type name: str :param name: The name of the button for use in error messages. This parameter cannot be set explicitly through the configuration file   
.. copied from GPIOZero's documentation: active_state, bounce_time .. Copyright Ben Nuttall / SPDX-License-Identifier: BSD-3-Clause 

**[LongPressButton](LongPressButton.md)**: A Button that runs a single actions only when the button is pressed long enough   
:param pull_up: See `Button`_   
:param active_state: See `Button`_   
:param bounce_time: See `Button`_   
:param hold_repeat: If :data:`True` repeat the :attr:`on_press` every :attr:`hold_time` seconds. Else only action is run only once independent of the length of time the button is pressed for.   
:param hold_time: The minimum time, the button must be pressed be running :attr:`on_press` for the first time. Also the time in seconds to wait between invocations of :attr:`on_press`. 

**[ShortLongPressButton](ShortLongPressButton.md)**: A single button that runs two different actions depending if the button is pressed for a short or long time.   
The shortest possible time is used to ensure a unique identification to an action can be made. For example a short press can only be identified, when a button is released before :attr:`hold_time`, i.e. not directly on button press. But a long press can be identified as soon as :attr:`hold_time` is reached and there is no need to wait for the release event. Furthermore, if there is a long hold, only the long hold action is executed - the short press action is not run in this case!   
:param pull_up: See `Button`_   
:param active_state: See `Button`_   
:param bounce_time: See `Button`_   
:param hold_time: The time in seconds to differentiate if it is a short or long press. If the button is released before this time, it is a short press. As soon as the button is held for :attr:`hold_time` it is a long press and the short press action is ignored   
:param hold_repeat: If :data:`True` repeat the long press action every :attr:`hold_time` seconds after first long press action   
:param pin_factory: See `Button`_   
:param name: See `Button`_ 

**[RotaryEncoder](RotaryEncoder.md)**: A rotary encoder to run one of two actions depending on the rotation direction.   
:param bounce_time: See `Button`_   
:param pin_factory: See `Button`_   
:param name: See `Button`_ 

**[TwinButton](TwinButton.md)**: A two-button device which can run up to six different actions, a.k.a the six function beast.   
Per user press "input" of the TwinButton, only a single callback is executed (but this callback may be executed several times). The shortest possible time is used to ensure a unique identification to an action can be made. For example a short press can only be identified, when a button is released before :attr:`hold_time`, i.e. not directly on button press. But a long press can be identified as soon as :attr:`hold_time` is reached and there is no need to wait for the release event. Furthermore, if there is a long hold, only the long hold action is executed - the short press action is not run in this case!   
It is not necessary to configure all actions.   
:param pull_up: See `Button`_   
:param active_state: See `Button`_   
:param bounce_time: See `Button`_   
:param hold_time: The time in seconds to differentiate if it is a short or long press. If the button is released before this time, it is a short press. As soon as the button is held for :attr:`hold_time` it is a long press and the short press action is ignored.   
:param hold_repeat: If :data:`True` repeat the long press action every :attr:`hold_time` seconds after first long press action. A long dual press is never repeated independent of this setting   
:param pin_factory: See `Button`_   
:param name: See `Button`_ 

**[ColorProperty](ColorProperty.md)**: Color descriptor ensuring valid weight ranges   
:meta private: 

**[VolumeToRGB](VolumeToRGB.md)**: Converts linear volume level to an RGB color value running through the color spectrum   
:param max_input: Maximum input value of linear input data :param offset: Offset in degrees in the color circle. Color circle traverses blue (0), cyan(60), green (120), yellow(180), red (240), magenta (340) :param section: The section of the full color circle to use in degrees   
Map input :data:`0...100` to color range :data:`green...magenta` and get the color for level 50   
.. code-block:: python   
conv = VolumeToRGB(100, offset=120, section=180) (r, g, b) = conv(50)   
The three components of an RGB LEDs do not have the same luminosity. Weight factors are used to get a balanced color output 

**[ServiceIsRunningCallbacks](ServiceIsRunningCallbacks.md)**: Callbacks are executed when   
* Jukebox app started * Jukebox shuts down   
This is intended to e.g. signal an LED to change state. This is integrated into this module because:   
* we need the GPIO to control a LED (it must be available when the status callback comes) * the plugin callback functions provide all the functionality to control the status of the LED * which means no need to adapt other modules 

**[ReaderBaseClass](ReaderBaseClass.md)**: Abstract Base Class for all Reader Classes to ensure common API   
Look at template_new_reader.py for documentation how to integrate a new RFID reader 

**[ReaderClass](ReaderClass.md)**: 

**[ReaderClass](ReaderClass.md)**: 

**[ReaderClass](ReaderClass.md)**: 

**[ReaderClass](ReaderClass.md)**: 

**[ReaderClass](ReaderClass.md)**: The actual reader class that is used to read RFID cards.   
It will be instantiated once and then read_card() is called in an endless loop.   
It will be used in a  manner with Reader(reader_cfg_key) as reader: for card_id in reader: ... which ensures proper resource de-allocation. For this to work derive this class from ReaderBaseClass. All the required interfaces are implemented there.   
Put your code into these functions (see below for more information) - __init__ - read_card - cleanup - stop 

**[ReaderClass](ReaderClass.md)**: 

**[RfidCardDetectState](RfidCardDetectState.md)**: 

**[RfidCardDetectCallbacks](RfidCardDetectCallbacks.md)**: Callbacks are executed if rfid card is detected 

**[CardRemovalTimerClass](CardRemovalTimerClass.md)**: A timer watchdog thread that calls timeout_action on time-out 

**[ReaderRunner](ReaderRunner.md)**: 

**[JingleFactory](JingleFactory.md)**: Jingle Factory 

**[AlsaWave](AlsaWave.md)**: Jingle Service for playing wave files directly from Python through ALSA 

**[AlsaWaveBuilder](AlsaWaveBuilder.md)**: 

**[JingleMp3Play](JingleMp3Play.md)**: Jingle Service for playing MP3 files 

**[JingleMp3PlayBuilder](JingleMp3PlayBuilder.md)**: 

**[pt1_frac](pt1_frac.md)**: fixed point first order filter, fractional format: 2^16,2^16 

**[BattmonBase](BattmonBase.md)**: Battery Monitor base class 

**[battmon_ads1015](battmon_ads1015.md)**: Battery Monitor based on a ADS1015   
CAUTION - WARNING ======================================================================== Lithium and other batteries are dangerous and must be treated with care. Rechargeable Lithium Ion batteries are potentially hazardous and can present a serious FIRE HAZARD if damaged, defective or improperly used. Do not use this circuit to a lithium ion battery without expertise and training in handling and use of batteries of this type. Use appropriate test equipment and safety protocols during development.   
There is no warranty, this may not work as expected or at all! =========================================================================   
This script is intended to read out the Voltage of a single Cell LiIon Battery using a CY-ADS1015 Board:   
3.3V + | .----o----. ___                   |         |  SDA .--------|___|---o----o---------o AIN0    o------ |         2MΩ    |    |         |         |  SCL |               .-.   |         | ADS1015 o------ ---              | |  ---        |         | Battery  -          1.5MΩ| |  ---100nF   '----o----' 2.9V-4.2V|               '-'   |              | |                |    |              | ===              ===  ===            ===   
Attention: - the circuit is constantly draining the battery! (leak current up to: 2.1µA) - the time between sample needs to be a minimum 1sec with this high impedance voltage divider don't use the continuous conversion method! 

**[battmon_simulator](battmon_simulator.md)**: Battery Monitor Simulator 

**[VolumeFadeOutActionClass](VolumeFadeOutActionClass.md)**: 

**[PulseMonitor](PulseMonitor.md)**: A thread for monitoring and interacting with the Pulse Lib via pulsectrl   
Whenever we want to access pulsectl, we need to exit the event listen loop. This is handled by the context manager. It stops the event loop and returns the pulsectl instance to be used (it does no return the monitor thread itself!)   
The context manager also locks the module to ensure proper thread sequencing, as only a single thread may work with pulsectl at any time. Currently, an RLock is used, even if it may not be necessary 

**[PulseVolumeControl](PulseVolumeControl.md)**: Volume control manager for PulseAudio   
When accessing the pulse library, it needs to be put into a special state. Which is ensured by the context manager   
.. code-block: python   
with pulse_monitor as pulse ...   
  
All private functions starting with `_function_name` assume that this is ensured by the calling function. All user functions acquire proper context! 

**[MusicLibPath](MusicLibPath.md)**: Extract the music directory from the mpd.conf file 

**[SyncRfidcards](SyncRfidcards.md)**: Control class for sync RFID cards functionality 

**[MusicCoverArt](MusicCoverArt.md)**: 


## Functions

### main







### main







### main



#### Parameters
name | description | default
--- | --- | ---
address |  | 
topic |  | 





### add_cli







### get_help



#### Parameters
name | description | default
--- | --- | ---
scr |  | 





### format_help



#### Parameters
name | description | default
--- | --- | ---
scr |  | 
topic |  | 





### format_welcome



#### Parameters
name | description | default
--- | --- | ---
scr |  | 





### format_usage



#### Parameters
name | description | default
--- | --- | ---
scr |  | 





### get_common_beginning


Return the strings that are common to the beginning of each string in the strings list. 
#### Parameters
name | description | default
--- | --- | ---
strings |  | 





### autocomplete



#### Parameters
name | description | default
--- | --- | ---
msg |  | 





### is_printable



#### Parameters
name | description | default
--- | --- | ---
ch |  | 





### reprompt



#### Parameters
name | description | default
--- | --- | ---
scr |  | 
msg |  | 
y |  | 
x |  | 





### get_input



#### Parameters
name | description | default
--- | --- | ---
scr |  | 





### tonum



#### Parameters
name | description | default
--- | --- | ---
string_value |  | 





### main



#### Parameters
name | description | default
--- | --- | ---
scr |  | 





### sink_is_equalizer



#### Parameters
name | description | default
--- | --- | ---
sink |  | 





### sink_is_monomixer



#### Parameters
name | description | default
--- | --- | ---
sink |  | 





### yield_upstream_sink



#### Parameters
name | description | default
--- | --- | ---
sink |  | 
all_sinks |  | 





### yield_downstream_sink



#### Parameters
name | description | default
--- | --- | ---
sink |  | 
all_sinks |  | 





### build_processing_chain



#### Parameters
name | description | default
--- | --- | ---
sink |  | 
all_sinks |  | 





### query_sinks



#### Parameters
name | description | default
--- | --- | ---
pulse_config |  | 





### configure_pa_equalizer



#### Parameters
name | description | default
--- | --- | ---
pulse_cfg_file_content |  | 
pulse_config |  | 





### configure_pa_monomixer



#### Parameters
name | description | default
--- | --- | ---
pulse_cfg_file_content |  | 
pulse_config |  | 





### configure_pa_system_default



#### Parameters
name | description | default
--- | --- | ---
pulse_cfg_file_content |  | 
pulse_config |  | 





### configure_pa_switch_on_connect



#### Parameters
name | description | default
--- | --- | ---
pulse_cfg_file_content |  | 





### query_create_default_pa_config



#### Parameters
name | description | default
--- | --- | ---
script_path |  | 
config_file_path |  | 





### configure_pulseaudio



#### Parameters
name | description | default
--- | --- | ---
pulse_config |  | 





### configure_jukebox



#### Parameters
name | description | default
--- | --- | ---
pulse_config |  | 





### welcome



#### Parameters
name | description | default
--- | --- | ---
pulse_config |  | 





### goodbye



#### Parameters
name | description | default
--- | --- | ---
pulse_config |  | 





### main







### _acquire_lock


Acquire the module-level lock for serializing access to shared data.   
This should be released with _releaseLock(). 




### _release_lock


Release the module-level lock acquired by calling _acquireLock(). 




### get_handler


Get a configuration data handler with the specified name, creating it if it doesn't yet exit. If created, it is always created empty.   
This is the main entry point for obtaining an configuration handler   
:param name: Name of the config handler :return: The configuration data handler for *name* :rtype: ConfigHandler 
#### Parameters
name | description | default
--- | --- | ---
name |  | 





### load_yaml


Load a yaml file into a ConfigHandler   
:param cfg: ConfigHandler instance :param filename: filename to yaml file :return: None 
#### Parameters
name | description | default
--- | --- | ---
cfg |  | 
filename |  | 





### write_yaml


Writes ConfigHandler data to yaml file / sys.stdout   
:param cfg: ConfigHandler instance :param filename: filename to output file. If *sys.stdout*, output is written to console :param only_if_changed: Write file only, if ConfigHandler.is_modified() :param args: passed on to yaml.dump(...) :param kwargs: passed on to yaml.dump(...) :return: None 
#### Parameters
name | description | default
--- | --- | ---
cfg |  | 
filename |  | 
only_if_changed |  | False





### version


Return the Jukebox version as a string 




### version_info


Return the Jukebox version as a tuple of three numbers   
If this is a development version, an identifier string will be appended after the third integer. 




### decode_podcast_core



#### Parameters
name | description | default
--- | --- | ---
url |  | 
playlist |  | 





### decode_podcast



#### Parameters
name | description | default
--- | --- | ---
filename |  | 
path |  | 
playlist |  | 





### decode_livestream



#### Parameters
name | description | default
--- | --- | ---
filename |  | 
path |  | 
playlist |  | 





### decode_musicfile



#### Parameters
name | description | default
--- | --- | ---
filename |  | 
path |  | 
playlist |  | 





### decode_m3u



#### Parameters
name | description | default
--- | --- | ---
filename |  | 
path |  | 
playlist |  | 





### log_active_threads


This functions is registered with atexit very early, meaning it will be run very late. It is the best guess to evaluate which Threads are still running (and probably shouldn't be)   
This function is registered before all the plugins and their dependencies are loaded 




### get_jukebox_daemon







### decode_rpc_call


Makes sure that the core rpc call parameters have valid default values in cfg_rpc_call.   
.. important: Leaves all other parameters in cfg_action untouched or later downstream processing!   
:param cfg_rpc_call: RPC command as configuration entry :return: A fully populated deep copy of cfg_rpc_call 
#### Parameters
name | description | default
--- | --- | ---
cfg_rpc_call |  | 





### decode_rpc_command


Decode an RPC Command from a config entry.   
This means   
* Decode RPC command alias (if present) * Ensure all RPC call parameters have valid default values   
If the command alias cannot be decoded correctly, the command is mapped to misc.empty_rpc_call which emits a misuse warning when called If an explicitly specified this is not done. However, it is ensured that the returned dictionary contains all mandatory parameters for an RPC call. RPC call functions have error handling for non-existing RPC commands and we get a clearer error message.   
:param cfg_rpc_cmd: RPC command as configuration entry :param logger: The logger to use :return: A decoded, fully populated deep copy of cfg_rpc_cmd 
#### Parameters
name | description | default
--- | --- | ---
cfg_rpc_cmd |  | 
logger |  | 





### decode_and_call_rpc_command


Convenience function combining decode_rpc_command and plugs.call_ignore_errors 
#### Parameters
name | description | default
--- | --- | ---
rpc_cmd |  | 
logger |  | 





### bind_rpc_command


Decode an RPC command configuration entry and bind it to a function   
:param dereference: Dereference even the call to plugs.call(...)   
#. If false, the returned function is ``plugs.call(package, plugin, method, *args, **kwargs)`` with all checks applied at bind time #. If true, the returned function is ``package.plugin.method(*args, **kwargs)`` with all checks applied at bind time.   
Setting deference to True, circumvents the dynamic nature of the plugins: the function to call must exist at bind time and cannot change. If False, the function to call must only exist at call time. This can be important during the initialization where package ordering and initialization means that not all classes have been instantiated yet. With dereference=True also the plugs thread lock for serialization of calls is circumvented. Use with care!   
:return: Callable function w/o parameters which directly runs the RPC command using plugs.call_ignore_errors 
#### Parameters
name | description | default
--- | --- | ---
cfg_rpc_cmd |  | 
dereference |  | False
logger |  | 





### rpc_call_to_str


Return a readable string of an RPC call config   
:param cfg_rpc_call: RPC call configuration entry :param with_args: Return string shall include the arguments of the function 
#### Parameters
name | description | default
--- | --- | ---
cfg_rpc_call |  | 
with_args |  | True





### indent



#### Parameters
name | description | default
--- | --- | ---
doc |  | 
spaces |  | 4





### generate_cmd_alias_rst


Write a reference of all rpc command aliases in Restructured Text format 
#### Parameters
name | description | default
--- | --- | ---
stream |  | 





### generate_cmd_alias_reference


Write a reference of all rpc command aliases in text format 
#### Parameters
name | description | default
--- | --- | ---
stream |  | 





### get_git_state


Return git state information for the current branch 




### _acquire_lock


Acquire the module-level lock for serializing access to shared data.   
This should be released with _releaseLock(). 




### _release_lock


Release the module-level lock acquired by calling _acquireLock(). 




### _deduce_package_origin


Given an object try to find which python package it belongs to in plugs.py terms   
:return: None if failed for up level error handling / Exception raising 
#### Parameters
name | description | default
--- | --- | ---
obj |  | 





### _enlist


Internal function for putting the plugin_obj in the storage container 
#### Parameters
name | description | default
--- | --- | ---
package |  | 
plugin_obj |  | 
plugin_name |  | 





### _register_obj


Register a non-class plugin object for a package. Use via the generic 'register' function.   
This function can register: - function in decorator style (cannot use name and package) - function as dynamic function style - bound method as dynamic function style - class instance as dynamic function style. Methods of class instances are only made callable, if they are tagged with the decorator @plugin.tag!   
:param plugin: Function to register :param name: Register with this name, if None the name is that of the function. Only of not used as decorator :param package: Register plugin with the package, if None use the configured plugin package for the python package :return: The object itself 
#### Parameters
name | description | default
--- | --- | ---
plugin |  | 
name |  | None
package |  | None





### _register_class


Decorator for classes. Decorated classes will auto-register when initialized   
The decorated class will have two additional parameters in the constructor! See __init__ below.   
Methods are not automatically made callable via the plugs interface! Only those methods tagged with the decorator @plugin.tag can be called via the plugs interface.   
Developers note: It is not guaranteed that the instantiation takes place during the loading of the module. For this case we store the name of the plugin package which we get during loading of the module into a Class variable. This is later used when the instance is registered.   
:param cls: The class to decorate :param auto_tag: Automatically tag all methods as callable through the plugs interface :return: The decorated class 
#### Parameters
name | description | default
--- | --- | ---
cls |  | 
auto_tag |  | False





### register


1-level decorator around a function 
#### Parameters
name | description | default
--- | --- | ---
plugin |  | 





### register


Signature: 1-level decorator around a class 
#### Parameters
name | description | default
--- | --- | ---
plugin |  | 





### register


Signature: 2-level decorator around a function 




### register


Signature: 2-level decorator around a class 




### register


Signature: Run-time registration of function / class instance / bound method 
#### Parameters
name | description | default
--- | --- | ---
plugin |  | None





### register


A generic decorator / run-time function to register plugin module callables   
The functions comes in five distinct signatures for 5 use cases:   
1. ``@plugs.register``: decorator for a class w/o any arguments 2. ``@plugs.register``: decorator for a function w/o any arguments 3. ``@plugs.register(auto_tag=bool)``: decorator for a class with 1 arguments 4. ``@plugs.register(name=name, package=package)``: decorator for a function with 1 or 2 arguments 5. ``plugs.register(plugin, name=name, package=package)``: run-time registration of   
* function * bound method * class instance   
For more documentation see the functions   
* :func:`_register_obj` * :func:`_register_class`   
See the examples in Module :mod:`plugs` how to use this decorator / function   
:param plugin: :param name: :param package: :param replace: :param auto_tag: :return: 
#### Parameters
name | description | default
--- | --- | ---
plugin |  | None





### tag


Method decorator for tagging a method as callable through the plugs interface   
Note that the instantiated class must still be registered as plugin object (either with the class decorator or dynamically)   
:param func: function to decorate :return: the function 
#### Parameters
name | description | default
--- | --- | ---
func |  | 





### initialize


Decorator for functions that shall be called by the plugs package directly after the module is loaded   
:param func: Function to decorate :return: The function itself 
#### Parameters
name | description | default
--- | --- | ---
func |  | 





### finalize


Decorator for functions that shall be called by the plugs package directly after ALL modules are loaded   
:param func: Function to decorate :return: The function itself 
#### Parameters
name | description | default
--- | --- | ---
func |  | 





### atexit


Decorator for functions that shall be called by the plugs package directly after at exit of program.   
.. important:: There is no automatism as in atexit.atexit. The function plugs.shutdown() must be explicitly called during the shutdown procedure of your program. This is by design, so you can choose the exact situation in your shutdown handler.   
The atexit-functions are called with a single integer argument, which is passed down from plugin.exit(int) It is intended for passing down the signal number that initiated the program termination   
:param func: Function to decorate :return: The function itself 
#### Parameters
name | description | default
--- | --- | ---
func |  | 





### load


Loads a python package as plugin package   
Executes a regular python package load. That means a potentially existing __init__.py is executed. Decorator @register can by used to register functions / classes / class istances as plugin callable Decorator @initializer can be used to tag functions that shall be called after package loading Decorator @finalizer can be used to tag functions that shall be called after ALL plugin packges have been loaded Instead of using @initializer, you may of course use __init__.py   
Python packages may be loaded under a different plugs package name. Python packages must be unique and the name under which they are loaded as plugin package also.   
:param package: Python package to load as plugin package :param load_as: Plugin package registration name. If None the name is the python's package simple name :param prefix: Prefix to python package to create fully qualified name. This is used only to locate the python package and ignored otherwise. Useful if all the plugin module are in a dedicated folder :return: 
#### Parameters
name | description | default
--- | --- | ---
package |  | 
load_as |  | None
prefix |  | None





### load_all_named


Load all packages in packages_named with mapped names   
:param packages_named: Dict[load_as, package] 
#### Parameters
name | description | default
--- | --- | ---
packages_named |  | 
prefix |  | None
ignore_errors |  | False





### load_all_unnamed


Load all packages in packages_unnamed with default names 
#### Parameters
name | description | default
--- | --- | ---
packages_unnamed |  | 
prefix |  | None
ignore_errors |  | False





### load_all_finalize


Calls all functions registered with @finalize from all loaded modules in the order they were loaded   
This must be executed after the last plugin package is loaded 
#### Parameters
name | description | default
--- | --- | ---
ignore_errors |  | False





### close_down


Calls all functions registered with @atexit from all loaded modules in reverse order of module load order   
Modules are processed in reverse order. Several at-exit tagged functions of a single module are processed in the order of registration.   
Errors raised in functions are suppressed to ensure all plugins are processed :return: 




### dereference



#### Parameters
name | description | default
--- | --- | ---
package |  | 
plugin |  | 
method |  | None





### _call


The internals of the call functionality. See :func:`call` for documentation!   
This low-level core is not thread safe! Surrounding function must lock the module properly. 
#### Parameters
name | description | default
--- | --- | ---
package |  | 
plugin |  | 
method |  | None





### call


Call a function/method from the loaded plugins   
If a plugin is a function or a callable instance of a class, this is equivalent to   
``package.plugin(*args, **kwargs)``   
If plugin is a class instance from which a method is called, this is equivalent to the followig. Also remember, that method must have the attribute ``plugin_callable = True``   
``package.plugin.method(*args, **kwargs)``   
Calls are serialized by a thread lock. The thread lock is shared with call_ignore_errors.   
.. note:: There is no logger in this function as they all belong up-level where the exceptions are handled. If you want logger messages instead of exceptions, use :func:`call_ignore_errors`   
:param package: Name of the plugin package in which to look for function/class instance :param plugin: Function name or instance name of a class :param method: Method name when accessing a class instance' method. Leave at *None* if unneeded. :param as_thread: Run the callable in separate daemon thread. There is no return value from the callable in this case! The return value is the thread object. Also note that Exceptions in the Thread must be handled in the Thread and are not propagated to the main Thread. All threads are started as daemon threads with terminate upon main program termination. There is not stop-thread mechanism. This is intended for short lived threads. :param thread_name: Name of the thread :param args: Arguments passed to callable :param kwargs: Keyword arguments passed to callable :return: The return value from the called function, or, if started as thread the thread object 
#### Parameters
name | description | default
--- | --- | ---
package |  | 
plugin |  | 
method |  | None





### call_ignore_errors


Call a function/method from the loaded plugins ignoring all raised Exceptions.   
Errors get logged.   
See :func:`call` for parameter documentation. 
#### Parameters
name | description | default
--- | --- | ---
package |  | 
plugin |  | 
method |  | None





### exists


Check if an object is registered within the plugs package 
#### Parameters
name | description | default
--- | --- | ---
package |  | 
plugin |  | None
method |  | None





### get


Get a plugs-package registered object   
The return object depends on the number of parameters   
* 1 argument: Get the python module reference for the plugs *package* * 2 arguments: Get the plugin reference for the plugs *package.plugin* * 3 arguments: Get the plugin reference for the plugs *package.plugin.method* 
#### Parameters
name | description | default
--- | --- | ---
package |  | 
plugin |  | None
method |  | None





### loaded_as


Return the plugin name a python module is loaded as 
#### Parameters
name | description | default
--- | --- | ---
module_name |  | 





### delete


Delete a plugin object from the registered plugs callables   
Note: This does not 'unload' the python module. It merely makes it un-callable via plugs! 
#### Parameters
name | description | default
--- | --- | ---
package |  | 
plugin |  | None
ignore_errors |  | False





### dump_plugins


Write a human readable summary of all plugin callables to stream 
#### Parameters
name | description | default
--- | --- | ---
stream |  | 





### summarize


Create a reference summary of all plugin callables in dictionary format 




### _indent



#### Parameters
name | description | default
--- | --- | ---
doc |  | 
spaces |  | 4





### generate_help_rst


Write a reference of all plugin callables in Restructured Text format 
#### Parameters
name | description | default
--- | --- | ---
stream |  | 





### get_all_loaded_packages


Report a short summary of all loaded packages   
:return: Dictionary of the form `{loaded_as: loaded_from, ...}` 




### get_all_failed_packages


Report those packages that did not load error free   
.. note:: Package could fail to load   
1. altogether: these package are not registered 2. partially: during initializer, finalizer functions: The package is loaded, but the function did not execute error-free   
Partially loaded packages are listed in both _PLUGINS and _PLUGINS_FAILED   
:return: Dictionary of the form `{loaded_as: loaded_from, ...}` 




### get_publisher


Return the publisher instance for this thread   
Per thread, only one publisher instance is required to connect to the inproc socket. A new instance is created if it does not already exist.   
If there is a remote-chance that your function publishing something may be called form different threads, always make a fresh call to ``get_publisher()`` to get the correct instance for the current thread.   
Example::   
import jukebox.publishing as publishing   
class MyClass: def __init__(self): pass   
def say_hello(name): publishing.get_publisher().send('hello', f'Hi {name}, howya?')   
To stress what **NOT** to do: don't get a publisher instance in the constructor and save it to ``self._pub``. If you do and ``say_hello`` gets called from different threads, the publisher of the thread which instantiated the class will be used.   
If you need your very own private Publisher Instance, you'll need to instantiate it yourself. But: the use cases are very rare for that. I cannot think of one at the moment.   
**Remember**: Don’t share ZeroMQ sockets between threads. 




### run_unix_command



#### Parameters
name | description | default
--- | --- | ---
command |  | 





### with_espeak



#### Parameters
name | description | default
--- | --- | ---
text |  | 
lang |  | None
speed |  | None
speak_punct |  | None
voice |  | None





### say



#### Parameters
name | description | default
--- | --- | ---
text |  | 
lang |  | None
speed |  | None
speak_punct |  | None
voice |  | None





### recursive_chmod


Recursively change folder and file permissions   
mode_files/mode dirs can be given in octal notation e.g. 0o777 flags from the stats module.   
Reference: https://docs.python.org/3/library/os.html#os.chmod 
#### Parameters
name | description | default
--- | --- | ---
path |  | 
mode_files |  | 
mode_dirs |  | 





### flatten


Flatten all levels of hierarchy in nested iterables 
#### Parameters
name | description | default
--- | --- | ---
iterable |  | 





### getattr_hierarchical


Like the builtin getattr, but descends though the hierarchy levels 
#### Parameters
name | description | default
--- | --- | ---
obj |  | 
name |  | 





### configure_default



#### Parameters
name | description | default
--- | --- | ---
level |  | 
name |  | "jb"
with_publisher |  | False





### configure_from_file



#### Parameters
name | description | default
--- | --- | ---
filename |  | None





### resolve


Resolve a color name into the respective color constant   
:param color_name: Name of the color :return: color constant 
#### Parameters
name | description | default
--- | --- | ---
color_name |  | 





### print


Drop-in replacement for print with color choice and auto color reset for convenience   
Use just as a regular print function, but with first parameter as color 
#### Parameters
name | description | default
--- | --- | ---
color |  | 





### input_int


Request an integer input from user   
:param prompt: The prompt to display :param blank: Value to return when user just hits enter. Leave at None, if blank is invalid :param min: Minimum valid integer value (None disables this check) :param max: Maximum valid integer value (None disables this check) :param prompt_color: Color of the prompt. Color will be reset at end of prompt :param prompt_hint: Append a 'hint' with [min...max, default=xx] to end of prompt :return: integer value read from user input 
#### Parameters
name | description | default
--- | --- | ---
prompt |  | 
blank |  | None
min |  | None
max |  | None
prompt_color |  | None
prompt_hint |  | False





### input_yesno


Request a yes / no choice from user   
Accepts multiple input for true/false and is case insensitive   
:param prompt: The prompt to display :param blank: Value to return when user just hits enter. Leave at None, if blank is invalid :param prompt_color: Color of the prompt. Color will be reset at end of prompt :param prompt_hint: Append a 'hint' with [y/n] to end of prompt. Default choice will be capitalized :return: boolean value read from user input 
#### Parameters
name | description | default
--- | --- | ---
prompt |  | 
blank |  | None
prompt_color |  | None
prompt_hint |  | False





### msg_highlight



#### Parameters
name | description | default
--- | --- | ---
msg |  | 
color |  | 
deliminator_length |  | 79





### rpc_cmd_help


Return all commands for RPC 




### get_all_loaded_packages


Get all successfully loaded plugins 




### get_all_failed_packages


Get all plugins with error during load or initialization 




### get_start_time


Time when JukeBox has been started 




### get_log


Get the log file from the loggers (debug_file_handler, error_file_handler) 
#### Parameters
name | description | default
--- | --- | ---
handler_name |  | 





### get_log_debug


Get the log file (from the debug_file_handler) 




### get_log_error


Get the log file (from the error_file_handler) 




### get_version







### get_git_state


Return git state information for the current branch 




### empty_rpc_call


This function does nothing.   
The RPC command alias 'none' is mapped to this function.   
This is also used when configuration errors lead to non existing RPC command alias definitions. When the alias definition is void, we still want to return a valid function to simplify error handling up the module call stack.   
:param msg: If present, this message is send to the logger with severity warning 
#### Parameters
name | description | default
--- | --- | ---
msg |  | ""





### initialize







### atexit







### _filter_by_mandatory_keys


Generator filtering all_devices based on mandatory keys   
:param all_devices: List of input device candidates :param mandatory_keys: Set of integer key codes that included devices must have 
#### Parameters
name | description | default
--- | --- | ---
all_devices |  | 
mandatory_keys |  | 





### _filter_by_device_name


Generator filtering all_devices based on device_name   
:param all_devices: List of input device candidates :param device_name: The device name to look for :param exact_name: If true, device_name must mach exactly, else a match is returned if device_name is a substring of the reported device name 
#### Parameters
name | description | default
--- | --- | ---
all_devices |  | 
device_name |  | 
exact_name |  | True





### find_device


Find an input device with device_name and mandatory keys.   
Raises   
#. FileNotFoundError, if no device is found. #. AttributeError, if device does not have the mandatory keys   
If multiple devices match, the first match is returned   
:param device_name: See :func:`_filter_by_device_name` :param exact_name: See :func:`_filter_by_device_name` :param mandatory_keys: See :func:`_filter_by_mandatory_keys` :return: The path to the device 
#### Parameters
name | description | default
--- | --- | ---
device_name |  | 
exact_name |  | True
mandatory_keys |  | None





### activate



#### Parameters
name | description | default
--- | --- | ---
device_name |  | 
exact |  | True
open_initial_delay |  | 0.25





### activate_from_pulse



#### Parameters
name | description | default
--- | --- | ---
card_driver |  | 
device_name |  | 





### initialize







### atexit







### republish


Re-publish the topic tree 'topic' to all subscribers   
:param topic: Topic tree to republish. None = resend all 
#### Parameters
name | description | default
--- | --- | ---
topic |  | None





### initialize







### closing







### rewrite



#### Parameters
name | description | default
--- | --- | ---
self |  | 
value |  | 





### patch_mock_outputs_with_callback


Monkey Patch LED + Buzzer to get a callback when state changes   
This targets to represent the state in the TK GUI. Other output devices cannot be represented in the GUI and are silently ignored.   
..note:: Only for developing purposes! 




### build_pin_factory







### connect_output_device



#### Parameters
name | description | default
--- | --- | ---
device |  | 
name |  | 
config |  | 





### build_output_device


Construct and register a new output device   
In principal all supported GPIOZero output devices can be used. For all devices a custom functions need to be written to control the state of the outputs 
#### Parameters
name | description | default
--- | --- | ---
name |  | 
config |  | 





### _build_all_output_devices







### build_input_device


Construct and connect a new input device   
Supported input devices are those from gpio.gpioz.core.input_devices 
#### Parameters
name | description | default
--- | --- | ---
name |  | 
config |  | 





### _build_all_input_devices







### get_output


Get the output device instance based on the configured name   
:param name: The alias name output device instance 
#### Parameters
name | description | default
--- | --- | ---
name |  | 





### on


Turn an output device on   
:param name: The alias name output device instance 
#### Parameters
name | description | default
--- | --- | ---
name |  | 





### off


Turn an output device off   
:param name: The alias name output device instance 
#### Parameters
name | description | default
--- | --- | ---
name |  | 





### set_value


Set the output device to :attr:`value`   
:param name: The alias name output device instance   
:param value: Value to set the device to 
#### Parameters
name | description | default
--- | --- | ---
name |  | 
value |  | 





### flash


Flash (blink or beep) an output device   
This is a generic function for all types of output devices. Parameters not applicable to an specific output device are silently ignored   
:param name: The alias name output device instance   
:param on_time: Time in seconds in state ``ON``   
:param off_time: Time in seconds in state ``OFF``   
:param n: Number of flash cycles   
:param tone: The tone in to play, e.g. 'A4'. *Only for TonalBuzzer*.   
:param color: The RGB color *only for PWMLED*.   
:param fade_in_time: Time in seconds for transitioning to on. *Only for PWMLED and RGBLED*   
:param fade_out_time: Time in seconds for transitioning to off. *Only for PWMLED and RGBLED* 
#### Parameters
name | description | default
--- | --- | ---
name |  | 
on_time |  | 1
off_time |  | 1
n |  | 1





### initialize







### finalize







### plugin_atexit







### _check_device_type


Check device instance is among valid devices types and return according function   
:param device: Device instance :param device_types: Valid device classes :param functions: List of functions - one for each device class in identical order. If only one function is given, it is assumed that the same function is valid for all device classes :return: The respective device function on success, else None 
#### Parameters
name | description | default
--- | --- | ---
device |  | 
device_types |  | 
functions |  | 





### register_rfid_callback


Flash the output device once on successful RFID card detection and thrice if card ID is unknown   
Compatible devices:   
- :class:`components.gpio.gpioz.core.output_devices.LED` - :class:`components.gpio.gpioz.core.output_devices.PWMLED` - :class:`components.gpio.gpioz.core.output_devices.RGBLED` - :class:`components.gpio.gpioz.core.output_devices.Buzzer` - :class:`components.gpio.gpioz.core.output_devices.TonalBuzzer` 
#### Parameters
name | description | default
--- | --- | ---
device |  | 





### register_status_led_callback


Turn LED on when Jukebox App has started   
Compatible devices:   
- :class:`components.gpio.gpioz.core.output_devices.LED` - :class:`components.gpio.gpioz.core.output_devices.PWMLED` - :class:`components.gpio.gpioz.core.output_devices.RGBLED` 
#### Parameters
name | description | default
--- | --- | ---
device |  | 





### register_status_buzzer_callback


Buzz once when Jukebox App has started, twice when closing down   
Compatible devices:   
- :class:`components.gpio.gpioz.core.output_devices.Buzzer` - :class:`components.gpio.gpioz.core.output_devices.TonalBuzzer` 
#### Parameters
name | description | default
--- | --- | ---
device |  | 





### register_status_tonalbuzzer_callback


Buzz a multi-note melody when Jukebox App has started and when closing down   
Compatible devices:   
- :class:`components.gpio.gpioz.core.output_devices.TonalBuzzer` 
#### Parameters
name | description | default
--- | --- | ---
device |  | 





### register_audio_sink_change_callback


Turn LED on if secondary audio output is selected. If audio output change fails, blink thrice   
Compatible devices:   
- :class:`components.gpio.gpioz.core.output_devices.LED` - :class:`components.gpio.gpioz.core.output_devices.PWMLED` - :class:`components.gpio.gpioz.core.output_devices.RGBLED` 
#### Parameters
name | description | default
--- | --- | ---
device |  | 





### register_volume_led_callback


Have a PWMLED change it's brightness according to current volume. LED flashes when minimum or maximum volume is reached. Minimum value is still a very dimly turned on LED (i.e. LED is never off).   
Compatible devices:   
- :class:`components.gpio.gpioz.core.output_devices.PWMLED` 
#### Parameters
name | description | default
--- | --- | ---
device |  | 





### register_volume_buzzer_callback


Sound a buzzer once when minimum or maximum value is reached   
Compatible devices:   
- :class:`components.gpio.gpioz.core.output_devices.Buzzer` - :class:`components.gpio.gpioz.core.output_devices.TonalBuzzer` 
#### Parameters
name | description | default
--- | --- | ---
device |  | 





### register_volume_rgbled_callback


Have a :class:`RGBLED` change it's color according to current volume. LED flashes when minimum or maximum volume is reached.   
Compatible devices:   
- :class:`components.gpio.gpioz.core.output_devices.RGBLED` 
#### Parameters
name | description | default
--- | --- | ---
device |  | 





### decode_card_command


Extension of utils.decode_action with card-specific parameters 
#### Parameters
name | description | default
--- | --- | ---
cfg_rpc_cmd |  | 
logger |  | 





### card_command_to_str


Returns a list of strings with [card_action, ignore_same_id_delay, ignore_card_removal_action]   
The last two parameters are only present, if *long* is True and if they are present in the cfg_rpc_cmd 
#### Parameters
name | description | default
--- | --- | ---
cfg_rpc_cmd |  | 
long |  | False





### card_to_str


Returns a list of strings from card entry command in the format of :func:`card_command_to_str` 
#### Parameters
name | description | default
--- | --- | ---
card_id |  | 
long |  | False





### query_customization







### gui_close







### _gpioz_press_short


Simulate a short press on an input device 
#### Parameters
name | description | default
--- | --- | ---
device |  | 





### _gpioz_press_long


Simulate a long press on an input device. Long means longer than the configured hold_time 
#### Parameters
name | description | default
--- | --- | ---
device |  | 





### _gpioz_rotate_cw


Simulate a clockwise rotation 
#### Parameters
name | description | default
--- | --- | ---
device |  | 





### _gpioz_rotate_ccw


Simulate a counter-clockwise rotation 
#### Parameters
name | description | default
--- | --- | ---
device |  | 





### create_inputs


Add all input devies to the GUI   
:param frame: The TK frame (e.g. LabelFrame) in the main GUI to add the buttons to :return: List of all added GUI buttons 
#### Parameters
name | description | default
--- | --- | ---
frame |  | 
default_btn_width |  | 
default_padx |  | 
default_pady |  | 





### set_state


Change the value of a checkbox state variable 
#### Parameters
name | description | default
--- | --- | ---
value |  | 
box_state_var |  | 





### que_set_state


Queue the action to change a checkbox state variable to the TK GUI main thread 
#### Parameters
name | description | default
--- | --- | ---
value |  | 
box_state_var |  | 





### fix_state


Prevent a checkbox state variable to change on checkbox mouse press 
#### Parameters
name | description | default
--- | --- | ---
box_state_var |  | 





### pbox_set_state


Update progress bar state and related state label 
#### Parameters
name | description | default
--- | --- | ---
value |  | 
pbox_state_var |  | 
label_var |  | 





### que_set_pbox


Queue the action to change the progress bar state to the TK GUI main thread 
#### Parameters
name | description | default
--- | --- | ---
value |  | 
pbox_state_var |  | 
label_var |  | 





### create_outputs


Add all output devices to the GUI   
:param frame: The TK frame (e.g. LabelFrame) in the main GUI to add the representations to :return: List of all added GUI objects 
#### Parameters
name | description | default
--- | --- | ---
frame |  | 
default_btn_width |  | 
default_padx |  | 
default_pady |  | 





### query_customization







### _get_devices


Open all input devices for inspection :return: List of input devices 




### _close_devices


Close listed input devices :param device_list: List of opened input devices to be closed :return: None 
#### Parameters
name | description | default
--- | --- | ---
device_list |  | 





### _is_keyboard


Check if an input device has the keys that are required by a 'normal' keyboard   
Some RFID readers (e.g. KKMoon) and keyboards appear multiple times in the device list with identical names. To differentiate between them, a look at the device capabilities is necessary. One device has normal keyboard keys (this is what we want), the other has only specialized keys.   
:parameter device: an opened evdev.InputDevice to inspect :return: True/False 
#### Parameters
name | description | default
--- | --- | ---
device |  | 





### query_customization







### query_customization







### decode


Decode the RDM6300 data format into actual card ID 
#### Parameters
name | description | default
--- | --- | ---
raw_card_id |  | 
number_format |  | 





### query_customization


Query the user for reader parameter customization   
This function will be called during the configuration/setup phase when the user selects this reader module. It must return all configuration parameters that are necessary to later use the Reader class. You can ask the user for selections and choices. And/or provide default values. If your reader requires absolutely no configuration return {} 




### query_customization







### list_cards


Provide a summarized, decoded list of all card actions   
This is intended as basis for a formatter function   
Format: 'id': {decoded_function_call, ignore_same_id_delay, ignore_card_removal_action, description, from_alias} 




### delete_card


:param auto_save: :param card_id: 
#### Parameters
name | description | default
--- | --- | ---
card_id |  | 
auto_save |  | True





### register_card


Register a new card based on quick-selection   
If you are going to call this through the RPC it will get a little verbose   
**Example:** Registering a new card with ID *0009* for increment volume with a custom argument to inc_volume (*here: 15*) and custom *ignore_same_id_delay value*::   
plugin.call_ignore_errors('cards', 'register_card', args=['0009', 'inc_volume'], kwargs={'args': [15], 'ignore_same_id_delay': True, 'overwrite': True}) 
#### Parameters
name | description | default
--- | --- | ---
card_id |  | 
cmd_alias |  | 
args |  | None
kwargs |  | None
ignore_card_removal_action |  | None
ignore_same_id_delay |  | None
overwrite |  | False
auto_save |  | True





### register_card_custom


Register a new card with full RPC call specification (Not implemented yet) 




### check_card_database







### load_card_database



#### Parameters
name | description | default
--- | --- | ---
filename |  | 





### save_card_database


Store the current card database. If filename is None, it is saved back to the file it was loaded from 
#### Parameters
name | description | default
--- | --- | ---
filename |  | None





### finalize







### atexit







### finalize







### atexit







### reader_install_dependencies


Install dependencies for the selected reader module   
:param reader_path: Path to the reader module :parameter dependency_install: how to handle installing of dependencies 'query': query user (default) 'auto': automatically 'no': don't install dependencies 
#### Parameters
name | description | default
--- | --- | ---
reader_path |  | 
dependency_install |  | 





### reader_load_module


Load the module for the reader_name   
A ModuleNotFoundError is unrecoverable, but we at least want to give some hint how to resolve that to the user All other errors will NOT be handled. Modules that do not load due to compile errors have other problems   
:param reader_name: Name of the reader to load the module for :return: module 
#### Parameters
name | description | default
--- | --- | ---
reader_name |  | 





### _get_reader_descriptions



#### Parameters
name | description | default
--- | --- | ---
reader_dirs |  | 





### query_user_for_reader


Ask the user to select a RFID reader and prompt for the reader's configuration   
This function performs the following steps, to find and present all available readers to the user   
- search for available reader subpackages - dynamically load the description module for each reader subpackage - queries user for selection - if no_dep_install=False, install dependencies as given by requirements.txt and execute setup.inc.sh of subpackage - dynamically load the actual reader module from the reader subpackage - if selected reader has customization options query user for that now - return configuration   
There are checks to make sure we have the right reader modules and they are what we expect. The are as few requirements towards the reader module as possible and everything else is optional (see reader_template for these requirements) However, there is no error handling w.r.t to user input and reader's query_config. Firstly, in this script we cannot gracefully handle an exception that occurs on reader level, and secondly the exception will simply exit the script w/o writing the config to file. No harm done.   
This script expects to reside in the directory with all the reader subpackages, i.e it is part of the rfid-reader package. Otherwise you'll need to adjust sys.path   
:parameter dependency_install: how to handle installing of dependencies 'query': query user (default) 'auto': automatically 'no': don't install dependencies :return: nested dict with entire configuration that can be read into ConfigParser :rtype: dict as {section: {parameter: value}} 
#### Parameters
name | description | default
--- | --- | ---
dependency_install |  | "query"





### write_config


Write configuration to config_file   
:parameter config_file: relative or absolute path to config file :parameter config_dict: nested dict with configuration parameters for ConfigParser consumption :parameter force_overwrite: overwrite existing configuration file without asking 
#### Parameters
name | description | default
--- | --- | ---
config_file |  | 
config_dict |  | 
force_overwrite |  | False





### initialize







### play


Play the jingle using the configured jingle service   
Note: This runs in a separate thread. And this may cause troubles when changing the volume level before and after the sound playback: There is nothing to prevent another thread from changing the volume and sink while playback happens and afterwards we change the volume back to where it was before!   
There is no way around this dilemma except for not running the jingle as a separate thread. Currently (as thread) even the RPC is started before the sound is finished and the volume is reset to normal...   
However: Volume plugin is loaded before jingle and sets the default volume. No interference here. It can now only happen if (a) through the RPC or (b) some other plugin the volume is changed. Okay, now (a) let's hope that there is enough delay in the user requesting a volume change (b) let's hope no other plugin wants to do that (c) no bluetooth device connects during this time (and pulseaudio control is set to toggle_on_connect) and take our changes with the threaded approach. 
#### Parameters
name | description | default
--- | --- | ---
filename |  | 





### play_startup


Play the startup sound (using jingle.play) 




### play_shutdown


Play the shutdown sound (using jingle.play) 




### finalize







### atexit



#### Parameters
name | description | default
--- | --- | ---
signal_id |  | 





### initialize







### initialize







### interpolate



#### Parameters
name | description | default
--- | --- | ---
cc |  | 
input |  | 





### finalize







### atexit







### finalize







### atexit







### shutdown







### stop_player







### finalize







### atexit







### clamp



#### Parameters
name | description | default
--- | --- | ---
n |  | 
minn |  | 
maxn |  | 





### parse_config







### initialize







### finalize







### atexit







### shutdown


Shutdown the host machine 




### reboot


Reboot the host machine 




### jukebox_is_service


Check if current Jukebox process is running as a service 




### is_any_jukebox_service_active


Check if a Jukebox service is running   
.. note:: Does not have the be the current app, that is running as a service! 




### restart_service


Restart Jukebox App if running as a service 




### get_disk_usage


Return the disk usage in Megabytes as dictionary for RPC export 
#### Parameters
name | description | default
--- | --- | ---
path |  | "/"





### get_cpu_temperature


Get the CPU temperature with single decimal point   
No error handling: this is expected to take place up-level! 




### publish_cpu_temperature







### get_ip_address


Get the IP address 




### say_my_ip



#### Parameters
name | description | default
--- | --- | ---
option |  | "full"





### wlan_disable_power_down


Turn off power management of wlan. Keep RPi reachable via WLAN   
This must be done after every reboot card=None takes card from configuration file 
#### Parameters
name | description | default
--- | --- | ---
card |  | None





### get_autohotspot_status


Get the status of the auto hotspot feature 




### stop_autohotspot


Stop auto hotspot functionality   
Basically disabling the cronjob and running the script one last time manually 




### start_autohotspot


start auto hotspot functionality   
Basically enabling the cronjob and running the script one time manually 




### initialize







### finalize







### atexit







### _get_music_library_path


Parse the music directory from the mpd.conf file 
#### Parameters
name | description | default
--- | --- | ---
conf_file |  | 





### get_music_library_path


Get the music library path 




### clean_foldername



#### Parameters
name | description | default
--- | --- | ---
lib_path |  | 
folder |  | 





### ensure_trailing_slash



#### Parameters
name | description | default
--- | --- | ---
path |  | 





### remove_trailing_slash



#### Parameters
name | description | default
--- | --- | ---
path |  | 





### remove_leading_slash



#### Parameters
name | description | default
--- | --- | ---
path |  | 





### initialize







### atexit







### initialize






