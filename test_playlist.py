import unittest
import sys
import os
from csv_playlist import database_of_songs
import csv_playlist
import pycodestyle

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestInput(unittest.TestCase):

    # test valid inputs
    def test_correct_values(self):
        self.assertEqual(database_of_songs("vasco rossi", "vivere"),
                         print("you have added this song to your playlist"))

    # test invalid inputs
    def test_wrong_values(self):
        # here some wrong data
        self.assertEqual(database_of_songs("Ada Lovelae", "none"), print(
            "you have added this song to your playlist"))
        self.assertEqual(database_of_songs("gross", "live"), print(
            "you have added this song to your playlist"))

    # test corner cases
    def test_empty_string(self):
        # here an example if nothing is inserted
        self.assertEqual(database_of_songs(" ", " "), print(
            "you have added this song to your playlist"))


if __name__ == '__main__':

    unittest.main(verbosity=2)
