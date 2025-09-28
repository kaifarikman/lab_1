from typing import Optional
from src.constants import Stack
from src.constants import get_tokens
from src.constants import numbers_are_integer


def calculator_job(expression: str, operations: dict) -> Optional[float]:
    stack = Stack()
    tokens: list[str] = get_tokens(expression)
    for token in tokens:
        if token in operations:
            '''Токен является операцией'''
            try:
                a, b = stack.get_two_last_elements()
                match token:
                    case token_ if token_ == '//' or token_ == "%":
                        if numbers_are_integer(b, a):
                            result = operations[token_](b, a)
                            stack.push(result)
                        else:
                            raise ValueError('Операции "//" и "%" доступны только на целых числах')
                    case _:
                        result = operations[token](b, a)
                        stack.push(result)
            except IndexError:
                raise IndexError("Ошибка: недостаточно операндов для оператора")
            except ZeroDivisionError:
                raise ZeroDivisionError("Ошибка: деление на ноль")
        else:
            '''Токен не является операцией. Или число, или не число'''
            try:
                token_is_numer = float(token)
                stack.push(token_is_numer)
            except ValueError:
                raise ValueError(f'Ошибка токена. Символ "{token}" не был обработан')
    return stack.answer()
