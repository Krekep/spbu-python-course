from functools import wraps
from typing import Callable, Any, Dict
import inspect, copy


def make_key(args: Any, kwargs: Any) -> tuple[Any, ...]:
    """
    Generates a hashable cache key from the arguments passed to the function.
    Handles nested structures like dicts, lists, sets, and tuples by recursively
    converting them into sorted, immutable tuples.
    Args:
        args: Positional arguments of the function.
        kwargs: Keyword arguments of the function.
    Returns:
        A tuple that can be used as a unique key for the function call.
    """

    def recursive_convert(item: Any) -> Any:
        """
        Recursively converts mutable structures (like dicts, lists, sets)
        into immutable tuples to make them hashable for cache keys.
        Args:
            item: The item to be converted, which can be a dict, list, set, tuple, or any other object.
        Returns:
            An immutable version of the input.
        """

        if isinstance(item, dict):
            return tuple(
                (k, recursive_convert(v)) for k, v in sorted(item.items())
            )
        elif isinstance(item, (list, set, tuple)):
            return tuple(recursive_convert(i) for i in item)
        else:
            return item

    conv_args: tuple[Any, ...] = recursive_convert(args)
    conv_kwargs: tuple[Any, ...] = recursive_convert(kwargs)

    return conv_args + conv_kwargs


def cache_decorator(
    function: Any = None, *, cache_size: int = 0
) -> Callable[..., Any]:
    """
    Function Caching decorator.
    Args:
        function (Callable[..., Any]: the function to implement caching for.
        cache_size (int): the number of recent results for the cache.
    Returns:
        result (Callable[..., Any]: a function that supports caching.
    """
    if function is None:
        return lambda func: cache_decorator(func, cache_size=cache_size)

    dict_cache: Dict[tuple[Any, ...], Any] = {}

    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if not cache_size:
            return function(*args, **kwargs)
        key = make_key(args, kwargs)
        if key not in dict_cache:
            result = function(*args, **kwargs)
            if len(dict_cache) == cache_size:
                dict_cache.pop(next(iter(dict_cache)))
            dict_cache[key] = result
        return dict_cache[key]

    setattr(wrapper, "dict_cache", dict_cache)

    return wrapper


class Evaluated:
    """
    Substitutes the default value calculated at the time of the call. Takes as an argument a function without arguments that returns something.
    """

    def __init__(self, func: Any) -> None:
        """
        Initializes Evaluated object.
        """
        if isinstance(func, Isolated):
            raise TypeError("You cannot combine Evaluated with Isolated.")
        self.func = func

    def execute(self) -> Any:
        """
        Performs a function call.
        """
        return self.func()


class Isolated:
    """
    A dummy default value. The argument must be passed, but at the time of transmission it is copied (deep copy).
    """

    def __init__(self, value: Any = None):
        """
        Initializes Isolated object.
        """
        if isinstance(value, Evaluated):
            raise TypeError("You cannot combine Isolated with Evaluated.")


def smart_args(
    function: Any = None, position_args: bool = False
) -> Callable[..., Any]:
    """
    Decorator for analyzing arguments of the Isolated and Evaluated types.
    Args:
        function (Callable[..., Any]: a function that should support Isolated and Evaluated as default arguments.
        position_args (bool): a parameter that determines whether positional arguments need to be supported.
    Returns:
        result (Callable[..., Any]: a function that supports Isolated and Evaluated as default arguments.
    """
    if function is None:
        return lambda func: smart_args(func, position_args=position_args)

    argspec = inspect.getfullargspec(function)
    default_kwarg = argspec.kwonlydefaults
    default_args = argspec.defaults
    all_positional_args = argspec.args

    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if default_kwarg is not None:
            for key, value in default_kwarg.items():
                if key in kwargs:
                    if isinstance(value, Isolated):
                        kwargs[key] = copy.deepcopy(kwargs[key])
                elif isinstance(value, Evaluated):
                    kwargs[key] = value.execute()

        if (
            position_args
            and default_args is not None
            and all_positional_args is not None
        ):
            num_non_default_args = len(all_positional_args) - len(default_args)
            num_default_args = len(all_positional_args) - num_non_default_args

            list_args = list(args)
            for id_default_arg in range(num_default_args):
                id_args = num_non_default_args + id_default_arg
                if isinstance(default_args[id_default_arg], Isolated):
                    list_args[id_args] = copy.deepcopy(args[id_args])
                elif id_args >= len(args) and isinstance(
                    default_args[id_default_arg], Evaluated
                ):
                    list_args.append(default_args[id_default_arg].execute())
            return function(*list_args, **kwargs)
        return function(*args, **kwargs)

    return wrapper
