import pytest
from unittest.mock import Mock
from project.Decorators.cache import cache

def test_cache_fibonacci():
    @cache(max_size=3)
    def fibonacci(n):
        if n < 2:
            return n
        result = fibonacci(n - 1) + fibonacci(n - 2)
        return result

    for i in range(0, 2000):
        fibonacci(i)

    fibonacci(1999)
    fibonacci(1998)
    fibonacci(1997)
    with pytest.raises(RecursionError):
        fibonacci(3000)
    with pytest.raises(RecursionError):
        fibonacci(1996)


def test_no_cache_calls():
    mock_func = Mock(side_effect=lambda x: x * 2)

    @cache()
    def cached_func(*args, **kwargs):
        return mock_func(*args, **kwargs)

    cached_func(2)
    cached_func(2)
    cached_func(3)

    assert mock_func.call_count == 3


def test_cache_calls_with_limit():
    mock_func = Mock(side_effect=lambda x: x * 2)

    @cache(max_size=2)
    def cached_func(*args, **kwargs):
        return mock_func(*args, **kwargs)

    cached_func(2)
    cached_func(2)
    cached_func(3)
    cached_func(2)

    assert mock_func.call_count == 2


def test_cache_eviction():
    mock_func = Mock(side_effect=lambda x: x * 2)

    @cache(max_size=2)
    def cached_func(*args, **kwargs):
        return mock_func(*args, **kwargs)

    cached_func(2)  
    cached_func(3)  
    cached_func(4)  
    cached_func(2)  

    assert mock_func.call_count == 4


def test_cache_with_kwargs():
    mock_func = Mock(side_effect=lambda x: x * 2)

    @cache(max_size=2)
    def cached_func(*args, **kwargs):
        return mock_func(*args, **kwargs)

    cached_func(x=5) 
    cached_func(x=5)  
    cached_func(x=6)  

    assert mock_func.call_count == 2