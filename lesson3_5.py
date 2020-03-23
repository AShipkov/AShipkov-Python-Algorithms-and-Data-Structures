"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
import random

random_list = random.sample(range(-50,20), 10)

max_number = {}
print(random_list)

for index,number in enumerate(random_list):
    if number < 0:
        if 'value' not in max_number:
            max_number['key'] = index+1
            max_number['value'] = number
        elif number > max_number['value']:
            max_number['key'] = index+1
            max_number['value'] = number

if not('value' in max_number):
    print('Массив содержит положительные значения')
else:
    print(f'Максимальное отрицательное число {max_number["value"]}, стоящее на {max_number["key"]} месте массива')