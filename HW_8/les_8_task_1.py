# Task 1 На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.


from collections import deque


def handshaking_counts(friends_num):
    is_shacked = [[False for _ in range(friends_num)] for _ in range(friends_num)]  # формируем матрицу рукопожатий
    for i in range(friends_num):
        is_shacked[i][i] = True  # Не даём возможность пожимать руку самим себе
    shaking_count = 0  # счётчик рукопожатий
    friends = deque([0])  # Очередь друзей на рукопожатие
    while len(friends) > 0:
        current = friends.pop()  # Выбираем друга
        for i, shook in enumerate(is_shacked[current]):  # Рукопожатие с каждым другом
            if not shook:  # Если до этого между ними не было рукопожатия
                shaking_count += 1
                is_shacked[current][i], is_shacked[i][current] = True, True
                friends.appendleft(i)
    return shaking_count


def handshaking_counts_alternative(friends_num):
    shaking_count = 0
    for i in range(friends_num):  # считаем все ячейки под диагональю матрицы
        shaking_count += 1 * i
    return shaking_count


print(handshaking_counts(int(input('Введите количество друзей: '))))
print(handshaking_counts_alternative(5))


