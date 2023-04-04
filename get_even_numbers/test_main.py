import unittest
from main import get_even_numbers


class TestGetEvenNumbers(unittest.TestCase):
    def test_get_even_numbers(self):
        # Test case where all numbers are even
        nums1 = [2, 4, 6, 8, 10]
        expected_output1 = [2, 4, 6, 8, 10]
        self.assertEqual(get_even_numbers(nums1), expected_output1)
        
        # Test case where no numbers are even
        nums2 = [1, 3, 5, 7, 9]
        expected_output2 = []
        self.assertEqual(get_even_numbers(nums2), expected_output2)
        
        # Test case where some numbers are even
        nums3 = [1, 2, 3, 4, 5, 6]
        expected_output3 = [2, 4, 6]
        self.assertEqual(get_even_numbers(nums3), expected_output3)
        
        # Test case where all numbers are odd
        nums4 = [7, 11, 13, 15, 19]
        expected_output4 = []
        self.assertEqual(get_even_numbers(nums4), expected_output4)


if __name__ == '__main__':
    unittest.main()