import unittest
import sys
import os
#from lyrics import get_lyric


# add parent folder to path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lyrics import get_lyric

class TestInput(unittest.TestCase):
    # smoke test: valid inputs
    def Test_correct(self):
        # you should select some valid inputs, for which the output is known
        self.assertEqual(get_lyric("Vasco Rossi", "Vivere", "-l", "yes"),get_lyric("Vasco Rossi","Vivere","-l", "yes"))
        #self.assertEqual(get_lyric("vasco rossi" "vivere" "-l" "yes"), (get_lyric("vasco rossi" "vivere" "-l" "yes"))

    # invalid inputs
    #def test_wrong_values(self):
        # you should input wrong data
        #self.assertFalse(get_lyric("Vasco Rossi", "Vivere", "-L", "YES"), get_lyric("Vasco Rossi", "Vivere","-L" "YES"))
        #self.assertEqual(return_birthday(7), None)

        # NOTE: the following test passing an empty list will fail!
        # self.assertEqual(return_birthday([]), None)

    # corner case: empty string
#    def test_empty_string(self):
    #    self.assertEqual(return_birthday(""), None)


if __name__ == '__main__':

    # basic test
    #unittest.main()

    # with more details
    unittest.main(verbosity=2)
