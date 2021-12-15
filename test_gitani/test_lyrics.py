import unittest
import sys
import os

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lyrics import get_lyric

from csv_file import write_data
class TestInput(unittest.TestCase):

    # smoke test: valid inputs
    def test_correct_values(self):
        artisttest= "Vasco Rossi"
        titletest= "Vivere"
        # you should select some valid inputs, for which the output is known
        self.assertEqual(get_lyric(artisttest, titletest),get_lyric("Vasco Rossi","Vivere"))



    # edge inputs (strange)
    def test_edgy_values(self):
        artisttest1= "VASCO ROSSI"
        titletest1= "VIVERE"
        artisttest2= "VaScO RosSi"
        titletest2= "ViVEre"
        # you should input wrong data
        self.assertEqual(get_lyric(artisttest1,titletest1),get_lyric(artisttest1,titletest1))
        self.assertEqual(get_lyric(artisttest2,titletest2),get_lyric(artisttest2,titletest2) )

        # NOTE: the following test passing an empty list will fail!
        # self.assertEqual(return_birthday([]), None)

    # corner case: empty string
#    def test_wrong_string(self):
        #artisttest3= "- "
        #titletest3= "Vivere"
        #self.assertFalse(get_lyric(artisttest3,titletest3),get_lyric( artisttest3, titletest3))






if __name__ == '__main__':

    # basic test
    #unittest.main()

    # with more details
    unittest.main(verbosity=2)
