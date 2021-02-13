import random

size = 10
arr = [i for i in range(size)]
random.shuffle(arr)
print(arr)


def shell_sort(array):
    def new_inc(array):
        incs = [1, 4, 10, 23, 57, 132, 701, 1750]
        while len(array) <= incs[-1]:
            incs.pop()
        while len(incs) > 0:
            yield incs.pop()
    for inc in new_inc(array):
        for i in range(inc, len(array)):
            for j in range(i, inc - 1, -inc):
                if array[j - inc] <= array[j]:
                    break
                array[j], array[j - inc] = array[j - inc], array[j]


def quick_sort_nomem(array, fst, lst):
    if fst >= lst:
        return
    print(array)
    pivot = array[random.randint(fst, lst)]
    i, j = fst, lst
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    quick_sort_nomem(array, fst, j)
    quick_sort_nomem(array, i, lst)


# shell_sort(arr)
quick_sort_nomem(arr, 0, len(arr) - 1)
print(arr)
