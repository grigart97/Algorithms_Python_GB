print('Поочереди введите две английские буквы и я вычислю расстояние между ними')
letter1 = input('Перва буква - ')
letter2 = input('Вторая буква - ')
if ord(letter1) > 122 or ord(letter2) > 122 or ord(letter1) < 97 or ord(letter2) < 97:
    print('Вы ввели не английские буквы')
else:
    print(f'Порядковые номера данных букв - {ord(letter1) - 96} & {ord(letter2) - 96},'
          f'\nколичество букв между ними - {abs(ord(letter2) - ord(letter1) - 1)}')
