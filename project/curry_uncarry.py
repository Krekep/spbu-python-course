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
        TypeError: If more than one argument is passed to any curried function call.
    """
    if not isinstance(arity, int) or arity < 0:
        raise ValueError("Arity must be a non-negative integer")

    @wraps(function)
    def curry(arg):
        def curried_function(*args):
            if len(args) > 1:
                raise TypeError("Each curried function should accept only one argument")

            new_args = arg_list + [args[0]]
            if len(new_args) == arity:
                return function(*new_args)

            return curry_explicit(
                lambda *rest: function(*(new_args + list(rest))), arity - len(new_args)
            )

        arg_list = [arg]
        return curried_function if arity > 1 else function(*arg_list)

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
    """
    if not isinstance(arity, int) or arity < 0:
        raise ValueError("Arity must be a non-negative integer")

    @wraps(function)
    def uncurried(*args):
        if len(args) != arity:
            raise TypeError(
                f"{function.__name__}() takes exactly {arity} positional arguments but {len(args)} were given"
            )
        result = function
        for arg in args:
            result = result(arg)
        return result

    return uncurried
