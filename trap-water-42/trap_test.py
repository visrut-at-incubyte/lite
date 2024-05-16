import unittest

import trap

class TestIntegerToRoman(unittest.TestCase):

    def setUp(self):
        self.sol = trap.Solution()

    def test_example1(self):
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        self.assertEqual(self.sol.trap(height), 6)

    def test_example2(self):
        height = [5, 0, 1, 2, 3]
        self.assertEqual(self.sol.trap(height), 6)

    def test_example3(self):
        height = [4,2,0,3,2,5]
        self.assertEqual(self.sol.trap(height), 9)

    def test_example4(self):
        height = [5,5,1,7,1,1,5,2,7,6]
        self.assertEqual(self.sol.trap(height), 23)

    def test_example5(self):
        height = [3,1,2,4,0,1,3,2]
        self.assertEqual(self.sol.trap(height), 8)

if __name__ == '__main__':
    unittest.main()