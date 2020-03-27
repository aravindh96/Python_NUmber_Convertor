#Testcase
import unittest

from conversion_functions import *

class TestHelper(unittest.TestCase):

    # Test that strip_number() can remove all non alphanumeric characters
    def test_strip_num(self):
        data = "_&^12#@!()34ab$*:\"\\,./?fe"
        result = strip_number(data)
        self.assertEqual(result,"1234abfe")


    # Test that strip_number() works for empty string
    def test_strip_empty(self):
        data = ""
        result = strip_number(data)
        self.assertEqual(result,"")


    # Test that strip_number() works for non strings
    def test_strip_int(self):
        data = 4585
        result = strip_number(data)
        self.assertEqual(result,"4585")


    # Test that valid_word() works for non strings
    def test_valid_int(self):
        data = 45859451
        result = valid_word(data)
        self.assertEqual(result,"")

    # Test that valid_word() can remove all non alphabets &
    # test for finding mixed case words - 'HeLlO'
    def test_valid_characters(self):
        data = "_&^12#@!()34ab$*:\"HeLlO\\,./?fe"
        result = valid_word(data)
        self.assertEqual(result.lower(),"hello")

    # Test that valid_word() returns first word in multi-word input
    def test_valid_multiple(self):
        data = "12ringing-bells"
        result = valid_word(data)
        self.assertEqual(result.lower(),"ringing")



if __name__ == 'main':
    unittest.main()
