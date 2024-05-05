'''# split_strings (6 kyu).py

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
'''

######################################################### MY

# def solution(s):
#     array=[]

#     for pot in range(0,len(s)):
#         if pot % 2 == 0:
#             array.append(s[pot:pot+2])

#     if len(s) % 2 == 0:
#         return array
#     else:
#         array[len(array)-1] = array[len(array)-1] + "_"
#         return array

######################################################### BEST PRACTICE

# def solution(s):
#     result = []
#     if len(s) % 2:
#         s += '_'
#     for i in range(0, len(s), 2):
#         result.append(s[i:i+2])
#     return result

######################################################### CLEVER

# import re

# def solution(s):
#     return re.findall(".{2}", s + "_")

######################################################### MY WITH EXTRA FEATURES

def solution(s):
    size=3 #
    array=[]

    for pot in range(0,len(s)):
        if pot % size == 0:
            array.append(s[pot:pot+size])   

    if len(s) % size == 0:
        return array
    else:
        array[len(array)-1] = array[len(array)-1] + ("_" * (size - (len(s) % size)))
        return array
        
######################################################### 

print(solution("123456789"))

