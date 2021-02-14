# Task 1 Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из
# модуля hashlib задача считается не решённой.

from hashlib import sha1


def substr_in_str(s: str) -> int:
    s_len = len(s)
    assert s_len > 0, 'Строка не может быть пустой'  # Проверяем не пустая ли строка
    s = s.lower()  # Понижаем регистр символов
    substrs = []  # Список списков для подстрок (substrs[i][0]) и их количества в строке (substrs[i][1])
    substrs_hash = []  # Список для уникальных значений хэшей имеющихся подстрок

    for substr_len in range(1, s_len - 1):  # выбор длины подстроки с одного символа до "вся строка" - 1 (в примечаниях)
        for i in range(s_len - substr_len + 1):  # Выбираем подстроку для прохода по строке
            if sha1(s[i:i + substr_len].encode('utf-8')).hexdigest() in substrs_hash:  # если строку смотрели, следующая
                break
            substrs.append([s[i:i + substr_len], s.count(s[i:i + substr_len])])
            # добавляем подстроку и количество вхождений в исходную строку
            substrs_hash.append(sha1(s[i:i + substr_len].encode('utf-8')).hexdigest())
            # добавляем хэш строки в список проверенных
    print(*substrs, sep='\n')
    return len(substrs_hash)


print(substr_in_str('Hello, world!'))
