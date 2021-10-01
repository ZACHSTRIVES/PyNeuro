PyNeuro
=======

PyNeuro is designed to connect NeuroSky's MindWave EEG device to Python
and provide Callback functionality to provide data to your application
in real time. The library is tested with Mindwave Mobie2 Headset, and
runs stably.

Installation
------------

Run the following command: ``pip install PyNeuro``

Usage
-----
1. Before you start, make sure you have downloaded `Nuerosky Mindware Developer Tools <https://store.neurosky.com/collections/developer-tools>`__  and turned on Thinkgear Connecter. Please keep Thinkgear Connecter on while the program is running.
2. Importing the module: ``from PyNeuro.PyNeuro import PyNeuro``
3. Initializing: ``pn = PyNeuro()``
4. After initializing, if required the callbacks can be set
5. Then call ``pn.connect()`` method, it will connect with TCP Socket
   server.
6. Then call ``pn.start()`` method, it will be start fetching data.
7. To stop call ``pn.close()``

Obtaining Data from Device
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Obtaining value:** ``attention = pn.attention`` #to get value of
   attention\_ >\ **Other Variable** attention, meditation,
   blinkStrength, delta, theta, lowAlpha, highAlpha, lowBeta, highBeta, lowGamma, highGamma.

-  **Setting callback:** A call back can be associated with all the
   above variables so that a function is called when the variable is
   updated. Syntax:

   ::

       pn.set_attention_callback(callback_function1)
       pn.set_meditation_callback(callback_function2)
       pn.set_blinkStrength_callback(callback_function3)
       ....

       You can add any number of callback functions to a variable..

Access via callback
--------------------------------------

.. code:: python

    from PyNeuro.PyNeuro import PyNeuro
    from time import sleep

    pn = PyNeuro() 

    def attention_callback(attention_value):
        """this function will be called everytime NeuroPy has a new value for attention"""
        print ("Value of attention is: ", attention_value)
        return None

    pn.set_attention_callback("attention", attention_callback)
    pn.connect()
    pn.start()



Access via object
------------------------------------

.. code:: python

    from PyNeuro.PyNeuro import PyNeuro
    from time import sleep

    pn = PyNeuro() 
    pn.start()

    while True:
        if pn.meditation > 70: # Access data through object
            pn.close() 
        sleep(0.2) 

Python Compatibility
--------------------

-  `Python <http://www.python.com>`__ -v3.\*

Reference
~~~~~~~~~

`lihas/NeuroPy <https://github.com/lihas/NeuroPy>`__ - A library based
on native Bluetooth serial connection
