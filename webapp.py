"""Test Loader
python -m unittest -v webapp
"""

import os
import sys
from gabbi import driver

name = __file__.split('.')[0]

import ConfigParser
config = ConfigParser.ConfigParser()
config.read('%s.ini' % name) # Load the settings.ini file

default = config.get('Tests','default')
data = dict(config.items(default))

def load_tests(loader, tests, pattern):
    """Provide a TestSuite to the discovery process."""
    
    test_dir = os.path.join(os.path.dirname(__file__), name)
    return driver.build_tests(test_dir, loader,
                              host=data['host'],
                              port=data['port'],
                              prefix=data['prefix'],
                              fixture_module=fixtures)

