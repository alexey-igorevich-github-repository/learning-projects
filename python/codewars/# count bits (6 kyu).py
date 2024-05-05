''' # count bits (6 kyu).py
Write a function that takes an integer as input, 
and returns the number of bits that are equal to one in 
the binary representation of that number. 
You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, 
so the function should return 5 in this case
'''

######################################################### MY

# def count_bits(n):
#     if n == 0:
#         return 0
#     string = ""
#     while n > 1:
#         tail = n % 2
#         string += str(tail)
#         n = n // 2

#     string = "1" + string[::-1]
#     return string.count("1")

######################################################### BEST PRACTICE && CLEVER

# def count_bits(n):
#     return bin(n).count("1")

######################################################### BEST PRACTICE && CLEVER

# def count_bits(n):
#     return n.bit_count()

######################################################### LAMBDA EXAMPLE

# count_bits = lambda n: bin(n).count('1')

######################################################### INTERESTING

# def count_bits(n):
#     return '{:b}'.format(n).count('1')

######################################################### SUPER CLEVER =)

count_bits = lambda n: n.bit_count()

######################################################### 

print(count_bits(14))