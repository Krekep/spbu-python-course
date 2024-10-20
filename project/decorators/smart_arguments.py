import inspect
import copy
from typing import Callable


class Evaluated:
    """
    A class to represent evaluated arguments.

    Attributes:
        func (callable): A callable function that produces a value when invoked.
    """

    def __init__(self, func):
        self.func = func


class Isolated:
    """
    A marker class to indicate that an argument should be treated as isolated.

    Instances of this class do not hold data but are used to mark arguments
    for special handling in the smart_args decorator.
    """

    pass


def smart_args(func: Callable) -> Callable:
    """
    A decorator that processes function arguments based on their types.

    The decorator allows the use of special argument types: `Evaluated` and `Isolated`.

    Parameters:
        func (callable): The function to be wrapped by the decorator.

    Returns:
        callable: A wrapper function that manages the arguments passed to the
        original function.
    """

    sig = inspect.signature(func)
    params = sig.parameters

    def wrapper(*args, **kwargs):
        new_kwargs = kwargs
        is_any_evaluated = False
        is_any_isolated = False

        # Validate positional arguments
        for arg in args:
            assert (
                isinstance(arg, Isolated) == 0 and isinstance(arg, Evaluated) == 0
            ), "Isolated and Evaluated are not supported for positional arguments"

        # Process keyword arguments
        for name, param in params.items():
            if name in kwargs:
                if isinstance(param.default, Isolated):
                    is_any_isolated = True
                    new_kwargs[name] = copy.deepcopy(kwargs[name])
            else:
                default = param.default

                if isinstance(default, Evaluated):
                    new_kwargs[name] = default.func()
                    is_any_evaluated = True
                elif isinstance(default, Isolated):
                    raise ValueError(f"Argument '{name}' must be provided.")
                else:
                    new_kwargs[name] = default

        # Check for mixed usage of Isolated and Evaluated
        assert not (
            is_any_evaluated and is_any_isolated
        ), "The mixture of Isolated and Evaluated is not allowed"

        return func(*args, **new_kwargs)

    return wrapper
