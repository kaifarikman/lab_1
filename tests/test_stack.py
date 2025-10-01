import pytest
from src.stack import Stack


def test_push_pop_and_size():
    s = Stack()
    assert s.is_empty() is True
    s.push(1.5)
    s.push(2.5)
    assert s.size() == 2
    assert s.pop() == 2.5
    assert s.pop() == 1.5
    assert s.is_empty() is True


def test_pop_from_empty_raises():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()


def test_get_two_last_elements():
    s = Stack()
    s.push(1)
    s.push(2)
    a, b = s.get_two_last_elements()
    assert (a, b) == (2, 1)
    assert s.is_empty() is True


def test_get_two_last_with_error():
    s = Stack()
    s.push(1)
    with pytest.raises(IndexError):
        s.get_two_last_elements()
