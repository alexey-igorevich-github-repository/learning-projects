''' # strip comments (4 kyu).py

Complete the solution so that it strips 
all text that follows any of a set of comment markers passed in. 
Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples

The output expected would be:

apples, pears
grapes
bananas

The code would be called like so:

result = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])

# result should == "apples, pears\ngrapes\nbananas"

'''

######################################################### MY

import re

def strip_comments(strng, markers):
    array = strng.split("\n")
    new_array = []
    for element in array:
        for marker in markers:
            cursor = element.find(marker)
            if cursor != -1:
                element = element[:cursor].rstrip()
        new_array.append(element)
    return("\n".join(new_array))

######################################################### BEST PRACTICE && CLEVER

# def strip_comments(string,markers):
#     parts = string.split('\n')
#     for s in markers:
#         parts = [v.split(s)[0].rstrip() for v in parts]
#     return '\n'.join(parts)


######################################################### CLEVER LAMBDA

# strip_comments=lambda t,m,r=__import__('re'):r.sub(r'( *[{}].*)'.format(r.escape(''.join(m))),'',t)if m else t

#########################################################


strng = "  ' ' oranges avocados bananas apples\n@ = - , strawberries\napples oranges ?"
markers = ['#', '?', '-', "'", '.', '=', '^', ',']

print(strip_comments(strng, markers))






