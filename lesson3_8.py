"""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в ее последнюю ячейку. В конце следует вывести полученную матрицу.
"""
def matrix_model(v, w):
    table = '{:>6}' * w
    return table.format(*v)

matrix = []
print('Введите 4 элемента строки матрицы')

for a in range(4):
    matrix.append([])
    element = 0
    for b in range(4):
        elements = int(input(f'Элемент {b+1}, строки {a+1}: '))
        matrix[a].append(elements)
        element += elements
    matrix[a].append(element)

print('Итоговая матрица: ')
for i in matrix:
    print(matrix_model(i,5))