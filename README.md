# PyNeuro

PyNeuro is designed to connect NeuroSky's MindWave EEG device to Python and provide Callback functionality to provide data to your application in real time.
The library is tested with Mindwave Mobie2 Headset, and runs stably.

## Installation

Run the following command: `pip install PyNeuro`

## Usage
1. Before you start, make sure you have downloaded [Nuerosky Mindware Developer Tools](https://store.neurosky.com/collections/developer-tools) and turned on Thinkgear Connecter. Please keep Thinkgear Connecter on while the program is running.
2. Importing the module: `from PyNeuro.PyNeuro import PyNeuro`
3. Initializing: `pn = PyNeuro()`
4. After initializing, if required the callbacks can be set
5. Then call `pn.connect()` method, it will connect with TCP Socket server.
6. Then call `pn.start()` method, it will be start fetching data.
7. To stop call `pn.close()`

### Obtaining Data from Mindware Mobile Headset

* **Obtaining value:** `attention = pn.attention` \#to get value of attention_
    >**Other Variables** attention, meditation, blinkStrength, delta, lowAlpha, highAlpha, lowBeta, highBeta, lowGamma, highGamma.

* **Setting callback:** A call back can be associated with all the above variables so that a function is called when the variable is updated. Syntax: 

    ```
    pn.set_attention_callback(callback_function1)
    pn.set_meditation_callback(callback_function2)
    pn.set_blinkStrength_callback(callback_function3)
    pn.set_delta_callback(callback_function4)
    pn.set_theta_callback(callback_function5)
    ....
  
    ``` 
   >You can add any number of callback functions to a variable..
  

## Access data via callback

```python
from PyNeuro.PyNeuro import PyNeuro
from time import sleep

pn = PyNeuro() 

def attention_callback(value):
    """this function will be called everytime PyNeuro has a new value for attention"""
    print ("attention: ", value)

pn.set_attention_callback("attention", attention_callback)
pn.connect()
pn.start()

```


## Access data via object

```python
from PyNeuro.PyNeuro import PyNeuro
from time import sleep

pn = PyNeuro() 
pn.start()

while True:
    if pn.theta > 70: # Access data through object
        pn.close() 
    sleep(0.2) 
```

## Python Compatibility

* [Python](http://www.python.com) -v3.*


### Reference
[lihas/NeuroPy](https://github.com/lihas/NeuroPy) - A library based on native Bluetooth serial connection
