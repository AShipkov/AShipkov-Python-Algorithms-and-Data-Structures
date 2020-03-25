"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
"""
from collections import deque

digit_numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def summ_sixteen(x, y):


    result = deque()
    transfer = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)
    while x:
        if y:
            output = digit_numbers[x.pop()] + digit_numbers[y.pop()] + transfer
        else:
            output = digit_numbers[x.pop()] + transfer
        transfer = 0
        if output < 16:
            result.appendleft(digit_numbers[output])
        else:
            result.appendleft(digit_numbers[output - 16])
            transfer = 1
    if transfer:
        result.appendleft('1')
    return list(result)

def multiplication_sixteen(x, y):

    result = deque()
    lot = deque([deque() for _ in range(len(y))])
    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        a = digit_numbers[y.pop()]
        for j in range(len(x) - 1, -1, -1):
            lot[i].appendleft(a * digit_numbers[x[j]])
        for _ in range(i):
            lot[i].append(0)

    transfer = 0
    for _ in range(len(lot[-1])):
        output = 0
        for i in range(len(lot)):
            if lot[i]:
                output += lot[i].pop()
        if output < 16:
            result.appendleft(digit_numbers[output])
        else:
            result.appendleft(digit_numbers[output % 16])
            transfer = output // 16
    if transfer:
        result.appendleft(digit_numbers[transfer])
    return list(result)

number1 = list(input('Введите число 1: ').upper())
number2 = list(input('Введите число 2: ').upper())

print(*number1, '+', *number2, '=', *summ_sixteen(number1, number2))
print(*number1, '*', *number2, '=', *multiplication_sixteen(number1, number2))
