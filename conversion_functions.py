
import re
from nltk.corpus import words


class NumberConverter():

    # Initializing instance variables
    def __init__(self, phone_number, word_set=None, phone_pad=None, keypad=None):

        self.phone_number = phone_number
        if word_set is None:
            word_set = set(words.words())
        self.word_set = word_set
        if phone_pad is None:
            phone_pad = {'0': [],
                         '1': [],
                         '2': ['A', 'B', 'C'],
                         '3': ['D', 'E', 'F'],
                         '4': ['G', 'H', 'I'],
                         '5': ['J', 'K', 'L'],
                         '6': ['M', 'N', 'O'],
                         '7': ['P', 'Q', 'R', 'S'],
                         '8': ['T', 'U', 'V'],
                         '9': ['W', 'X', 'Y', 'Z']}
        self.phone_pad = phone_pad
        if keypad is None:
            keypad = {}
        self.keypad = keypad
        for key, value in phone_pad.items():
            keypad.update(dict.fromkeys(value, key))


    """ Input: Phone Number  - type:str
        Funct (strip): Removes all characters other than digits and alphabets"""
    def strip_number(self,number):
        strip_num = re.sub('[^A-Za-z0-9]+', '', str(number))
        return strip_num


    """ Input: Phone Number - type:str
        Funct(valid_word): Returns a valid english word in the given number"""
    def valid_word(self,number):
        p = re.compile('[^A-Za-z]')
        word_list = p.split(str(number))
        word_list = list(filter(None, word_list))

        for word in word_list:
            if(word.lower() in self.word_set and len(word) > 2):
                return word
        return ""


    """ Input: Phone Number - type: str
        Funct (phone_format): Returns formated number into following pattern
                              (d-ddd-ddd-dddd) or (ddd-lll-ddd) where d-digit; l-letter"""
    def phone_format(self,number):
        clean_phone_number = self.strip_number(number)
        word = self.valid_word(number)

        if word:
            p = re.compile('(' + word + ')')
            num_list = p.split(clean_phone_number)
            num_list = list(filter(None, num_list))
            formatted_num = ""
            for i in range(len(num_list)):
                if i != len(num_list)-1:
                    formatted_num += num_list[i] + "-"
            formatted_num += num_list[-1]
            return formatted_num

        # Formats the number to the desired pattern using regex

        formatted_phone_number = (re.sub("(\w)(?=(\w{3})+(?!\w))", r"\1-", "%s" %
                                 str(clean_phone_number[:-1])) + clean_phone_number[-1])
        return formatted_phone_number


    """ Funct(words_to_number): Converts a phone number containing letters
        into a pure phone number with only digits"""
    def words_to_number(self):
        ret_num = ""
        for i in range(len(self.phone_number)):
            if(self.phone_number[i].isalpha()):
                ret_num += str(self.keypad[self.phone_number[i].upper()])
                continue
            ret_num += self.phone_number[i]
        return self.phone_format(ret_num)
