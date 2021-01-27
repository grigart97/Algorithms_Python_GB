# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу
matrix = []
for i in range(5):
    sum_i = 0
    matrix.append([])
    for j in range(4):
        matrix[i].append(int(input('число: ')))
        sum_i += matrix[i][j]
    matrix[i].append(sum_i)
print('финальная матрица: ')
for raw in matrix:
    for el in raw:
        print(f'{el:3}', end='')
    print()
