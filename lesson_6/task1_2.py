"""
1.3. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

import random
import sys

def f(*qwarks):
    sum_size =0
    count = 0
    for i in qwarks:
        count+=1
        print(f'Переменная {count}: type = {type(i)}, size = {sys.getsizeof(i)}, object = {i}')
        sum_size += sys.getsizeof(i)
    return sum_size

number_range = input('Для получения случайного числа, введите диапазон чисел от и до через запятую: ').split(',')
rand_int = random.randint(int(number_range[0]), int(number_range[1]))
#print('Случайное целое число: ', format(rand_int))

uni_range = input('Для получения случайного вещественного числа, введите диапазон чисел от и до через запятую: ').split(',')
rand_uni = random.uniform(float(uni_range[0]), float(uni_range[1]))
#print('Случайное вещественное число: ', format(rand_uni))

char_range = input('Для получения случайного символа, введите диапазон символов от a до Z через запятую: ').split(',')
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = chars.index(char_range[0])
b = chars.index(char_range[1])
rand_uni1 = random.choice(chars[a:b])
#print('Случайнный символ: ',format(rand_uni))

print(f'Переменные в сумме занимают {f(number_range, rand_int, uni_range, rand_uni, char_range, chars, a, b, rand_uni1)}')
"""
1 вариант
Для получения случайного числа, введите диапазон чисел от и до через запятую: 1,100
Для получения случайного вещественного числа, введите диапазон чисел от и до через запятую: 1,100
Для получения случайного символа, введите диапазон символов от a до Z через запятую: a,Z
Переменная 1: type = <class 'list'>, size = 152, object = ['1', '100']
Переменная 2: type = <class 'int'>, size = 28, object = 40
Переменная 3: type = <class 'list'>, size = 152, object = ['1', '100']
Переменная 4: type = <class 'float'>, size = 24, object = 48.199374186388006
Переменная 5: type = <class 'list'>, size = 152, object = ['a', 'Z']
Переменная 6: type = <class 'str'>, size = 101, object = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
Переменная 7: type = <class 'int'>, size = 24, object = 0
Переменная 8: type = <class 'int'>, size = 28, object = 51
Переменная 9: type = <class 'str'>, size = 50, object = p
Переменные в сумме занимают 711
2 вариант
Для получения случайного числа, введите диапазон чисел от и до через запятую: 1,2
Для получения случайного вещественного числа, введите диапазон чисел от и до через запятую: 1,2
Для получения случайного символа, введите диапазон символов от a до Z через запятую: a,c
Переменная 1: type = <class 'list'>, size = 152, object = ['1', '2']
Переменная 2: type = <class 'int'>, size = 28, object = 1
Переменная 3: type = <class 'list'>, size = 152, object = ['1', '2']
Переменная 4: type = <class 'float'>, size = 24, object = 1.792984794197296
Переменная 5: type = <class 'list'>, size = 152, object = ['a', 'c']
Переменная 6: type = <class 'str'>, size = 101, object = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
Переменная 7: type = <class 'int'>, size = 24, object = 0
Переменная 8: type = <class 'int'>, size = 28, object = 2
Переменная 9: type = <class 'str'>, size = 50, object = a
Переменные в сумме занимают 711
Вывод: как и в первой задаче размер места, занимаемого данными, не зависит от введенного диапазона.
"""