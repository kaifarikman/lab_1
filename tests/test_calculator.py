import pytest
from src.calculator import calculator_job
from src.constants import OPERATIONS


def test_basic_arithmetic():
    assert calculator_job("3 4 +", OPERATIONS) == 7.0
    assert calculator_job("10 5 -", OPERATIONS) == 5.0
    assert calculator_job("2 3 *", OPERATIONS) == 6.0
    assert calculator_job("8 2 /", OPERATIONS) == 4.0


def test_power_and_composed_expression():
    assert calculator_job("2 3 **", OPERATIONS) == 8.0
    assert calculator_job("3 4 2 * +", OPERATIONS) == 11.0


def test_integer_div_and_mod_with_integers():
    assert calculator_job("7 2 //", OPERATIONS) == 3.0
    assert calculator_job("7 3 %", OPERATIONS) == 1.0


def test_integer_div_and_mod_reject_non_integer_operands():
    with pytest.raises(ValueError):
        calculator_job("7.5 2 //", OPERATIONS)
    with pytest.raises(ValueError):
        calculator_job("7 2.1 %", OPERATIONS)


def test_division_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        calculator_job("3 0 /", OPERATIONS)
    with pytest.raises(ZeroDivisionError):
        calculator_job("3 0 //", OPERATIONS)
    with pytest.raises(ZeroDivisionError):
        calculator_job("3 0 %", OPERATIONS)


def test_insufficient_operands_raises():
    with pytest.raises(IndexError):
        calculator_job("+", OPERATIONS)
    with pytest.raises(IndexError):
        calculator_job("1 +", OPERATIONS)


def test_invalid_token_raises():
    with pytest.raises(ValueError):
        calculator_job("3 a +", OPERATIONS)


def test_extra_operands_leftover_raises():
    with pytest.raises(ValueError):
        calculator_job("3 4", OPERATIONS)
