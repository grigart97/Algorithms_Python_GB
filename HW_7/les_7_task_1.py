# Task 1
# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.


import random

size = 10
arr = [random.randint(-100, 100) for _ in range(size)]
print(arr)


def bubble(array):
    for n in range(1, len(array) - 1):
        for j in range(len(array) - n):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


bubble(arr)
print(arr)
