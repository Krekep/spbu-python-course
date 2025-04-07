from functools import wraps
from collections import OrderedDict
from typing import Callable, Any, Tuple


def cache(max_size: int = 0) -> Callable[[Callable], Callable]:
    """
    Декоратор для кэширования результатов функции с ограничением по размеру кэша.

    Args:
    max_size (int): Максимальный размер кэша. Если 0, кэширование отключено.
    Должен быть неотрицательным числом.

    Returns:
    Callable[[Callable], Callable]: Декоратор, который принимает функцию и возвращает
    её обертку с кэшированием.

    Raises:
    ValueError: Если max_size отрицательное число.
    """
    
    if max_size < 0:
        raise ValueError("max_size must be a non-negative integer")

    def cache_inner(function: Callable) -> Callable:
        """
        Внутренняя функция декоратора, реализующая кэширование.

        Args:
        function (Callable): Функция, которую нужно обернуть для кэширования.

        Returns:
        Callable: Обертка функции с добавленной логикой кэширования.

        Raises:
        Нет исключений.
        """
        cached: OrderedDict[Tuple[Tuple[Any, ...], frozenset], Any] = OrderedDict()

        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Обертка функции, выполняющая кэширование результатов.

            Args:
            *args (Any): Позиционные аргументы исходной функции.
            **kwargs (Any): Именованные аргументы исходной функции.

            Returns:
            Any: Результат выполнения функции (либо из кэша, либо новый результат).

            Raises:
            Нет исключений.
            """
            cache_key = (args, frozenset(kwargs.items()))
            
            if cache_key in cached:
                return cached[cache_key]

            result = function(*args, **kwargs)
            
            if max_size > 0:
                if len(cached) >= max_size and max_size > 0:
                    cached.popitem(last=False)
                cached[cache_key] = result

            return result

        return wrapper

    return cache_inner