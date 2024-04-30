'''# alphabet_position (6kyu).py

Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
Example

alphabet_position("The sunset sets at twelve o' clock.")

Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

'''

######################################################### MY FAIL

def alphabet_position(text):
    string = ""
    for index, symbol in enumerate(text):
        if symbol.isalpha() and index == len(text) - 1:
            print(index)          
            string += str(ord(symbol.lower()) - 96)
        elif symbol.isalpha():
            print(f"{index} + isalpha")            
            string += str(ord(symbol.lower()) - 96) + " "      
        else:
            pass
    return string.rstrip()


######################################################### MY

# def alphabet_position(text):
#     string = ""
#     for symbol in text:
#         if symbol.isalpha():       
#             string += str(ord(symbol.lower()) - 96) + " "    
#         else:
#             pass
#     return string.rstrip()

######################################################### BEST PRACTICE && CLEVER

# def alphabet_position(text):
#     return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

######################################################### DICT IN STRING VARIANT

# def alphabet_position(text):
#   al = 'abcdefghijklmnopqrstuvwxyz'
#   return " ".join(filter(lambda a: a != '0', [str(al.find(c) + 1) for c in text.lower()]))

######################################################### DICT IN LIST VARIANT

# def alphabet_position(text):
#     answer = ""
#     alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
#     'w', 'x', 'y', 'z']
#     for char in text.lower():
#         if char in alphabet:
#             answer += (str(alphabet.index(char) + 1) + " ")
#     return answer[:-1]

######################################################### ANOTHER DICT

def alphabet_position(text):
    s=''
    for i in text:
        if i!=' ':
            if ord(i)==65 or ord(i)==97:
                s+='1 '
            elif ord(i)==66 or ord(i)==98:
                s+='2 '
            elif ord(i)==67 or ord(i)==99:
                s+='3 ' 
            elif ord(i)==68 or ord(i)==100:
                s+='4 '
            elif ord(i)==69 or ord(i)==101:
                s+='5 '
            elif ord(i)==70 or ord(i)==102:
                s+='6 '
            elif ord(i)==71 or ord(i)==103:
                s+='7 '
            elif ord(i)==72 or ord(i)==104:
                s+='8 '
            elif ord(i)==73 or ord(i)==105:
                s+='9 '
            elif ord(i)==74 or ord(i)==106:
                s+='10 '
            elif ord(i)==75 or ord(i)==107:
                s+='11 '
            elif ord(i)==76 or ord(i)==108:
                s+='12 '
            elif ord(i)==77 or ord(i)==109:
                s+='13 '
            elif ord(i)==78 or ord(i)==110:
                s+='14 '
            elif ord(i)==79 or ord(i)==111:
                s+='15 '
            elif ord(i)==80 or ord(i)==112:
                s+='16 '
            elif ord(i)==81 or ord(i)==113:
                s+='17 '
            elif ord(i)==82 or ord(i)==114:
                s+='18 '
            elif ord(i)==83 or ord(i)==115:
                s+='19 '
            elif ord(i)==84 or ord(i)==116:
                s+='20 '
            elif ord(i)==85 or ord(i)==117:
                s+='21 '
            elif ord(i)==86 or ord(i)==118:
                s+='22 '
            elif ord(i)==87 or ord(i)==119:
                s+='23 '
            elif ord(i)==88 or ord(i)==120:
                s+='24 '
            elif ord(i)==89 or ord(i)==121:
                s+='25 '
            elif ord(i)==90 or ord(i)==122:
                s+='26 '
            else:
                s+=''
    l=len(s)
    return s[0:-1]

#########################################################

print(alphabet_position("The."))