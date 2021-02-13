# Task 2
# Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.


g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]


def dijkastra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    paths = [[] for _ in range(length)]
    cost[start] = 0
    min_cost = 0
    while min_cost < float('inf'):
        is_visited[start] = True
        paths[start].append(start)
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
                    paths[i] = list(paths[start])
        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
                break
    return cost, paths


way_costs, way_paths = dijkastra(g, 0)
for i in range(len(g)):
    if way_costs[i] != float('inf'):
        print(f'Путь до вершины {i} - ', *way_paths[i], ' ', f'и занимает {way_costs[i]} условных единиц')
    else:
        print(f'Путь до вершины {i} - невозможен')
