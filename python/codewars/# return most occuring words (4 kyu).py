'''# return most occuring words (4 kyu).py

Write a function that, given a string of text (possibly with punctuation and line-breaks),
 returns an array of the top-3 most occurring words, in descending order of the number of occurrences.
Assumptions:

    A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
    Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
    Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
    Matches should be case-insensitive, and the words in the result should be lowercased.
    Ties may be broken arbitrarily.
    If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned,
    or an empty array if a text contains no words.

Examples:

"In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."

--> ["a", "of", "on"]


"e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"

--> ["e", "ddd", "aa"]


"  //wont won't won't"

--> ["won't", "wont"]

Bonus points (not really, but just for fun):

    Avoid creating an array whose memory footprint is roughly as big as the input text.
    Avoid sorting the entire array of unique words.

'''

######################################################### MY 

import re
from collections import Counter

def top_3_words(text):
    modified_text_list = []

    if not text:
        return []
    
    text = ''.join(' ' if not symbol.isalpha() and symbol != "'" else symbol for symbol in text)
          
    text_list = text.lower().split()

    for element in text_list:
        if "'" in element:
            if re.match(r"[a-zA-Z]+'", element) or re.match(r"'[a-zA-Z]+", element):
                modified_text_list.append(element)
        else:
            modified_text_list.append(element)

    counter_modified_text_list = Counter(modified_text_list)

    biggest_counter = min(3, len(counter_modified_text_list))
    biggest_elements = [item for item, count in counter_modified_text_list.most_common(biggest_counter)]

    return biggest_elements

######################################################### BEST PRACTICES && CLEVER

# from collections import Counter
# import re


# def top_3_words(text):
#     c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
#     return [w for w,_ in c.most_common(3)]

######################################################### BEST 2

# import re
# from collections import Counter

# def top_3_words(text):
#     words = re.findall(r"[a-z']*[a-z]+[a-z']*", text.lower())
#     top_3 = Counter(words).most_common(3)
#     return [tup[0] for tup in top_3]

 #########################################################  LAMBDA

# import re
# from collections import Counter

# top_3_words=lambda t:[w for w,c in Counter(re.findall("'*[a-z][a-z']*",t.lower())).most_common(3)]   


 ######################################################### 

print(top_3_words("aa hhh ''' "))