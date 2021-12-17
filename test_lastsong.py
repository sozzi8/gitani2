from csv_file import write_data
from lyrics import get_lyric
from lastSong import read_data
import pandas as pd
import unittest
import sys
import os

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestInput(unittest.TestCase):

    def test_correct_values_last(self):
        artisttest9 = "Vasco Rossi"
        titletest9 = "Vivere"
        marta = get_lyric(artisttest9, titletest9)
        # you should select some valid inputs, for which the output is known
        self.assertEqual(write_data("test.csv", artisttest9, titletest9, marta),
                         write_data("test.csv", artisttest9, titletest9, marta))

    def test_with_nonexistent_file(self):
        path = "NONE.csv"
        self.assertEqual(read_data(path), print('The file does not exist'))

    def test_with_wrongencoding(self):
        path = "reader.csv"
        self.assertEqual(read_data(path), print('File has a wrong encoding'))


if __name__ == '__main__':

    unittest.main(verbosity=2)
