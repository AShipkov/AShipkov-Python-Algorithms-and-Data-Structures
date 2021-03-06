"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин
"""
import random
def graph(n):
    g={}
    list = [i for i in range (0,n)]
    i=0
    for i in range (0,n):
        key = i
        random.shuffle(list)
        value = [list[a] for a in range (0,3) if list[a] != i]  # range от (0 до 2, 3, 4 итд принял (0,3)
        g [key] = value
    return  g

def dfs(v):
    visited[v] = True
    for w in graph(N):
        if visited[w] == False:  # посещён ли текущий сосед?
            dfs(w)

N = int(input('Введите количество вершин:  '))
print(f'Получился граф : {graph(N)}')
visited = [False] * N  # массив "посещена ли вершина?"
dfs(0)                 # идем от 0 вершины
print(f'Проверяем условие, в котором все вершины связаны: Количество вершин {N} = Обошли вершин {visited.count(True)}')
"""
Введите количество вершин:  11
Получился граф : {0: [3, 8], 1: [7, 3, 10], 2: [5, 10, 7], 3: [1, 10, 0], 4: [9, 5, 7], 5: [1, 8, 10], 6: [8, 7, 2], 7: [5, 0, 4], 8: [0, 7, 4], 9: [8, 7], 10: [1, 2, 6]}
Проверяем условие, в котором все вершины связаны: Количество вершин 11 = Обошли вершин 11
По условию задачи вводим количество вершин -- 11
После получаем не взвешенный ориентированный граф (вывел на печать)
Обходим граф для проверки. Начало с вершины 0.
При тождестве Количество вершин 11 = Обошли вершин 11 получаем исполнение условия задачи : "граф без петель, в котором все вершины связаны"
чтд :)
"""