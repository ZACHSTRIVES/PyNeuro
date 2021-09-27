from PyNeuro import PyNeuro


def callback(value):
    print("callback:", value)


pn = PyNeuro()

pn.connect()
pn.set_meditation_callback(callback)
pn.start()
