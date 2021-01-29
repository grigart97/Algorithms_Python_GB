# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
import cProfile


# def test_sum(func):
#     _sum = [1, 0.5, 0.75, 0.625, 0.6875, 0.65625]
#     for i, el in enumerate(_sum):
#         assert el == func(i)
#         print(f'{i} tested - OK')


def sum_n1(n):
    _sum = 0
    for i in range(n + 1): # считаю, что 1 - нулевой элемент
        _sum += 1 * (-0.5) ** i
    return _sum

# les_3_task_1.sum_n1(10)"
# 1000 loops, best of 5: 2.77 usec per loop

# "les_3_task_1.sum_n1(15)"
# 1000 loops, best of 5: 4 usec per loop

# "les_3_task_1.sum_n1(20)"
# 1000 loops, best of 5: 5.24 usec per loop

# "les_3_task_1.sum_n1(100)"
# 1000 loops, best of 5: 26.9 usec per loop

# "les_3_task_1.sum_n1(1000)"
# 1000 loops, best of 5: 286 usec per loop


def sum_n2(n):
    if n == 0:
        return 1
    return sum_n2(n - 1) + sum_n2(0) * (-0.5) ** n

# "les_3_task_1.sum_n2(10)"
# 1000 loops, best of 5: 3.93 usec per loop

# "les_3_task_1.sum_n2(15)"
# 1000 loops, best of 5: 5.92 usec per loop

# "les_3_task_1.sum_n2(20)"
# 1000 loops, best of 5: 7.87 usec per loop

# "les_3_task_1.sum_n2(50)"
# 1000 loops, best of 5: 20.7 usec per loop

# "les_3_task_1.sum_n2(100)"
# 1000 loops, best of 5: 42.3 usec per loop

# "les_3_task_1.sum_n2(1000)"
# maximum recursion depth exceeded in comparison

# Сорри, не смог придумать третий вариант... Впринципе понятно, что первый вариант гораздо лучше,
# потому что второй - рекурсивный, а значит кушает много памяти, имеет ограничения
# + судя по отчётам timeit ещё и дольше выполняется
