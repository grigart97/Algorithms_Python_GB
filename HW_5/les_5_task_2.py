from collections import deque


hex_values = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
tens_values = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def equal_check(num1, num2):  # Проверка на одинаковое количество символов, если нет, добавляем нули
    if len(num1) > len(num2):
        for _ in range(len(num1) - len(num2)):
            num2.appendleft('0')
    elif len(num2) > len((num1)):
        for _ in range(len(num2) - len(num1)):
            num1.appendleft('0')
    return num1, num2


def hex_sum(num1, num2):  # Сумма шестнадцатиричных чисел
    num1, num2 = equal_check(num1, num2)
    sum_num = deque()
    for_next_sum = 0  # Для суммы со следующим разрядом, если текущий больше 16
    for i in range(len(num1) - 1, -1, -1):
        sum_i = (hex_values.get(num1[i]) if num1[i].isalpha() else int(num1[i])) + \
                (hex_values.get(num2[i]) if num2[i].isalpha() else int(num2[i])) + for_next_sum
        for_next_sum = sum_i // 16
        sum_num.appendleft(str(sum_i % 16)) if sum_i % 16 < 10 else sum_num.appendleft(tens_values.get(sum_i % 16))
    return sum_num


def hex_mul(num1, num2):
    result_num = deque('0') * (len(num1) + len(num2))  # создаю очередь для формирования конечного результата
    for i in range(len(num1) - 1, -1, -1):
        for_nex_i = 0
        mul_num = deque()
        digit1 = hex_values.get(num1[i]) if num1[i].isalpha() else int(num1[i])
        for j in range(len(num2) - 1, -1, -1):
            digit2 = hex_values.get(num2[j]) if num2[j].isalpha() else int(num2[j])
            mul_i = digit1 * digit2 + for_nex_i
            for_nex_i = mul_i // 16
            mul_num.appendleft(str(mul_i % 16)) if mul_i % 16 < 10 else mul_num.appendleft(tens_values.get(mul_i % 16))
        if for_nex_i:
            mul_num.appendleft(str(for_nex_i))
        mul_num.extend(['0'] * (len(num1) - 1 - i))
        result_num = hex_sum(result_num, mul_num)
    for item in result_num.copy(): #  Удаляю лишние нули перед числом
        if item == '0':
            result_num.remove(item)
        else:
            break
    return result_num


inp_lst = input('Введите пример для решения в формате (число1) (+ или *) (число2):\n').split()
a = deque(inp_lst[0].upper())
b = deque(inp_lst[-1].upper())
if inp_lst[1] == '+':
    print(hex_sum(a, b))
elif inp_lst[1] == '*':
    print(hex_mul(a, b))
