# В массиве случайных чисел поменять местами минимальный и максимальный элемент.

from random import randint


arr = [randint(0, 100) for _ in range(10)]
print(arr)
min_el = max_el = arr[0]
for i, el in enumerate(arr):
    if el < min_el:
        min_el = el
        min_i = i
    if el > max_el:
        max_el = el
        max_i = i
print(max_el, min_el)
arr[min_i], arr[max_i] = arr[max_i], arr[min_i]
print(arr)


