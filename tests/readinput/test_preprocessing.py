#!/usr/bin/env python

# To add <package> to PYTHONPATH
# https://stackoverflow.com/a/34938623
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../src")

import unittest
from pypipeviewer.readinput import preprocessing

class TestMainLoop(unittest.TestCase):

    def test_input_pre_processing(self):
        self.assertTrue(preprocessing.catch_exit_condition(":q"))
        self.assertTrue(preprocessing.catch_exit_condition(";q"))
        self.assertTrue(preprocessing.catch_exit_condition("=q"))

if __name__ == '__main__':
    unittest.main()