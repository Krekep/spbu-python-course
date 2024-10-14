from functools import wraps


def curry_explicit(function, arity):
    """
    Transforms a function into a curried version with a specified arity.

    Currying is the process of transforming a function that takes multiple arguments
    into a series of functions that each take a single argument.

    Parameters:
        function (callable): The function to be curried.
        arity (int): The number of arguments the function expects (its arity).

    Returns:
        callable: A curried version of the original function that can be called
                  successively with single arguments until all arguments are provided.

    Raises:
        ValueError: If arity is not a non-negative integer.
        TypeError: If more than the expected number of arguments is passed at once.

    Example:
        f = curry_explicit(lambda x, y, z: f"<{x},{y},{z}>", 3)
        f(1)(2)(3)  # Returns: "<1,2,3>"
    """
    if not isinstance(arity, int) or arity < 0:
        raise ValueError("Arity must be a non-negative integer")

    @wraps(function)
    def curry(*args):
        if len(args) > arity:
            raise TypeError(
                f"{function.__name__}() takes {arity} positional arguments but {len(args)} were given"
            )

        if len(args) == arity:
            return function(*args)

        def curried(*more_args):
            return curry(*(args + more_args))

        return curried

    return curry


def uncurry_explicit(function, arity):
    """
    Transforms a curried function back into a regular function with a specified arity.

    Uncurrying is the reverse of currying, where a function that takes arguments in a
    series of function calls is transformed back into a function that takes all arguments
    at once.

    Parameters:
        function (callable): The curried function to be uncurried.
        arity (int): The number of arguments the original function expects.

    Returns:
        callable: A function that accepts all arguments at once.

    Raises:
        ValueError: If arity is not a non-negative integer.
        TypeError: If the uncurried function is called with an incorrect number of arguments.

    Example:
        f_curried = curry_explicit(lambda x, y, z: f"<{x},{y},{z}>", 3)
        f_uncurried = uncurry_explicit(f_curried, 3)
        f_uncurried(1, 2, 3)  # Returns: "<1,2,3>"
    """
    if not isinstance(arity, int) or arity < 0:
        raise ValueError("Arity must be a non-negative integer")

    @wraps(function)
    def uncurried(*args):
        if len(args) != arity:
            raise TypeError(
                f"{function.__name__}() takes exactly {arity} positional arguments but {len(args)} were given"
            )
        return function(*args)

    return uncurried


# Example usage
f2 = curry_explicit((lambda x, y, z: f"<{x},{y},{z}>"), 3)
g2 = uncurry_explicit(f2, 3)

# Testing the curried function
print(f2(123)(456)(562))  # Output: "<123,456,562>"

# Testing the uncurried function
print(g2(123, 456, 562))  # Output: "<123,456,562>"
