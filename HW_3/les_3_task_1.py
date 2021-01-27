# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов

arr = [i for i in range(1, 100)]
nums = {key: 0 for key in range(2, 10)}
for item in arr:
    for key in nums:
        if item % key == 0:
            nums[key] += 1

print(nums)

