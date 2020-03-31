"""
3.5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
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

random_list = random.sample(range(-50,20), 10)
max_number = {}
#print(random_list)
for index,number in enumerate(random_list):
    if number < 0:
        if 'value' not in max_number:
            max_number['key'] = index+1
            max_number['value'] = number
        elif number > max_number['value']:
            max_number['key'] = index+1
            max_number['value'] = number
if not('value' in max_number):
    pass
#    print('Массив содержит положительные значения')
else:
    pass
#    print(f'Максимальное отрицательное число {max_number["value"]}, стоящее на {max_number["key"]} месте массива')

print(f'Переменные в сумме занимают {f(random_list, max_number, number, index)}')
"""
1 вариант
Переменная 1: type = <class 'list'>, size = 136, object = [7, -6, 1, -49, -14, 16, -35, -46, -31, -43]
Переменная 2: type = <class 'dict'>, size = 232, object = {'key': 2, 'value': -6}
Переменная 3: type = <class 'int'>, size = 28, object = -43
Переменная 4: type = <class 'int'>, size = 28, object = 9
Переменные в сумме занимают 424
2 вариант
Переменная 1: type = <class 'list'>, size = 136, object = [-3, -14, 6, 7, 5, 4, -29, -16, 10, -17]
Переменная 2: type = <class 'dict'>, size = 232, object = {'key': 1, 'value': -3}
Переменная 3: type = <class 'int'>, size = 28, object = -17
Переменная 4: type = <class 'int'>, size = 28, object = 9
Переменные в сумме занимают 424
Выврд: размер памяти, занимаемой переменными, не зависит от значений в random_list.
"""