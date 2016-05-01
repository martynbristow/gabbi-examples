""" Webapp
"""

import os
import sys
from gabbi import driver
import ConfigParser

settings = 'settings.ini'
name = __file__.split('.')[0]

config = ConfigParser.ConfigParser()
config.read('%s' % settings)

#default = config.get('Server', 'default')
default="Server"
data = dict(config.items(default))

def load_tests(loader, tests, pattern):
    """Provide a TestSuite to the discovery process
    """
    
    test_dir = os.path.join(os.path.dirname(__file__), name)
    return driver.build_tests(test_dir, loader,
                              host=data['host'],
                              port=data['port'],
                              prefix=data['prefix'],
                              fixture_module=fixtures)

