# Определить, какое число в массиве встречается чаще всего

from random import randint

n = 10
arr = [randint(0, 7) for _ in range(n)]
print(arr)
q_nums = {i: 0 for i in set(arr)}
for i in arr:
    for key in q_nums.keys():
        if i == key:
            q_nums[key] += 1
print(q_nums)
max_q_num = 0
for key in q_nums.keys():
    if q_nums[max_q_num] < q_nums[key]:
        max_q_num = key
print(f'число {max_q_num} встречается чаще всего')
