'''# return digital_root (6 kyu).py

Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
Examples

    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
'''

######################################################### MY

# def digital_root(n):
#     new_n = 0
#     if len(str(n)) == 1:
#         return n
#     else:          
#         for digit in str(n):
#             new_n += int(digit)
#         return digital_root(new_n)
   
######################################################### MY REFACTORED

def digital_root(n):
    new_n = 0
    if len(str(n)) == 1:
        return n
    else:          
        new_n = sum(int(digit) for digit in str(n))
        return digital_root(new_n)

######################################################### BEST PRACTICE

# def digital_root(n):
#     return n if n < 10 else digital_root(sum(map(int,str(n))))

######################################################### CLEVER

# def digital_root(n):
# 	return n%9 or n and 9 

#########################################################

print(digital_root(12567535685845565))