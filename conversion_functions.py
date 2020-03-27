
import re
from nltk.corpus import words
word_set = set(words.words())
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
keypad = {}
for key, value in phone_pad.items():
    keypad.update(dict.fromkeys(value, key))

""" Input: Phone Number  - type:str
    Funct (strip): Removes all characters other than digits and alphabets"""

def strip_number(phone_number):
    strip_num = re.sub('[^A-Za-z0-9]+', '', str(phone_number))
    return strip_num

"""Input: Phone Number - type:str
   Funct(valid_word): Returns a valid english word in the given number"""

def valid_word(phone_number):
    p = re.compile('[^A-Za-z]')
    word_list = p.split(phone_number)
    word_list = list(filter(None, word_list))

    for word in word_list:
        if(word.lower() in word_set and len(word) > 2):
            return word
    return ""

""" Input: Phone Number - type: str
    Funct (phone_format): Returns formated number into following pattern
                          (d-ddd-ddd-dddd) or (ddd-lll-ddd) where- digit; l-letter"""

def phone_format(phone_number):
    clean_phone_number = re.sub('[^A-Za-z0-9]+', '', str(phone_number))
    word = valid_word(clean_phone_number)

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

    formatted_phone_number = (re.sub("(\w)(?=(\w{3})+(?!\w))", r"\1-", "%s" %
                             str(clean_phone_number[:-1])) + clean_phone_number[-1])
    return formatted_phone_number
