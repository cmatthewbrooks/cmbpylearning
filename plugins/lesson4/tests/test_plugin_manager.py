import unittest

from context import PluginManager

class TestPluginManager(unittest.TestCase):

    def test_get_all_plugins(self):

        plugins = PluginManager._get_all_plugins()

        



if __name__ == '__main__':
    unittest.main()
