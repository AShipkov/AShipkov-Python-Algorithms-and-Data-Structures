"""
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

def find_number(a, b, c=0):
    if a < 10:
        if a == b:
            c += 1
        return int(c)
    else:
        if int(a % 10) == b:
            c += 1
        return find_number(a // 10, b, c)

count = 0
number = int(input('Искомое число: '))
print('Вводите последовательность чисел, для завершения введите "0"')

while True:
    d = int(input('Последовательность чисел: '))
    if d == 0:
        break
    count += find_number(d, number)
    print(f'найдено {count} раз')
    count = 0