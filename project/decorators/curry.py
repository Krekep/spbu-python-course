from functools import wraps
from typing import Callable


def curry_explicit(function: Callable, arity: int) -> Callable:
    """
    Curries a function with a specified arity.

    Parameters:
    ----------
    function: Callable
        The function to be curried.
    arity: int
        The number of arguments the original function expects.

    Returns:
    -------
    callable
        A curried version of the original function.

    Raises:
    ------
    ValueError
        If a negative arity is provided.
    TypeError
        If more arguments are passed than specified by the arity.

    """
    if arity < 0:
        raise ValueError("Arity cannot be negative")
    if arity == 0:
        return function

    numargs: int = 0

    @wraps(function)
    def curried(*args):
        nonlocal numargs
        if numargs != len(args) - 1:
            raise TypeError(f"Expected 1 argument")
        numargs += 1

        if len(args) == arity:
            return function(*args)
        if len(args) < arity:
            return lambda arg: curried(*(args + (arg,)))
        raise TypeError(f"Expected exactly {arity} arguments, but got {len(args)}")

    return curried


def uncurry_explicit(function: Callable, arity: int) -> Callable:
    """
    Uncurries a curried function with a specified arity.

    Parameters:
    ----------
    function: callable
        The curried function to be uncurried.
    arity: int
        The number of arguments the original uncurried function should expect.

    Returns:
    -------
    callable
        The uncurried version of the function.

    Raises:
    ----------
    ValueError
        If a negative arity is provided.
    TypeError
        If the number of arguments passed is not equal to the specified arity.
    """
    if arity < 0:
        raise ValueError("Arity cannot be negative")

    if arity == 0:
        return function

    @wraps(function)
    def uncurried(*args):
        if len(args) != arity:
            raise TypeError(f"Expected {arity} arguments, but got {len(args)}")
        result = function
        for arg in args:
            result = result(arg)
        return result

    return uncurried
