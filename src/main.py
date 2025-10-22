from src.config import OPERATIONS
from src.calculator import calculator_job


def main() -> float | str:
    """
    Основная функция: читает RPN-выражение, вычисляет результат и выводит его
    Возвращает результат или 'Ошибка!' при исключении
    """
    rpn_expression: str = str(input())
    try:
        result: float = calculator_job(
            expression=rpn_expression,
            operations=OPERATIONS
        )
    except Exception as e:
        print(e)
        return 'Ошибка!'
    print(result)
    return result


if __name__ == "__main__":
    main()
