'''
This is a simple plugin that prints
all the arguments passed to it.
'''

def plugin_main(*args, **kwargs):
    print(args, kwargs)
