def add_numbers(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b
 
 import unittest

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-1, -1), -2)

    def test_add_positive_and_negative(self):
        self.assertEqual(add_numbers(5, -3), 2)

    def test_add_zeros(self):
        self.assertEqual(add_numbers(0, 0), 0)

    def test_add_floats(self):
        self.assertAlmostEqual(add_numbers(2.5, 3.1), 5.6)
