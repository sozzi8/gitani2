import unittest
import sys
import os
from csv_playlist import database_of_songs
import csv_playlist
#from lyrics import get_lyric


# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestInput(unittest.TestCase):

    # smoke test: valid inputs
    def test_correct_values(self):
        # you should select some valid inputs, for which the output is known
        self.assertEqual(database_of_songs("vasco rossi", "vivere"),
                         print("you have added this song to your playlist"))

    # invalid inputs
    def test_wrong_values(self):
        # you should input wrong data
        self.assertEqual(database_of_songs("Ada Lovelae", "none"), print(
            "you have added this song to your playlist"))
        self.assertEqual(database_of_songs("gross", "live"), print(
            "you have added this song to your playlist"))

        # NOTE: the following test passing an empty list will fail!
        # self.assertEqual(database_of_songs([]), None)

    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(database_of_songs(" ", " "), print(
            "you have added this song to your playlist"))


if __name__ == '__main__':

    # basic test
    # unittest.main()

    # with more details
    unittest.main(verbosity=2)
