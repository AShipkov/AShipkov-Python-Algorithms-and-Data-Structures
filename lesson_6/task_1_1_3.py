"""
1.4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""
import sys
def f(*qwarks):
    sum_size =0
    count = 0
    for i in qwarks:
        count+=1
        print(f'Переменная {count}: type = {type(i)}, size = {sys.getsizeof(i)}, object = {i}')
        sum_size += sys.getsizeof(i)
    return sum_size

def alphabet_position(text):
    nums = [int(str(ord(x) - 96)) for x in text.lower() if x >= 'a' and x <= 'z']
    return nums
text = input('Введите подряд 2 буквы: ')
#print(f'Позиция букв {alphabet_position(text)} между ними {alphabet_position(text)[1]-alphabet_position(text)[0]-1} буква')
print(f'Переменные в сумме занимают {f(text)}')
"""
вариант 1
Введите подряд 2 буквы: az
Переменная 1: type = <class 'str'>, size = 51, object = az
Переменные в сумме занимают 51
вариант 2
Переменная 1: type = <class 'str'>, size = 51, object = ac
Переменные в сумме занимают 51
Вывод: количество занимаемой памяти также не зависит от диапазона символов.

Вывод: количество памяти, занимаемой переменными, значительно ниже чем во всех предыдущих вариантах. Это саммая эффективная программа.
"""