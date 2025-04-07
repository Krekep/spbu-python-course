from copy import deepcopy
from inspect import signature, getfullargspec
from typing import Any, Callable


class Isolated:
    """
    Маркерный класс, указывающий, что аргумент должен быть глубоко скопирован.
    """
    pass


class Evaluated:

    def __init__(self, function: Callable[..., Any]) -> None:
        """
        Класс-обертка, гарантирующий выполнение переданной функции при вызове.
        Запрещает передачу экземпляров класса Isolated.

        Args:
        function (Callable[..., Any]): Функция для обертывания.

        Raises:
        Нет.

        Returns:
        Нет возвращаемого значения.
        """

        self.function = function

    def __call__(self) -> Any:
        """
        Вызывает обернутую функцию.

        Args:
        Нет аргументов.

        Returns:
        Any: Результат выполнения обернутой функции.

        Raises:
        Нет исключений.
        """
        return self.function()


def smart_args(enable_positional: bool = False) -> Callable[..., Any]:
    """
    Декоратор для обработки аргументов функции с поддержкой специальных классов Isolated и Evaluated.

    Args:
    enable_positional (bool): Флаг разрешения позиционных аргументов (по умолчанию False).

    Returns:
    Callable[..., Any]: Декоратор с интеллектуальной обработкой аргументов.

    Raises:
    Нет исключений (на этом уровне).
    """
    def decorator(function: Callable[..., Any]) -> Callable[..., Any]:
        """
        Декоратор, обрабатывающий аргументы функции.

        Args:
        function (Callable[..., Any]): Декорируемая функция.

        Returns:
        Callable[..., Any]: Обернутая функция с обработкой аргументов.

        Raises:
        Нет исключений (на этом уровне).
        """
        sign = signature(function)
        argspec = getfullargspec(function)

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Обрабатывает аргументы функции, выполняя глубокое копирование для Isolated и вызов для Evaluated.

            Args:
            *args (Any): Позиционные аргументы.
            **kwargs (Any): Именованные аргументы.

            Raises:
            TypeError: При передаче позиционных аргументов, когда они отключены.
            ValueError: Если не передан обязательный аргумент с Isolated.
            TypeError: При дублировании аргументов.

            Returns:
            Any: Результат выполнения декорированной функции.
            """
            if not enable_positional and args:
                raise TypeError("Positional arguments are disabled for this function")

            if enable_positional and args:
                positional_params = argspec.args[:len(args)]
                for name, value in zip(positional_params, args):
                    if name in kwargs:
                        raise TypeError(f"Got multiple values for argument '{name}'")
                    kwargs[name] = value

            for key, value in sign.parameters.items():
                if isinstance(value.default, Isolated):
                    if key not in kwargs:
                        raise ValueError(
                            f"Argument '{key}' must be provided when using Isolated()"
                        )
                    kwargs[key] = deepcopy(kwargs[key])
                if isinstance(value.default, Evaluated):
                    if key not in kwargs:
                        kwargs[key] = value.default()

            return function(**kwargs)

        return wrapper
    return decorator