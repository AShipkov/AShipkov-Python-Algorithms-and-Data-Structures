"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
import random

random_list = random.sample([i for i in range(0, 10)] * 2,10)

print(random_list)

numbers = {}

for index, number in enumerate(random_list):
    if 'min_number1' not in numbers:
        numbers['min_number1'] = number
    elif number < numbers['min_number1']:
        numbers['min_number2'] = numbers['min_number1']
        numbers['min_number1'] = number
    elif 'min_number2' not in numbers:
        numbers['min_number2'] = number
    elif number < numbers['min_number2']:
        numbers['min_number2'] = number

print(f"Два наименьших числа {numbers['min_number1']} и {numbers['min_number2']}")