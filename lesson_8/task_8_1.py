"""
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""

from functools import reduce

N = int(input('Введите количество друзей N: '))
print('Получился graph:')
graph = [[int(i > j) for i in range(N)] for j in range(N)]
for i in range(len(graph)):
    for j in range(len(graph[i])):
        print(graph[i][j], end=' ')
    print()
count = reduce(lambda list, x: list + sum(x), graph, 0)
print(f'Количество рукопожатий {count}')

"""
Базовое условие, что друзья не жмут руку сами себе :)
Введите количество друзей N: 6
Получился graph:
0 1 1 1 1 1 
0 0 1 1 1 1 
0 0 0 1 1 1 
0 0 0 0 1 1 
0 0 0 0 0 1 
0 0 0 0 0 0 
Количество рукопожатий 15
"""