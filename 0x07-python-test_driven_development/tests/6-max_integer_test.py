#!/usr/bin/python3

"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):

        # Test case for a list with one element
        self.assertEqual(max_integer([1]), 1)
        
        # Test case for a list with multiple elements
        self.assertEqual(max_integer([1, 2, 3]), 3)
        
        # Test case for a list with negative numbers
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        
        # Test case for a list with all the same number
        self.assertEqual(max_integer([5, 5, 5]), 5)
        
        # Test case for an empty list
        self.assertEqual(max_integer([]), None)
        
        # Test case for a list with all negative numbers
        self.assertEqual(max_integer([-5, -8, -1]), -1)
        
        # Test case for a list with a mix of positive and negative numbers
        self.assertEqual(max_integer([1, -5, 8, -3, 9]), 9)
        
        # Test case for a list with one positive number and one negative number
        self.assertEqual(max_integer([-5, 8]), 8)
        
        # Test case for a list with one positive number and one negative number, where the negative number is larger
        self.assertEqual(max_integer([-5, -8]), -5)

if __name__ == '__main__':
    unittest.main()

