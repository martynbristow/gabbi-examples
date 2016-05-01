""" API Tests
Test a JSON API
"""

import os
import sys
import ConfigParser
from gabbi import driver

settings = 'settings.ini'
name = __file__.split('.')[0]

config = ConfigParser.ConfigParser()
config.read('%s' % settings)
print config.sections()
#default = config.get('Server','default')
default="Server"
data = dict(config.items(default))

def load_tests(loader, tests, pattern):
    """Provide a TestSuite to the discovery process."""
    
    test_dir = os.path.join(os.path.dirname(__file__), name)
    return driver.build_tests(test_dir, loader,
                              host=data['host'],
                              port=data['port'],
                              prefix=data['prefix'],
                              fixture_module=fixtures)

