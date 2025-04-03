from typing import Callable, Any
from functools import wraps


def curry_explicit(
    function: Callable[..., Any], arity: int
) -> Callable[..., Any]:
    """
    A function for currying an accepted function.
    Args:
        function (Callable[..., Any]: the function that needs to be curried.
        arity (int): the number of arguments for the curried function.
    Returns:
        result (Callable[..., Any]: a function that supports currying.
    """
    if arity < 0:
        raise TypeError("Input must be a non-negative numeric.")

    @wraps(function)
    def wrapper(*args: Any) -> Any:
        if len(args) == arity:
            return function(*args)
        return lambda *next_args: wrapper(*(args + next_args))

    return wrapper


def uncurry_explicit(
    function: Callable[..., Any], arity: int
) -> Callable[..., Any]:
    """
    A function for uncurrying an accepted function.
    Args:
        function (Callable[..., Any]: the function that needs to be uncurried.
        arity (int): the number of arguments for the curried function.
    Returns:
        result (Callable[..., Any]: a function that accepts a list of arguments.
    """
    if arity < 0:
        raise TypeError("Input must be a non-negative numeric.")

    @wraps(function)
    def wrapper(*args: Any) -> Any:
        if len(args) != arity:
            raise ValueError(
                "More parameters are passed than the arity of the function."
            )

        if not args:
            return function()

        res = function
        for arg in args:
            res = res(arg)
        return res

    return wrapper
