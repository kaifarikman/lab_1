class Stack:
    """
    Класс Stack реализует стек для хранения чисел и основные операции над ним.
    """

    def __init__(self) -> None:
        self._items = []

    def is_empty(self) -> bool:
        """Проверяет, пуст ли стек."""
        return len(self._items) == 0

    def push(self, item) -> None:
        """Добавляет элемент в верхнюю часть стека."""
        self._items.append(item)

    def pop(self) -> float:
        """
        Извлекает верхний элемент из стека.
        :raises IndexError: если стек пуст.
        """
        if self.is_empty():
            raise IndexError("Попытка извлечь элемент из пустого стека")
        return self._items.pop()

    def size(self) -> int:
        """Возвращает текущее количество элементов в стеке."""
        return len(self._items)

    def get_two_last_elements(self) -> (float, float):
        """
        Извлекает и возвращает два последних элемента из стека.
        :raises IndexError: если в стеке меньше двух элементов.
        """
        if self.size() < 2:
            raise IndexError("В стеке находится меньше двух элементов")
        left = self.pop()
        right = self.pop()
        return left, right

    def answer(self) -> float:
        """
        Возвращает единственный оставшийся элемент как результат.
        :raises ValueError: если после обработки выражения в стеке больше или меньше одного элемента.
        """
        if self.size() != 1:
            raise ValueError("Ошибка: выражение содержит лишние операнды")
        return float(self._items[0])
