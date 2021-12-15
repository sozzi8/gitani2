import unittest
import sys
import os
#from lyrics import get_lyric


# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestInput(unittest.TestCase):

    # smoke test: valid inputs
    def test_correct_values(self):
        # you should select some valid inputs, for which the output is known
        self.assertEqual(database_of_songs("vasco rossi" "vivere" "-l" "yes"), print ("you have added this song to your playlist"))

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

    # basic test
    #unittest.main()

    # with more details
    unittest.main(verbosity=2)
