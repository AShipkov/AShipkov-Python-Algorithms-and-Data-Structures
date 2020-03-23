"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

random_list = random.sample(range(0,1000), 5)
print(f'{"Массив случаных чисел":25} {random_list}')
index_max = index_min = 0
number_max = random_list[0]
number_min = random_list[0]

for index, number in enumerate(random_list):
    if(number > number_max):
        number_max = number
        index_max = index
    if(number < number_min):
        number_min = number
        index_min = index
random_list[index_min], random_list[index_max] = random_list[index_max], random_list[index_min]

print(f'{"Массив измененный":25} {random_list}\nЗамена местами максимального числа {number_max} и минимального числа {number_min}')