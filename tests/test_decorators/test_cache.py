import pytest
from project.decorators.cache import cache_results


def create_add_function_with_counter():
    call_counter = 0

    @cache_results(max_cache_size=2)
    def add_with_counter(a, b):
        nonlocal call_counter
        call_counter += 1
        return a + b

    return add_with_counter, lambda: call_counter


def create_div_function_with_counter():
    call_counter = 0

    @cache_results(max_cache_size=2)
    def divide(x=1, y=1):
        nonlocal call_counter
        call_counter += 1
        return x / y

    return divide, lambda: call_counter


def test_cache_hits():
    add, get_call_counter = create_add_function_with_counter()

    add(1, 2)
    assert get_call_counter() == 1

    add(1, 2)
    assert get_call_counter() == 1

    add(2, 3)
    assert get_call_counter() == 2

    add(1, 2)
    assert get_call_counter() == 2


def test_cache_eviction_with_counter():
    add, get_call_counter = create_add_function_with_counter()

    add(4, 6)
    assert get_call_counter() == 1

    add(8, 10)

    assert get_call_counter() == 2

    add(12, 14)
    assert get_call_counter() == 3

    add(4, 6)
    assert get_call_counter() == 4


def test_cache_with_kwargs():

    div, get_call_counter = create_div_function_with_counter()

    div(x=10, y=2)
    assert get_call_counter() == 1

    div(x=10, y=2)
    assert get_call_counter() == 1

    div(x=2, y=10)
    assert get_call_counter() == 2

    div(y=2, x=10)
    assert get_call_counter() == 2
