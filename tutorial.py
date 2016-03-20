""" Gabbi Examples - 
** Usage **
Run with ``python -m unittest -v webapp`` or directly with python samples.py
"""

import os
import sys
from gabbi import driver

TEST_DIR = __file__.split('.')[0] # Take tests from the folder matching this file, i.e. were running from TEST_DIR.py

def load_tests(loader, tests, pattern):
    """Provide a TestSuite to the discovery process.
    """
    test_dir = os.path.join(os.path.dirname(__file__), TEST_DIR)
    # Use localhost as the host paramerter, this is requried but never used
    return driver.build_tests(test_dir, loader,
    	host="127.0.0.1")

if __name__ == "__main__":
	# Call the unitestdiscovery
    import unittest
    unittest.main()