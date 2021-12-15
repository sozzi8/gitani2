import unittest
import sys
import os

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lyrics import get_lyric

from csv_file import write_data
class TestInput(unittest.TestCase):
        def test_correct_values_last(self):
            artisttest9= "Vasco Rossi"
            titletest9= "Vivere"
            marta = get_lyric(artisttest9, titletest9)



            # you should select some valid inputs, for which the output is known
            self.assertEqual( write_data(artisttest9, titletest9,marta ), write_data(artisttest9, titletest9,marta))




if __name__ == '__main__':

        # basic test
        #unittest.main()

        # with more details
    unittest.main(verbosity=2)
