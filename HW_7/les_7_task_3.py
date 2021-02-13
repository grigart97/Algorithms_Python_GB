# Task 3 Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы


import random
from statistics import median

size = 5
arr = [random.randint(-100, 100) for _ in range(2 * size - 1)]
print(arr)


def get_median(arr):
    for el in arr:  # Идём по каждому элементу
        smaller, equal, larger = 0, 0, 0  # считаем количество элементом больше и меньше данного
        for i in range(len(arr)):
            if el < arr[i]:
                larger += 1
            elif el > arr[i]:
                smaller += 1
            else:
                equal += 1
        if smaller == larger or abs(larger - smaller) == equal - 1:  # вычитаем единицу, потому что сравнивали с собой
            return el


print(get_median(arr))
print(median(arr))
