
"""
conversion_functions.py implements 3 functions as part of the NumberConverter
class. The three functions words_to_number() , number_to_words() and
all_wordifications() are implemented below.

Helper functions are defined in the util.py file under the Number class.
"""

from util import Number
import random


class NumberConverter:

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.num = Number(self.phone_number)

    def set_number(self, number):
        self.num.phone_number = number

    def words_to_number(self):
        """
        Function: Converts a phone number containing letters
                  into a pure phone number with only digits
        """
        if self.num.phone_number is None:
            print("Input should be of type: str")
            return ""

        ret_num = ""
        if not self.num.phone_number:
            return self.num.phone_number

        for i in range(len(self.num.phone_number)):
            if(self.num.phone_number[i].isalpha()):
                ret_num += str(self.num.keypad[self.num.phone_number[i].upper()])
                continue
            ret_num += self.num.phone_number[i]
        return self.num.phone_format(ret_num)

    def all_wordifications(self):
        """
        Function: Returns a list of all possible combinations
                  containing valid english words and a list of
                  unique english words that exist for this number
        """
        if self.num.phone_number is None:
            print("Input must be of type str")
            return [], []
        phone_number = self.num.strip_number(self.words_to_number())
        if not phone_number:
            return [], []

        number_list = []
        english_list = set()

        # Recursive Helper Function
        def wordification_helper(phone_number, combination):
            # Base case: if length(num)=0 add to list
            if len(phone_number) == 0:
                word = self.num.valid_word(combination)
                if word:
                    number_list.append(self.num.phone_format(combination))
                    english_list.add(word)
                    return
                return

            for letter in self.num.phone_pad[phone_number[0]]:
                wordification_helper(phone_number[1:], combination + letter)

            # To consider combinations where some numbers are not changed
            wordification_helper(phone_number[1:], combination + phone_number[0])
            return

        wordification_helper(phone_number, "")
        return number_list, english_list

    def number_to_words(self):
        """
        Function: Returns one random number from the list of
                  numbers containing valid english word combinations
        """
        if self.num.phone_number is None:
            print("Input must be of type str")
            return ""
        num_list, english_words = self.all_wordifications()
        if num_list:
            return random.choice(num_list)
        else:
            return ""
