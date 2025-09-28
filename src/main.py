from src.constants import OPERATIONS
from src.calculator import calculator_job
from typing import Optional


def main() -> float | str:
    rpn_expression: str = str(input())
    result: Optional[float] = calculator_job(
        expression=rpn_expression,
        operations=OPERATIONS
    )
    if result is None:
        return 'Ошибка!'
    return result


if __name__ == "__main__":
    print(main())
