# Task 2
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

size = 10
array = [round(random.uniform(0, 50), 3) for _ in range(size)]
print(array)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left_arr, right_arr):
        out_arr = []
        idx_l, idx_r = 0, 0
        while idx_l < len(left_arr) and idx_r < len(right_arr):  # добавляем поэлементно от меньшего к большему
            if left_arr[idx_l] > right_arr[idx_r]:
                out_arr.append(right_arr[idx_r])
                j += 1
            else:
                out_arr.append(left_arr[idx_l])
                idx_l += 1
        # один из списком полностью добавлен. Осталось добавить последний элемент второго
        if idx_l == len(left_arr):  # если левый список пройден полностью, добавляем последний элемент правого
            out_arr.append(right_arr[idx_r])
        elif idx_r == len(right_arr):  # если правый список пройден полностью, добавляем последний элемент левого
            out_arr.append(left_arr[idx_l])
        return out_arr
    left = merge_sort(arr[:int(len(arr) / 2)])
    right = merge_sort(arr[int(len(arr) / 2):])
    return merge(left, right)


a = merge_sort(array)
print(a)
