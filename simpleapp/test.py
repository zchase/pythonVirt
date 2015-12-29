#!/usr/bin/env python

import unittest
from simpleapp import hello_world

class HelloWorldTestCase(unittest.TestCase):
    """Tests for `simpleapp.py`."""

    def test_is_output_hw(self):
        """Is the output of your Python Application what you expect?"""
        self.assertTrue(hello_world() == "Hello World from Distelli!")

if __name__ == '__main__':
    unittest.main()