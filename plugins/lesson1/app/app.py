'''

Start reading at Line 46: if __name__ == '__main__':

Do the following as an exercise:

    - Create a new file called "plugin_\w+.py" where
      \w+ is any word you want to call it.

    - Similar to plugin_example.py, create a function
      called plugin_main that takes the same args and
      make it print something based on the args.

    - Change the first arg of line 56 in this file below 
      (which currently says 'example') to the word you chose
      for the file name of your plugin.

    - Now, when you run this file using "python app.py", your
      plugin should be dynamically imported and it's
      "plugin_main" function should be called.

'''


def load_plugin(name):
    '''
    This function imports a plugin based on the name
    argument being passed in.
    '''

    plugin = __import__('plugin_%s' % name)
    return plugin

def call_plugin(name, *args, **kwargs):
    '''
    This function loads a plugin based on the first argument
    and passes the rest of the arguments to the plugin.

    It assumes each plugin has a method called "plugin_main"
    as that will be the method that executes.
    '''

    plugin = load_plugin(name)
    plugin.plugin_main(*args, **kwargs)

if __name__ == '__main__':

    '''
    This is the entry point. It's calling the plugin example
    which is being imported from the plugin_example.py file
    because of the first arg being passed. The rest of the
    args are passed to the plugin, and because of the use of
    args and kwargs, any number of arguments can be passed.
    '''

    call_plugin('example','arg1','arg2','arg3')
