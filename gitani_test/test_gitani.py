import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lyrics import get_lyric

class insert_values(unittest.TestCase):

    # smoke test: valid inputs
    def test_correct_values(self):
        # you should select some valid inputs, for which the output is known

        self.assertEqual(get_lyric("vasco rossi" "vivere"), song)

    # invalid inputs
    def test_wrong_values(self):
        # you should input wrong data
        self.assertEqual(return_birthday("Ada Lovelae"), None)
        self.assertEqual(return_birthday(7), None)

        # NOTE: the following test passing an empty list will fail!
        # self.assertEqual(return_birthday([]), None)

    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(return_birthday(""), None)


if __name__ == '__main__':
