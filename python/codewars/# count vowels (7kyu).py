'''# count vowels (7kyu).py

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

'''

######################################################### MY

# def get_count(sentence):
#     i = 0
#     for s in sentence:
#         if s == "a" or s == "e" or s == "i" or s == "o" or s == "u":
#             i += 1
#     return i

######################################################### BEST PRACTICE && CLEVER

# def get_count(inputStr):
#     return sum(1 for let in inputStr if let in "aeiouAEIOU")

######################################################### BEST PRACTICE && CLEVER

# def get_count(s):
#     return sum(c in 'aeiou' for c in s)

######################################################### LAMBDA

get_count = lambda s: sum(s.count(i) for i in 'aeiou')

#########################################################

print(get_count("Hello World!"))