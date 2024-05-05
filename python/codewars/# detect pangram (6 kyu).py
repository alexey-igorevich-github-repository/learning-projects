'''# detect pangram (6 kyu).py

A pangram is a sentence that contains every single letter of the alphabet at least once.

For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is,
False if not. Ignore numbers and punctuation.

'''

######################################################### MY

# def is_pangram(s):
#     s= s.lower().replace(" ","")
#     for symbol in s:
#         counter = 0
#         for letter in s:
#             if symbol == letter:
#                 counter += 1
#                 if counter >= 2:
#                     return False
#     return True

######################################################### MY + What is a pangram? I dont understand.

# def is_pangram(s):
#     s = s.lower().replace(" ", "")
#     return len(set(s)) == len(s)

######################################################### MY +++

# import re

# def is_pangram(s):
#     s = s.lower()
#     s = re.sub(r'[^a-zA-Z]', '', s)
#     unique_letters = set(s)
#     if len(unique_letters) == 26:
#         return True
#     else:
#         return False

######################################################### MY +++

import re

def is_pangram(s):
    return len(set(re.sub(r'[^a-zA-Z]', '',s.lower()))) == 26

######################################################### BEST PRACTICE

# import string

# def is_pangram(s):
#     s = s.lower()
#     for char in 'abcdefghijklmnopqrstuvwxyz':
#         if char not in s:
#             return False
#     return True

######################################################### CLEVER

# import string

# def is_pangram(s):
#     return set(string.ascii_lowercase).issubset(s.lower())

######################################################### 

print(is_pangram("Cwm fjord bank glyphs vext quiz"))
print(is_pangram("This isn't a pangram!"))