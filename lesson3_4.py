"""
4. Определить, какое число в массиве встречается чаще всего.
"""
import random

def f(a):    #для первой сотни раз :)
    if a < 20:
        if a > 1 and a < 5:
            a = 'раза'
        else:
            a = 'раз'
    else:
        a = a % 10
        if a > 1 and a < 5:
            a= 'раза'
        else:
            a = 'раз'
    return a

random_list = random.sample([i for i in range(0, 5)]*100,30)
print(f"Массив {random_list}")

count = {}
max_number = max_count = 0

for i in random_list:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
    if count[i] > max_count:
        max_count = count[i]
        max_number = i

print(f'Чаще всего встречается число: {max_number} - {max_count} {f(max_count)}')