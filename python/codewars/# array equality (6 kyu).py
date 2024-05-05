'''# array equality (6 kyu).py

Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks
whether the two arrays have the "same" elements, with the same multiplicities
(the multiplicity of a member is the number of times it appears).
"Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

Examples
Valid arrays

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

comp(a, b) returns true because in b 
121 is the square of 11, 
14641 is the square of 121, 
20736 the square of 144, 
361 the square of 19, 
25921 the square of 161, 
and so on. It gets obvious 
if we write b's elements in terms of squares:

a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

Invalid arrays

If, for example, we change the first number to something else, comp is not returning true anymore:

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]

comp(a,b) returns false because in b 132 is not the square of any number of a.

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]

comp(a,b) returns false because in b 36100 is not the square of any number of a.
Remarks

    a or b might be [] or {} (all languages except R, Shell).
    a or b might be nil or null or None or nothing (except in C++, COBOL, Crystal, D, Dart, Elixir, Fortran, F#, Haskell, Nim, OCaml, Pascal, Perl, PowerShell, Prolog, PureScript, R, Racket, Rust, Shell, Swift).

If a or b are nil (or null or None, depending on the language), the problem doesn't make sense so return false.


'''

######################################################### MY

array1 = [11, 19, 19, 19, 121, 144, 144, 161]
array2 = [121, 361, 361, 361, 14641, 20736, 20736, 25921]


# def comp(array1, array2):
#     if (array1 == [] and array2 == []):
#         return True
#     elif not array1 or not array2:
#         return False
#     elif len(array1) == len(array2):
#         for e in array1:
#             if e is None or e == "" or type(e) is not int:
#                 return False
#         for e in array2:
#             if e is None or e == "" or type(e) is not int:
#                 return False
#         sa1 = sorted(array1)
#         sa2 = sorted(array2)
#         sqrt1 = []
#         for e in sa1:
#             sqrt1.append(e**2)
#         for e in sqrt1:
#             if e not in sa2:
#                 return False
#             else:
#              print(sqrt1)
#              print(sa2)
#             for e, ee in zip(sorted(sqrt1), sorted(sa2)):
#              if e != ee:
#               return False
#             return True
#     else:
#      return False

######################################################### BEST PRACTICE && CLEVER

def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False

'''
    Код, который может вызвать ошибку, помещается в блок try. 
    
    return sorted([i ** 2 for i in array1]) == sorted(array2): Эта строка выполняет следующие действия:
        Генератор списка [i ** 2 for i in array1] создает список квадратов элементов из array1.
        Функция sorted() сортирует оба списка.
        Сравнивает два отсортированных списка на равенство. Если оба списка одинаковы, 
        значит, квадраты элементов из array1 равны array2.
        Если нет ошибок, функция возвращает результат сравнения. 
        Если возникает исключение (например, если array1 содержит 
        нечисловые элементы), выполнение переходит к блоку except.

    except: Универсальный способ борьбы с фокусами автора каты=)
    любое исключение (будь то TypeError, ValueError, и т.д.) и функция возвращает False

'''

######################################################### CLEVER

# def comp(array1, array2):
#     return None not in (array1, array2) and [i*i for i in sorted(array1)]==sorted(array2)


'''
    None not in (array1, array2): 
    Эта проверка убеждается, что ни один из аргументов функции array1 или array2 не является None.
    
    [i*i for i in sorted(array1)]: 
    Это генератор списка, который создает список квадратов элементов из array1, но сначала сортирует array1.

    sorted(array2): Эта функция сортирует элементы в array2.

'''

#########################################################

print(comp(array1, array2))