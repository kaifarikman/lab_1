import re

# Операции над числами
OPERATIONS: dict = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '**': lambda x, y: x ** y,
    '//': lambda x, y: x // y,
    '%': lambda x, y: x % y
}


def get_tokens(expression: str) -> list[str]:
    """
    Разбивает выражение на токены (числа и операторы).
    Удаляет скобки и проверяет корректность всех символов.
    :param expression: строка с обратной польской записью
    :return: список токенов (строк)
    :raises ValueError: если встречен некорректный символ
    """
    # Введена пустая строка
    if expression.lstrip().rstrip() == "":
        raise ValueError('Вы ничего не ввели!')
    # Удаляем скобки (они не нужны для вычисления RPN)
    expr = expression.replace('(', '').replace(')', '')

    # Регулярное выражение для чисел (целые и дробные) и операций
    pattern = r'\s*([+\-]?\d+(?:\.\d+)?|//|\*\*|[%+\-*/])'
    tokens = re.findall(pattern, expr)

    joined_tokens = ''.join(tokens)
    expr_no_spaces = expr.replace(' ', '')
    if joined_tokens != expr_no_spaces:
        invalid_chars = set(expr_no_spaces) - set(joined_tokens)
        raise ValueError(f'Некорректные символы в выражении: {" ".join(invalid_chars)}')

    return tokens


def numbers_are_integer(a: float, b: float) -> bool:
    """
    Проверяет, являются ли оба числа целыми.
    :param a: первое число
    :param b: второе число
    :return: True, если оба числа целые
    """
    return a.is_integer() and b.is_integer()
