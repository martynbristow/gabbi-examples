"""Test Loader
python -m unittest -v webapp
"""

import os
import sys
from gabbi import driver

TESTS_DIR = 'samples'

def load_tests(loader, tests, pattern):
    """Provide a TestSuite to the discovery process.
    """
    
    test_dir = os.path.join(os.path.dirname(__file__), TESTS_DIR)
    return driver.build_tests(test_dir, loader,
    	host="127.0.0.1")

if __name__ == "__main__":
    import unittest
    unittest.main()