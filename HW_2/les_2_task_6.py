from random import randint

m = randint(0, 100)
for i in range(10):
    n = int(input('Постарайтесь угадать число: '))
    if m == n:
        print('Угадал')
        break
    elif m > n:
        print('Загаданное число больше')
    elif m < n:
        print('Загаданное число меньше')
if m != n:
    print(m)
