#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 7]), 7)

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_all_negative(self):
        self.assertEqual(max_integer([-10, -20, -3, -40]), -3)

    def test_mixed_positive_negative(self):
        self.assertEqual(max_integer([-10, 0, 10, -20]), 10)

    def test_with_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_int_and_float(self):
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_list_of_strings_raises(self):
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])

    def test_list_with_none_raises(self):
        with self.assertRaises(TypeError):
            max_integer([None, 1, 2])

if __name__ == '__main__':
    unittest.main()
