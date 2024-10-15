import copy
import inspect
import random


def Isolated():
    """Returns a marker for arguments that should be passed as deep copies."""
    return None


def Evaluated(func):
    """Evaluates a function passed as an argument and returns the result."""
    return func()


def smart_args(func):
    """
    A decorator that processes function arguments based on the following markers:

    - Evaluated: Evaluates a function at the time of the function call.
    - Isolated: Deep-copies an argument to prevent changes to the original object.
    """
    sig = inspect.signature(func)

    def wrapper(*args, **kwargs):
        # Store default values based on the signature of the function
        default_values = {}

        for param_name, param in sig.parameters.items():
            if param_name in kwargs:
                default_values[param_name] = kwargs[param_name]
            elif param.default != inspect.Parameter.empty:
                if isinstance(param.default, Evaluated):
                    default_values[param_name] = Evaluated(param.default.func)
                elif param.default == Isolated():
                    default_values[param_name] = copy.deepcopy(param.default)
                else:
                    default_values[param_name] = param.default

        new_kwargs = default_values.copy()
        new_kwargs.update(kwargs)

        return func(**new_kwargs)

    return wrapper


@smart_args
def check_isolation(*, d=Isolated()):
    """Test function to check the behavior of Isolated arguments."""
    d["a"] = 0
    return d


def get_random_number():
    """Generates a random integer between 0 and 100."""
    return random.randint(0, 100)


@smart_args
def check_evaluation(*, x=get_random_number(), y=Evaluated(get_random_number)):
    """Test function to check the behavior of Evaluated arguments."""
    return x, y
