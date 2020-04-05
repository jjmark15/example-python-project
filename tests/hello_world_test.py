import unittest
from cool_package.app import hello_world


class TestApp(unittest.TestCase):
    def test_hello_world_says_hello_world(self):
        self.assertEqual("Hello World!", hello_world())
