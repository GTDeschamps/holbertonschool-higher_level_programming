#!/usr/bin/python3
"""Module for testing max integer condition in a list
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class test_max_integer(unittest.TestCase):
    """definition class test_max_integer for test"""

    def test_max_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max__neg(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_max_int_empty_list(self):
        self.assertEqual(max_integer(), None)

    def test_str_fail(self):
        numbers = ["charlot", 4]
        with self.assertRaises(TypeError):
            max_value = max_integer(numbers)
