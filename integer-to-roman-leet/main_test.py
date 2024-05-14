import unittest

import main

class TestIntegerToRoman(unittest.TestCase):

    def setUp(self):
        self.sol = main.Solution()

    def test_56(self):
        self.assertEqual(self.sol.intToRoman(56), 'LVI')

    def test_54(self):
        self.assertEqual(self.sol.intToRoman(54), 'LIV')

    def test_1994(self):
        self.assertEqual(self.sol.intToRoman(1994), 'MCMXCIV')

    def test_58(self):
        self.assertEqual(self.sol.intToRoman(58), 'LVIII')

    def test_3749(self):
        self.assertEqual(self.sol.intToRoman(3749), 'MMMDCCXLIX')

    def test_3(self):
        self.assertEqual(self.sol.intToRoman(3), 'III')

    def test_4(self):
        self.assertEqual(self.sol.intToRoman(4), 'IV')

    def test_99(self):
        self.assertEqual(self.sol.intToRoman(99), 'XCIX')

    def test_0(self):
        self.assertEqual(self.sol.intToRoman(0), '')

    def test_1(self):
        self.assertEqual(self.sol.intToRoman(1), 'I')

if __name__ == '__main__':
    unittest.main()
