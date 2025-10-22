from src.stack import Stack
import re


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
    # Меняем \t на пробелы, так как пользователь может ввести любое количество пробелов
    expr = expr.replace('\t', ' ')
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


def calculator_job(expression: str, operations: dict) -> float:
    """
    Вычисляет значение выражения в обратной польской нотации (RPN).
    :param expression: строка в RPN
    :param operations: словарь функций операций
    :return: результат вычисления как float
    :raises IndexError: если недостаточно операндов для операции
    :raises ZeroDivisionError: если деление на ноль
    :raises ValueError: при недопустимом токене или оставшихся лишних операндах
    """
    stack = Stack()
    tokens = get_tokens(expression)
    for token in tokens:
        if token in operations:
            try:
                a, b = stack.get_two_last_elements()
                # Для целочисленных операций оба операнда должны быть целыми
                if token == '//' or token == '%':
                    if numbers_are_integer(b, a):
                        result = operations[token](b, a)
                        stack.push(result)
                    else:
                        raise ValueError('Операции "//" и "%" доступны только на целых числах')
                else:
                    # Обычная операция (сложение, вычитание, умножение и т.д.)
                    result = operations[token](b, a)
                    stack.push(result)
            except IndexError:
                raise IndexError("Ошибка: недостаточно операндов для оператора")
            except ZeroDivisionError:
                raise ZeroDivisionError("Ошибка: деление на ноль")
        else:
            try:
                number = float(token)
                stack.push(number)
            except ValueError:
                raise ValueError(f'Ошибка токена. Символ "{token}" не был обработан')
    return stack.answer()
