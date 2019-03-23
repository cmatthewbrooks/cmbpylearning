import argparse

from plugins.plugin_a import PluginA
from plugins.plugin_b import PluginB



class App:
    
    def __init__(self, plugins = [], command = '', *args):
        self._plugins = plugins
        self.command = command

    def run(self):
        
        modules_to_execute = self._plugins

        for module in modules_to_execute:

            print('Executing %s' % module)
            getattr(module, self.command)()



if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help='Commands')


    parser_domain = subparsers.add_parser('domain')
    parser_domain.set_defaults(command = 'domain')

    parser_ip = subparsers.add_parser('ip')
    parser_ip.set_defaults(command = 'ip')


    args = parser.parse_args()


    app = App(plugins=[PluginA(),PluginB()], command=args.command)
    app.run()
