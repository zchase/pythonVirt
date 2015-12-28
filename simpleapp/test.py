#!/usr/bin/env python

import unittest
from simpleapp import hello_world

class PrimesTestCase(unittest.TestCase):
    """Tests for `simpleapp.py`."""

    def test_is_output_hw(self):
        """Is the output of your Python Application what you expect?"""
        self.assertTrue(hello_world() == "<h1>Hello World from an updated and redeployed Python Application!</h1>")

if __name__ == '__main__':
    unittest.main()