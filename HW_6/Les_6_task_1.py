# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
# первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
import sys


def show_sizeof(x, level=0):
    print("\t" * level, x.__class__, sys.getsizeof(x), x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_sizeof(xx, level + 1)
        else:
            for xx in x:
                show_sizeof(xx, level + 1)

# les_3_task_3
# В массиве случайных чисел поменять местами минимальный и максимальный элемент.
# Вариант 1


from random import randint


arr = [randint(0, 100) for _ in range(10)]
print(arr)
# min_el = max_el = arr[0]
# for i, el in enumerate(arr):
#     if el < min_el:
#         min_el = el
#         min_i = i
#     if el > max_el:
#         max_el = el
#         max_i = i
# print(max_el, min_el)
# arr[min_i], arr[max_i] = arr[max_i], arr[min_i]
# print(arr)


# show_sizeof(arr)
# <class 'list'> 184 [40, 13, 74, 37, 12, 76, 68, 65, 59, 91]
# 	 <class 'int'> 28 40
# 	 <class 'int'> 28 13
# 	 <class 'int'> 28 74
# 	 <class 'int'> 28 37
# 	 <class 'int'> 28 12
# 	 <class 'int'> 28 76
# 	 <class 'int'> 28 68
# 	 <class 'int'> 28 65
# 	 <class 'int'> 28 59
# 	 <class 'int'> 28 91
# show_sizeof(min_i)
# #  <class 'int'> 28 8
# show_sizeof(min_el)
# # <class 'int'> 28 3
# show_sizeof(max_i)
# # <class 'int'> 28 2
# show_sizeof(max_el)
# # <class 'int'> 28 94
# show_sizeof(i)
# # <class 'int'> 28 9
# show_sizeof(el)
# <class 'int'> 28 7

# Вариант 2

arr[arr.index(max(arr))], arr[arr.index(min(arr))] = arr[arr.index(min(arr))], arr[arr.index(max(arr))]

# show_sizeof(arr)
# <class 'list'> 184 [55, 19, 10, 5, 75, 45, 15, 11, 86, 18]
# 	 <class 'int'> 28 40
# 	 <class 'int'> 28 13
# 	 <class 'int'> 28 74
# 	 <class 'int'> 28 37
# 	 <class 'int'> 28 12
# 	 <class 'int'> 28 76
# 	 <class 'int'> 28 68
# 	 <class 'int'> 28 65
# 	 <class 'int'> 28 59
# 	 <class 'int'> 28 91

# Третий вариант придумать не смог, простите, но я думаю и так понятно, что второй вариант самый классный!