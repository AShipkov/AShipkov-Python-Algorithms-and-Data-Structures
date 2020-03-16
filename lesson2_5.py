"""
5. Вывести на экран коды и символы таблицы ASCII,
начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
"""

def row_model(v, w):
    table = '| {:<1}: {:<2} ' * w + '|'
    return table.format(*v)

def rowsymbol(a, b, c):
    row = []
    result = ''

    for i in range(a, b+1):
        row.append(i)
        row.append(chr(i))
        if len(row) >= c * 2:
            result += row_model(tuple(row), c) + '\n'
            row = []

    if len(row) > 0:
        result += row_model(tuple(row), len(row) // 2)
    return result

print(rowsymbol(32, 127, 10))