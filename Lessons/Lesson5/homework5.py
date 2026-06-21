#- створити функцію яка обчислює та повертає площу прямокутника зі сторонами а і б
from unittest import result


def calc (a, b):
    result = a * b
    print(result)
    return result

calc(25, 30)
print('----------------')

#створити функцію яка обчислює та повертає площу кола з радіусом r
import math
def calc2(r):
    res = math.pi * r * r
    print(res)
    return res

calc2(8)
print('--------------')

#створити функцію яка обчислює та повертає площу циліндру висотою h, та радіутом r
def calc3 (r, h):
    result = (2 * math.pi * r * r)+(2 * math.pi * r * h)
    print(result)
    return result

calc3(7, 4)
print('--------------')

#створити функцію яка приймає масив та виводить кожен його елемент
content = [11, 'sunny', 7, 'gold standart', 558, 25, 34]

def arr (big_arr):
    for index in big_arr:
        print(index)

arr(content)
print('-----------------')

#створити функцію sum(arr) яка приймає масив чисел,
# підсумовує значення елементів масиву та повертає його. Приклад sum([1,2,10]) //->13
def sum_number (arr_num):
    return sum(arr_num)

print(sum_number([22, 10, 5, 17, 30, 11, 9, 8]))
