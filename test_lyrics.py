from lyrics import get_lyric
import unittest
import sys
import os
import pycodestyle


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestInput(unittest.TestCase):

    # test valid inputs
    def test_correct_values(self):
        artisttest = "Vasco Rossi"
        titletest = "Vivere"
        self.assertEqual(get_lyric(artisttest, titletest),
                         get_lyric("Vasco Rossi", "Vivere"))

    # test invalid inputs
    def test_wrong_values(self):
        artisttest = "Vasco Rossi"
        titletest = "Vivvvere"
        artisttest2 = "Vasso Rose"
        titletest2 = "Vivere"
        # here some wrong data
        self.assertRaises(KeyError, get_lyric, artisttest, titletest)
        self.assertRaises(KeyError, get_lyric, artisttest2, titletest2)

    # test corner cases
    def test_empty_string(self):
        # here an example if nothing is inserted
        self.assertRaises(KeyError, get_lyric, "-", "Vivere")
        self.assertRaises(KeyError, get_lyric, " ", "Vivere")


if __name__ == '__main__':

    unittest.main(verbosity=2)
