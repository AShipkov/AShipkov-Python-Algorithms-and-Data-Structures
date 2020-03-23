"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random
random_list = random.sample(range(0,1000), 15)

numbers = {
    'max_number': random_list[0],
    'min_number': random_list[0],
    'min_index': 0,
    'max_index': 0,
    'summ': 0
}

print("\n",random_list,"\n")

for index,number in enumerate(random_list):
    if number > numbers['max_number']:
        numbers['max_index'] = index
        numbers['max_number'] = number
    elif number < numbers['min_number']:
        numbers['min_index'] = index
        numbers['min_number'] = number

if numbers['min_index']+1 < numbers['max_index']:
    for i in random_list[numbers['min_index']+1:numbers['max_index']]:
        numbers['summ'] += i
elif numbers['min_index'] > numbers['max_index']+1:
    for i in random_list[numbers['max_index']+1:numbers['min_index']]:
        numbers['summ'] += i

print(f'Сумма, элементов массива, стоящих между минимальным элеиентом {numbers["min_number"]} и максимальным элементом {numbers["max_number"]} равна {numbers["summ"]}')

