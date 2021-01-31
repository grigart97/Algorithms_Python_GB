# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов, в том числе
# написанных самостоятельно.
from random import randint

n = m = 5
matrix = [[randint(2, 15) for _ in range(m)] for i in range(n)]
for raw in matrix:
    for el in raw:
        print(f'{el:4}', end='')
    print()
raws_min = []
for raw in matrix:
    min_el = raw[0]
    for el in raw:
        if min_el > el:
            min_el = el
    raws_min.append(min_el)
print(f'Минимальные элементы строк: {", ".join(str(el) for el in raws_min)}')
max_el = raws_min[0]
for el in raws_min:
    if max_el < el:
        max_el = el
print(f'Максимальное среди минимальных: {max_el}')
