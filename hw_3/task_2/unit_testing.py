import unittest
from num_interval import numberInterval

class Testing(unittest.TestCase):
    def test_in_interval(self):
        self.assertTrue(numberInterval(58))

    def test_out_interval(self):
        self.assertFalse(numberInterval(10))