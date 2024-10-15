from functools import wraps
from collections import OrderedDict
from typing import Callable


def cache_results(max_cache_size: int = 0):
    """
    Decorator for caching function results. Supports both positional and keyword arguments.

    Parameters:
    ----------
    max_cache_size: int
        The maximum number of recent results to cache. By default (0), caching is disabled.

    Returns:
    -------
    callable
        The decorated function with caching enabled.
    """

    def decorator(function: Callable) -> Callable:
        cache: OrderedDict = OrderedDict()

        @wraps(function)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))

            if key in cache:
                return cache[key]

            result = function(*args, **kwargs)

            if max_cache_size > 0:
                if len(cache) >= max_cache_size:
                    cache.popitem(last=False)
                cache[key] = result

            return result

        return wrapper

    return decorator
