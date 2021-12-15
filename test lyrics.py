import unittest
import sys
import os

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lyrics import get_lyric


class TestInput(unittest.TestCase):

    # smoke test: valid inputs
    def test_correct_values(self):
        artisttest= "Vasco Rossi"
        titletest= "Vivere"
        # you should select some valid inputs, for which the output is known
        self.assertEqual(get_lyric(artisttest, titletest),get_lyric("Vasco Rossi","Vivere"))

    # invalid inputs
    def test_wrong_values(self):
        artisttest= "Vasco Rossi"
        titletest= "Vivvvere"
        artisttest2= "Vasso Rose"
        titletest2= "Vivere"
        # you should input wrong data
        self.assertTrue(get_lyric(artisttest,titletest),get_lyric(artisttest,titletest))
        self.assertTrue(get_lyric(artisttest2,titletest2),get_lyric(artisttest2,titletest2) )

        # NOTE: the following test passing an empty list will fail!
        # self.assertEqual(return_birthday([]), None)

    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(get_lyric("-", "Vivere"),get_lyric("", "Vivere"))


if __name__ == '__main__':

    # basic test
    #unittest.main()

    # with more details
    unittest.main(verbosity=2)
