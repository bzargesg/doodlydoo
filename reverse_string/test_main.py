import unittest
from main import reverse_string


class TestReverseString(unittest.TestCase):

    def test_reverse_string(self):
        assert reverse_string('hello') == 'olleh'
        assert reverse_string('world') == 'dlrow'
        assert reverse_string('Python') == 'nohtyP'
        assert reverse_string('') == ''

if __name__ == '__main__':
    unittest.main()