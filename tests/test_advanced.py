# -*- coding: utf-8 -*-

from .context import py_yaml_util

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(py_yaml_util.main())


if __name__ == '__main__':
    unittest.main()
