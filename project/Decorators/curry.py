from typing import Callable, Any, Tuple


def curry_explicit(function: Callable, arity: int) -> Callable:
    """
    Преобразует функцию в каррированную версию с заданной арностью.

    Каррированная функция позволяет частичное применение аргументов. Если передано достаточно аргументов (равных арности функции), функция выполняется. В противном случае возвращается новая функция, ожидающая оставшиеся аргументы.

    Args:
    function (Callable): Функция для каррирования.
    arity (int): Количество аргументов, которые ожидает функция (её арность).

    Returns:
    Callable: Каррированная версия исходной функции.

    Raises:
    ValueError: Если арность отрицательная.
    TypeError: Если передано слишком много аргументов.
    """
    if arity == 0:
        return function
    if arity < 0:
        raise ValueError("Arity must be a non-negative integer")

    def inner_curry(args: Tuple[Any, ...]) -> Callable:
        """
        Внутренняя функция для каррирования, которая накапливает аргументы.

        Args:
        args (Tuple[Any, ...]): Кортеж уже накопленных аргументов.

        Returns:
        Callable: Либо результат выполнения функции (если аргументов достаточно), либо новую функцию для приёма следующего аргумента.
        """
        if len(args) == arity:
            return function(*args)
        else:
            return lambda arg: inner_curry(args + (arg,))

    return inner_curry(())



def uncurry_explicit(function: Callable, arity: int) -> Callable:
    """
    Преобразует каррированную функцию обратно в некаррированную версию с заданной арностью.

    Args:
    function (Callable): Каррированная функция для преобразования.
    arity (int): Количество аргументов, которые ожидает функция (её арность).

    Returns:
    Callable: Некаррированная версия исходной функции.

    Raises:
    ValueError: Если арность отрицательная или количество аргументов не совпадает.
    TypeError: Если переданные аргументы не соответствуют ожиданиям функции.
    """
    if arity < 0:
        raise ValueError("Arity must be a non-negative integer")
    if arity == 0:
        return function()

    def inner_uncurry(*args: Any) -> Any:
        """
        Внутренняя функция, которая применяет все аргументы сразу.

        Args:
        *args (Any): Переданные аргументы.

        Returns:
        Any: Результат выполнения исходной каррированной функции.

        Raises:
        ValueError: Если количество аргументов не совпадает с арностью.
        """
        if len(args) != arity:
            raise ValueError(f"Expected {arity} arguments, but got {len(args)}")

        result = function
        for arg in args:
            result = result(arg)
        return result

    return inner_uncurry