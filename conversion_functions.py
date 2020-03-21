
import re

phone_pad = { '0':[],
              '1':[],
              '2':['A','B','C'],
              '3':['D','E','F'],
              '4':['G','H','I'],
              '5':['J','K','L'],
              '6':['M','N','O'],
              '7':['P','Q','R','S'],
              '8':['T','U','V'],
              '9':['W','X','Y','Z'],}
keypad = {}
for key, value in phone_pad.items():
    keypad.update(dict.fromkeys(value,key))

# Input: Phone Number  - type:str
# Output: Stripped Number - type:str
# Func (strip): Removes all characters other than digits and alphabets

def strip_number(phone_number):
    strip_num = re.sub('[^A-Za-z0-9]+', '', phone_number)
    return strip_num

# Input: Phone Number  - type:str
# Output: Formatted Number - type:str
# Func (phone_format): Formats number into following pattern (d-ddd-ddd-dddd)

def phone_format(phone_number):
    clean_phone_number = re.sub('w+', '', phone_number)
    formatted_phone_number = re.sub("(\w)(?=(\w{3})+(?!\w))", r"\1-", "%s" %str(clean_phone_number[:-1])) + clean_phone_number[-1]
    return formatted_phone_number
