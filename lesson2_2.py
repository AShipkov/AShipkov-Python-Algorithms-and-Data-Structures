"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

def f(n, even=0, odd=0):
    if n % 2 == 0:
        even +=1
    else:
        odd +=1
    if (n < 10):
        return f'четных цифр = {even},\nнечетных цифр = {odd}'
    else:
        return f(n // 10, even, odd)

number = input('Введите натуральное число: ')
try:
    print(f(int(number)))
except ValueError:
    print('Ошибка ввода!')