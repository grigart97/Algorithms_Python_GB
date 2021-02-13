# Task 3
# Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

import random


def graph_generator(vertex_num):
    graph = [[random.randint(0, 1) for _ in range(vertex_num)] for _ in range(vertex_num)]
    for i in graph:
        if i.count(0) == 4:
            i[random.randint(0, 3)] = 1
    return graph


def graph_bypass(graph):
    length = len(graph)
    is_visited = [False] * length
    paths = [[] for _ in range(length)]

    def deep_first_search(start):
        paths[start].append(start)
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                paths[i] = list(paths[start])
                deep_first_search(i)
    deep_first_search(0)
    return paths


n = 4
g = graph_generator(n)
print(*g, sep='\n')
way_paths = graph_bypass(g)
for i in range(n):
    print(f'Путь до вершины {i} - ', *way_paths[i])


