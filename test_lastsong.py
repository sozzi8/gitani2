from csv_file import write_data
from lyrics import get_lyric
from lastSong import read_data
import pandas as pd
import unittest
import sys
import os
import pycodestyle


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestInput(unittest.TestCase):

    # test valid inputs
    def test_correct_values_last(self):
        artisttest9 = "Vasco Rossi"
        titletest9 = "Vivere"
        canzone = get_lyric(artisttest9, titletest9)
        self.assertEqual(write_data("test.csv", artisttest9,
                         titletest9, canzone),
                         write_data("test.csv",
                         artisttest9, titletest9, canzone))

    # test with non existent file
    def test_with_nonexistent_file(self):
        path = "NONE.csv"
        self.assertEqual(read_data(path), print('The file does not exist'))

    # test with wrong encoding
    def test_with_wrongencoding(self):
        path = "reader.csv"
        self.assertEqual(read_data(path), print('File has a wrong encoding'))


if __name__ == '__main__':

    unittest.main(verbosity=2)
