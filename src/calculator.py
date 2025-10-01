from src.stack import Stack
from src.constants import get_tokens, numbers_are_integer


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
