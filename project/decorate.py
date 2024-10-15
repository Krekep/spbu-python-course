import copy
import inspect


def Isolated():
    return None


def Evaluated(func):
    return func()


def smart_args(func):
    sig = inspect.signature(func)

    def wrapper(*args, **kwargs):
        default_values = {}

        for param_name, param in sig.parameters.items():
            if param_name in kwargs:
                default_values[param_name] = kwargs[param_name]
            elif param.default != inspect.Parameter.empty:
                if isinstance(param.default, Evaluated):
                    default_values[param_name] = Evaluated(param.default.func)
                elif param.default == Isolated():
                    default_values[
                        param_name
                    ] = None  # Измените на None, а затем обработайте в следующем шаге
                else:
                    default_values[param_name] = param.default

        new_kwargs = default_values.copy()
        new_kwargs.update(kwargs)

        # Применяем deepcopy для изолированных аргументов
        for key, value in new_kwargs.items():
            if value is None:  # Это Isolated
                new_kwargs[key] = copy.deepcopy(value)

        return func(**new_kwargs)

    return wrapper


@smart_args
def check_isolation(*, d=Isolated()):
    d = copy.deepcopy(d)  # Создаем глубокую копию перед изменением
    d["a"] = 0
    return d


@smart_args
def check_evaluation(*, x=get_random_number(), y=Evaluated(get_random_number)):
    print(x, y)
