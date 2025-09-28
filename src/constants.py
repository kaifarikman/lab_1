class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Попытка извлечь элемент из пустого стека")
        return self._items.pop()

    def size(self) -> int:
        return len(self._items)

    def get_two_last_elements(self):
        if self.size() < 2:
            raise IndexError("В стеке находится меньше двух элементов")
        return self.pop(), self.pop()

    def answer_(self):
        if self.size() != 1:
            raise ValueError('Oшибка: выражение содержит лишние операнды')
        return self._items[0]


def get_tokens(expression: str) -> list[str]:
    """
    Разбиваю выражение на токены. Также игнорирую скобки, так как они не нужны
    :param expression:
    :return:
    """
    expression = expression.replace('(', '')
    expression = expression.replace(')', '')
    tokens = expression.split()
    return tokens


def numbers_are_integer(a: float, b: float) -> bool:
    """
    Функция принимает два float числа
    Проверяет можно ли их сконвертить в целые
    Если да, то True. Иначе False
    :param a:
    :param b:
    :return:
    """
    return a.is_integer() and b.is_integer()


OPERATIONS: dict = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '**': lambda x, y: x ** y,
    '//': lambda x, y: x // y,
    '%': lambda x, y: x % y
}
