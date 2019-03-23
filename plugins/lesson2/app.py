class MyTestPluginApplication:
    
    def __init__(self, plugins = [], *args):
        self._plugins = plugins

    def run(self):
        
        print('Starting application')
        print('-' * 79)

        modules_to_execute = self._plugins

        for module in modules_to_execute:
            print('Executing %s' % module)
            module.process()

        print('-' * 79)
        print('Starting application...DONE')
