import unittest
from main import is_palindrome


class TestReverseString(unittest.TestCase):

    def test_is_palindrome(self):
        assert is_palindrome('racecar') == True
        assert is_palindrome('level') == True
        assert is_palindrome('python') == False
        assert is_palindrome('') == True
        assert is_palindrome('racebcar') == False

if __name__ == '__main__':
    unittest.main()