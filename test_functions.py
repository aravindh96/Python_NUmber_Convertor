#Testcase
import unittest

from conversion_functions import *

class TestHelper(unittest.TestCase):
    def test_strip_num(self):

        #Test that strip_number can remove all non numbers and alphabets

        data = "_&^12#@!()34ab$*:\"\\,./?fe"
        result = strip_number(data)
        self.assertEqual(result,"1234abfe")


    #Test that strip_number works for empty string
    def test_strip_empty(self):

        data = ""
        result = strip_number(data)
        self.assertEqual(result,"")


    def test_strip_int(self):
        """
        Test that strip_number works for non strings
        """
        data = 4585
        result = strip_number(data)
        self.assertEqual(result,"4585")


if __name__ == 'main':
    unittest.main()
