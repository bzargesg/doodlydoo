import unittest
from main import is_anagram


class TestReverseString(unittest.TestCase):

    def test_is_anagram(self):
        assert is_anagram('listen', 'silent') == True
        assert is_anagram('abc', 'def') == False
        assert is_anagram('debit card', 'bad credit') == True
        assert is_anagram('', '') == True

if __name__ == '__main__':
    unittest.main()