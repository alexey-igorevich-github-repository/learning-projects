'''# array substrings (6 kyu).py

Given two arrays of strings a1 and a2 return a sorted array r 
in lexicographical order of the strings of a1 which are substrings of strings of a2.

Example 1:

a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
returns ["arp", "live", "strong"]


Example 2:

a1 = ["tarp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
returns []

Notes:
    Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
    In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
    Beware: In some languages r must be without duplicates.



'''

######################################################### MY

array1 = ["arp", "live", "strong"]
array2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# def in_array(array1, array2):
#     array3 = []
#     for element1 in array1:
#         for element2 in array2:
#             if element1 in element2:
#                 array3.append(element1)

#     return sorted(list(set(array3)))


######################################################### CLEVER

def in_array(array1, array2):
    return sorted({sub for sub in array1 if any(sub in s for s in array2)})

'''
{sub for sub in a1 if any(sub in s for s in a2)}: Это генератор множества, который выполняет следующее:

    for sub in a1: Проходит по каждому элементу в списке a1.
    any(sub in s for s in a2): Проверяет, существует ли хотя бы один элемент в списке a2, который содержит текущий элемент из a1.
    Внешние фигурные скобки {} используются для создания множества, в котором будут только уникальные элементы.
    Генератор множества отфильтровывает только те элементы из a1, которые встречаются хотя бы раз в a2.

'''   
#########################################################   

print(in_array(array1, array2))