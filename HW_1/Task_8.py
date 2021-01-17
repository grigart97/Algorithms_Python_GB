print('Введите поочередно три числа и я найду среднее из них (не максимально/минимальное')
a = int(input('Первное число - '))
b = int(input('Второе число - '))
c = int(input('Третье число - '))
if a == max(a,b,c) or a == min(a,b,c):
    if b == max(a,b,c) or b == min(a,b,c):
        print(f'Среднее из них - {c}')
    else:
        print(f'Среднее из них - {b}')
else:
    print(f'Среднее из них - {a}')
