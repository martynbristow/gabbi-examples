""" UnitTests for the SimpleHTTPServer
"""
import mock
import unittest

class TestHTTPServerHandler(unittest.TestCase):
    """
    """
    def setUp(self):
        self.handler = mock.Mock()
    def test_do_GET(self):
        pass
    def test_do_POST(self):
        pass
    def tearDown(self):
        self.handler()

if __name__ == "__main__":
    unittest.main()