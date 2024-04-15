import unittest
import Calc_functions

# Inheriting TestCase from unittest module
class TestCalcFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calc_functions.add(10,5), 15)
        self.assertEqual(Calc_functions.add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
