from src.constants import OPERATIONS
from src.calculator import calculator_job


def main() -> float | str:
    rpn_expression: str = str(input())
    try:
        result: float = calculator_job(
            expression=rpn_expression,
            operations=OPERATIONS
        )
    except Exception as e:
        print(f"Ошибка: {e}")
        return 'Ошибка!'
    print(result)
    return result


if __name__ == "__main__":
    main()
