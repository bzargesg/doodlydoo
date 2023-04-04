import unittest
from typing import List
from main import find_largest_int

class TestLargestInt(unittest.TestCase):
    
    def test_find_largest_int(self):
        print("testing")
        self.assertEqual(find_largest_int([1, 5, 3, 9, 2]), 9)
        self.assertEqual(find_largest_int([-3, -5, -1]), -1)
        self.assertEqual(find_largest_int([10]), 10)
        self.assertEqual(find_largest_int([0, 0, 0, 0]), 0)

if __name__ == '__main__':
    unittest.main()