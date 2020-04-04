"""
2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые необходимо обойти.

"""
graph = [
    [0, 0, 1, 1, 9, 0, 0, 0],   # ВНИМАНИЕ В СХЕМЕ: ПЕРВАЯ ВЕРШИНА СДЕЛАНА ПО СХЕМЕ УРОКА [0, 0, 9, 4, 0, 0, 7, 0]
    [0, 0, 9, 4, 0, 0, 7, 0],       # В КОДЕ: В ГРАФЕ ОШИБКА ПО ПЕРВОЙ ВЕРШИНЕ            [0, 0, 9, 4, 0, 0, 5, 0]
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]



def dijkstra(graph, start):
    start1 = start
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    cost[start] = 0
    min_cost = 0
    d = {}

    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    ways = []
    for i in range(length):
        j = i
        way = ['finish']
        while parent[j] != -1:
            if parent[j] == start1:
                way.insert(0, 'start')
            else:
                way.insert(0, parent[j])
            j = parent[j]

        if way == ['finish'] and cost[i] == 0:
            way = 'Already here'
        elif way == ['finish']:
            way = 'Not avaliable'

        ways.append(way)

    return cost, ways

start_input = int(input('От какой вершины идти: '))
result = dijkstra(graph, start_input)
print(f'Стоимость пути до каждой вершины {result[0]}')
print(f'Маршрут до вершины {result[1]}')
"""
Пояснение к решению:
От какой вершины идти: 6
Стоимость пути до каждой вершины [inf, 16, 7, 20, 8, 1, 0, inf]
Маршрут до вершины ['Not avaliable', ['start', 2, 'finish'], ['start', 'finish'], ['start', 2, 1, 'finish'], ['start', 'finish'], ['start', 'finish'], 'Already here', 'Not avaliable']
Маршрут до вершин можно проверить по схеме (на уроке). В данном примере, если идти от вершины 6 то:
0 вершина недоступна 'Not avaliable 
1 вершина start в 6 вершине, затем идем во вторую, затем идем в первую finish -- ['start', 2, 'finish']
2 вершина доступна за один ход ['start', 'finish']
6 вершина мы в ней находимся ['Already here']
"""

