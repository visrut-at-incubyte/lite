import unittest

import candy

class TestIntegerToRoman(unittest.TestCase):

    def setUp(self):
        self.sol = candy.Solution()

    def test_102(self):
        self.assertEqual(self.sol.candy([1,0,2]), 5)

    def test_1(self):
        self.assertEqual(self.sol.candy([1]), 1)

    def test_12(self):
        self.assertEqual(self.sol.candy([1, 2]), 3)

    def test_21(self):
        self.assertEqual(self.sol.candy([2, 1]), 3)

    def test_121(self):
        self.assertEqual(self.sol.candy([1, 2, 1]), 4)

    def test_12221(self):
        self.assertEqual(self.sol.candy([1, 2, 2, 2, 1]), 7)

    def test_211122(self):
        self.assertEqual(self.sol.candy([2, 1, 1, 1, 2, 2]), 8)
    
    def test_122(self):
        self.assertEqual(self.sol.candy([1, 2, 2]), 4)

    def test_123454321(self):
        self.assertEqual(self.sol.candy([1,2,3,4,5,4,3,2,1]), 25)

    def test_111112345432123111012345111111(self):
        self.assertEqual(self.sol.candy([1,1,1,1,1,2,3,4,5,4,3,2,1,1,1,0,1,2,3,4,5,1,1,1,1,1,1,10]), 61)
