#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))
        def test_valid_min(self):
                self.assertEqual(calc(1, 1), 1)

        def test_valid_max(self):
                self.assertEqual(calc(999, 999), 998001)


        def test_boundary_min(self):
                self.assertEqual(calc(1, 500), 500)
    
        def test_boundary_max(self):
                self.assertEqual(calc(999, 500), 499500)

 
        def test_out_of_range_lower(self):
                self.assertEqual(calc(0, 100), -1)
    
        def test_out_of_range_upper(self):
                self.assertEqual(calc(1000, 100), -1)

    
        def test_decimal_input(self):
                self.assertEqual(calc(0.1, 999), -1)

        def test_string_input(self):
                self.assertEqual(calc("abc", 100), -1)

        def test_none_input(self):
                self.assertEqual(calc(None, 2), -1)

        if __name__ == '__main__':
                unittest.main()

