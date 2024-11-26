import unittest
from even_odd_num import evenOddNum


class Testing(unittest.TestCase):
    def test_even_num(self):
        self.assertTrue(evenOddNum(4))

    def test_odd_num(self):
        self.assertFalse(evenOddNum(5))
