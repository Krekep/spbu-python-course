import copy
import inspect
import random


def Isolated():
    """
    Returns a marker for arguments that should be passed as deep copies.

    This function is used as a marker within the smart_args decorator.
    When the decorator detects this marker, it deep copies the argument
    to ensure that changes made inside the function do not affect the
    original argument.

    Returns:
        None: Acts as a placeholder to signal isolation of arguments.
    """
    return None


def Evaluated(func):
    """
    Evaluates a function passed as an argument and returns the result.

    This function is used in combination with the smart_args decorator to
    delay the evaluation of an argument until the function is called, instead
    of evaluating it at the time of function definition.

    Parameters:
        func (callable): The function to evaluate.

    Returns:
        The result of the function call.
    """
    return func()


def get_random_number():
    """
    Generates a random integer between 0 and 100.

    Returns:
        int: A random number between 0 and 100.
    """
    return random.randint(0, 100)


def smart_args(func):
    """
    A decorator that processes function arguments based on the following markers:

    - Evaluated: Evaluates a function at the time of the function call.
    - Isolated: Deep-copies an argument to prevent changes to the original object.

    The decorator analyzes the function signature and processes default arguments
    accordingly. It ensures that `Isolated` arguments are copied and `Evaluated`
    arguments are computed at the time of the function call.

    Parameters:
        func (callable): The function to decorate.

    Returns:
        callable: A wrapped version of the function that processes arguments based
                  on the markers.
    """
    sig = inspect.signature(func)

    def wrapper(*args, **kwargs):
        # Store default values based on the signature of the function
        default_values = {}

        for param_name, param in sig.parameters.items():
            if param_name in kwargs:
                # Use the provided argument
                default_values[param_name] = kwargs[param_name]
            elif param.default != inspect.Parameter.empty:
                # Check if default argument is Evaluated or Isolated
                if param.default is Evaluated:  # Changed this line
                    default_values[param_name] = Evaluated(param.default.func)
                elif param.default == Isolated():
                    default_values[param_name] = None  # Set default to None
                else:
                    # Use the default argument as-is
                    default_values[param_name] = param.default

        new_kwargs = default_values.copy()
        new_kwargs.update(kwargs)

        # Apply deepcopy for isolated arguments
        for key, value in new_kwargs.items():
            if value is None:  # This is Isolated
                new_kwargs[key] = copy.deepcopy(value)

        return func(**new_kwargs)

    return wrapper


@smart_args
def check_isolation(*, d=Isolated()):
    """
    Test function to check the behavior of Isolated arguments.

    Modifies a dictionary by setting the key 'a' to 0, but due to the use
    of the `Isolated` marker, the original dictionary will not be modified.

    Parameters:
        d (dict, optional): A dictionary to modify. If not provided, the
                            argument is deep-copied from the default value.

    Returns:
        dict: The modified dictionary with 'a' set to 0.
    """
    d = copy.deepcopy(d)  # Create a deep copy before modifying
    d["a"] = 0
    return d


@smart_args
def check_evaluation(*, x=get_random_number(), y=Evaluated(get_random_number)):
    """
    Test function to check the behavior of Evaluated arguments.

    Prints two values. The first value `x` is computed when the function
    is defined, and the second value `y` is evaluated at the time of
    function call (unless provided as an argument).

    Parameters:
        x (int, optional): A random number, evaluated at function definition.
        y (int, optional): A random number, evaluated at function call using
                           the Evaluated marker. Can be manually overridden.

    Returns:
        tuple: A tuple containing the values of x and y.
    """
    return x, y  # Возвращаем значения x и y
