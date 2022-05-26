"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""


import collections
import operator


class Leaf:
    """ Вспомогательный класс Лист для создания дерева Хаффмана
        char - символ из кодируемой строки
        value - частота буквы в строке
    """

    def __init__(self, char: str, *value: int):
        if isinstance(char, tuple):
            self.char, self.value = char
        else:
            self.char = char
            self.value = value

    def __repr__(self):
        return f'Leaf: char "{self.char}" value {self.value}'


class Node:
    """ Вспомогательный класс Узел для построения дерева Хаффмана """

    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node: value {self.value} \nleft->{self.left} \nright->{self.right}'


class Haffman:
    """ Основной класс для реализации алгоритма Хаффмана """

    def __init__(self):
        self._code_table = {}

    def _get_table(self, tree, code=''):
        """ Рекурсивный обход дерева и построение таблицы кодирования """
        if isinstance(tree, Node):
            self._get_table(tree.left, code=f'{code}0')
            self._get_table(tree.right, code=f'{code}1')
        elif isinstance(tree, Leaf):
            self._code_table[tree.char] = code

    def encode(self, string, detail=False):
        """ Main метод для кодирования строки """
        self._code_table = {}
        count = collections.Counter(string)
        leaf_deque = collections.deque(map(Leaf, count.most_common()))
        if detail:
            print(leaf_deque)    # deque из листьев

        while len(leaf_deque) > 1:  # формируем дерево
            leaf_deque = collections.deque(sorted(leaf_deque, key=operator.attrgetter('value')))
            leaf_small = leaf_deque.popleft()
            leaf_bigger = leaf_deque.popleft()
            leaf_deque.append(Node(leaf_small.value + leaf_bigger.value, leaf_small, leaf_bigger))

        tree = leaf_deque.pop()
        if detail:
            print(tree)  # дерево Хаффмана

        self._get_table(tree)
        if detail:
            print(self._code_table)  # таблица кодирования

        return ' '.join([self._code_table[char] for char in string])


if __name__ == '__main__':
    haf = Haffman()
    my_str = input('Введите строку для кодирования: ')
    print(haf.encode(my_str, detail=True))
