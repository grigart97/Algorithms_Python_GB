'''
Task 2 Закодируйте любую строку по алгоритму Хаффмана.
'''
import heapq  # для работы с кучей
from collections import namedtuple, Counter  #


class Node(namedtuple('Node', ['left', 'right'])):  # Класс для узла

    def search_code(self, code, path):  # Функция для прохода по дереву
        self.left.search_code(code, path + '0')
        self.right.search_code(code, path + '1')


class Leaf(namedtuple('Leaf', ['char'])):  # Класс для листа (символа)

    def search_code(self, code, path):  # функция для прохода по дереву
        code[self.char] = path or '0'


def haffmanita(s: str) -> dict:
    assert len(s) > 0, 'Строка не может быть пустой'
    tree_s = []  # Список списков для символов и количества их вхождения в строку
    for char, freq in Counter(s).items():  # считаем количетсво вхождений для каждого уникального символа в строке
        tree_s.append((freq, len(tree_s), Leaf(char)))  # Добавляем объект лист (символ) и количество вхождений в дерево
    heapq.heapify(tree_s)  # Превращаем список к кучу, чтобы вычлинять минимальные элементы вместо постоянной сортировки
    count = len(tree_s)
    while len(tree_s) > 1:  # Пока не дойдём до корня root
        freq1, _count1, left = heapq.heappop(tree_s)  # Берём минимальный элемент (минимальный по количеству вхождений)
        freq2, _count2, right = heapq.heappop(tree_s)  # Берём второй минимальный элемент
        heapq.heappush(tree_s, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if tree_s:
        [(_freq, _count, root)] = tree_s
        root.search_code(code, '')
    return code


haffman_code = haffmanita('beep boop beer!')
print(*haffman_code.items(), sep='\n')
# Он выводит код не такой как на уроке, так как вес узлов/символов в некоторых выборках одинаковый