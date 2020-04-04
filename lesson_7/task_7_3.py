"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

"""
import random

m = int(input('Введите натуральное число m, ВНИМАНИЕ 0 НЕ НАТУРАЛЬНОЕ ЧИСЛО! :  ')) #Вводится натуральное число.
array_random = [random.randrange(0, 100, 1) for _i in range(2 * m + 1)]             #Создаем спмсок длинной len(array_random) = 2*m+1

def median(array, pivot_fn=random.choice):                         #Ищем медиану,поэтому мы ищем (2*m+1)//2 наименьший элемент, тк len(array_random) = 2*m+1
        return select(array, (2*m+1) // 2, pivot_fn)           #Сначала нам нужно выбрать опорный элемент (pivot).Мы случайным образом выбираем индекс  pivot_fn=random.choice

def select(array, k, pivot_fn):
    pivot = pivot_fn(array)

    low = [element for element in array if element < pivot]                             #Разбиваем список на группы согласно pivot и т.д.
    high = [element for element in array if element > pivot]
    pivots = [element for element in array if element == pivot]

    if k < len(low):
        return select(low, k, pivot_fn)
    elif k < len(low) + len(pivots):
        return pivots[0]                                                                #  Мы угадали медиану!!!
    else:
        return select(high, k - len(low) - len(pivots), pivot_fn)

print(f'Медиана массива {array_random} равна {median(array_random)}')

"""
Полученный код имеет сложность О(N)
"""