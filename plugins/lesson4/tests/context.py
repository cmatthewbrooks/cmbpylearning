# This idea was taken from:
# https://docs.python-guide.org/writing/structure/ 

import os,sys

sys.path.append( 
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from app.app import App as App
from app.app import PluginManager as PluginManager
from app.app import ConfigManager as ConfigManager
