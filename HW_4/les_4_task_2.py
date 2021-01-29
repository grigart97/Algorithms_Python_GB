# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
import cProfile

n = 10000


def eratosfen(m):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    count = 0
    for i in range(2, n):
        if sieve[i] != 0:
            count += 1
            if count == m:
                return  i
            for j in range(i * 2, n, i):
                sieve[j] = 0
    return 'Not Found'

# "les_4_task_2.eratosfen(4)" - для чисел от 1 до 1000
# 1000 loops, best of 5: 80.4 usec per loop

# "les_4_task_2.eratosfen(8)" - для чисел от 1 до 1000
# 1000 loops, best of 5: 95.9 usec per loop

# "les_4_task_2.eratosfen(12)" - для чисел от 1 до 1000
# 1000 loops, best of 5: 105 usec per loop

# "les_4_task_2.eratosfen(36)" - для чисел от 1 до 1000
# 1000 loops, best of 5: 131 usec per loop

# "les_4_task_2.eratosfen(36)" - для чисел от 1 до 10000
# 1000 loops, best of 5: 1.34 msec per loop


def not_eratosfen(m):
    def easy_n(num):
        for i in range(2, num):
            if sieve[num] % i == 0:
                return False
        else:
            return True

    sieve = [i for i in range(n)]
    sieve[1] = 0
    count_m = 0
    for i in range(2, n):
        if easy_n(i):
            count_m += 1
            if count_m == m:
                return i

# "les_4_task_2.not_eratosfen(4)" - для чисел от 1 до 1000
# 1000 loops, best of 5: 33.5 usec per loop

# "les_4_task_2.not_eratosfen(8)" - для чисел от 1 до 1000
# 1000 loops, best of 5: 40.5 usec per loop

# "les_4_task_2.not_eratosfen(12)" - для чисел от 1 до 1000
# 1000 loops, best of 5: 55 usec per loop

# "les_4_task_2.not_eratosfen(36)" - для чисел от 1 до 1000
# 1000 loops, best of 5: 247 usec per loop

# "les_4_task_2.not_eratosfen(36)" - для чисел от 1 до 10000
# 1000 loops, best of 5: 550 usec per loop

# print(eratosfen(12))
