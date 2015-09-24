#!/usr/bin/env python

"""Regression testing framework

Borrowed from http://www.diveintopython.org/

This module will search for scripts in the same directory named
XYZtest.py.  Each such script should be a test suite that tests a
module through PyUnit.  (As of Python 2.1, PyUnit is included in
the standard library as "unittest".)  This script will aggregate all
found test suites into one big test suite and run them all at once.

* Modified to use os.path.walk to find all the test scripts
* Modified to find all python scripts, not just ones of the form *test.py
"""
import sys
import os.path
import unittest


# ensure that the module in this directory is used instead of the system one
# or else we would be testing the system one and not the one with the
# changes :)
import sys
sys.path.insert(0, os.path.abspath('lib'))
print ("System path is: " + str(sys.path))


if __name__ == '__main__':
    unittest.main("tests", verbosity=1)
