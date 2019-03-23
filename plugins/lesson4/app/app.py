import os
import sys
import json
import inspect
import argparse

from plugins.a import PluginA
from plugins.b import PluginB



class App:
    
    def __init__(self, plugins = None, command = None, *args):
        
        self.config_manager = ConfigManager()

        self.plugin_manager = PluginManager(plugins)
        self._plugins = self.plugin_manager.active_plugins

        self.command = command

    def run(self):

        for plugin in self._plugins:

            print('Executing %s' % plugin)
            getattr(plugin, self.command)()



class PluginManager:
    
    PLUGINDIRECTORY = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'plugins')
    )

    def __init__(self, plugins):
        
        #self.active_plugins = [PluginA(), PluginB()]
        self.active_plugins = None

        if not plugins:
            self.active_plugins = self._get_all_plugins()


    def _get_all_plugins(self):

        all_plugins = []

        plugin_files = [f for f in os.listdir(PluginManager.PLUGINDIRECTORY) 
            if os.isfile(join(PluginManager.PLUGINDIRECTORY, f))
        ]

        for plugin in plugin_files:
            
            module = __import__(plugin)


        return all_plugins


class ConfigManager:

    def __init__(self):

        self.config_data = None

        with open('config.json') as json_config_file:
            
            self.config_data = json.load(json_config_file)



if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-p','--plugins', default=None)

    subparsers = parser.add_subparsers(help='Commands')


    parser_domain = subparsers.add_parser('domain')
    parser_domain.set_defaults(command = 'domain')

    parser_ip = subparsers.add_parser('ip')
    parser_ip.set_defaults(command = 'ip')


    args = parser.parse_args()


    app = App(plugins=args.plugins, command=args.command)
    app.run()
