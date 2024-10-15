import pytest
from project.decorate import (
    smart_args,
    Isolated,
    Evaluated,
    check_isolation,
    check_evaluation,
)


def test_check_isolation():
    """Тест для проверки работы аргумента Isolated."""
    no_mutable = {"a": 10}
    result = check_isolation(d=no_mutable)
    assert result == {"a": 0}  # Проверка, что возвращается {'a': 0}
    assert no_mutable == {"a": 10}  # Проверка, что исходный словарь не изменился


def test_check_evaluation():
    """Тест для проверки работы аргумента Evaluated."""
    result1 = check_evaluation()  # Теперь result1 будет кортежем (x, y)
    assert result1[0] != result1[1]  # Проверка, что значения разные
