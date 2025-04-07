from typing import Generator, Tuple, Optional, Callable


def rgba_gen() -> Generator[Tuple[int, int, int, int], None, None]:
    """
    Генератор всех возможных RGBA цветовых комбинаций.

    Args:
    Нет аргументов.

    Returns:
    Generator[Tuple[int, int, int, int], None, None]: Генератор, который возвращает кортежи с значениями RGBA.
    - r: Красный канал (0-255)
    - g: Зеленый канал (0-255)
    - b: Синий канал (0-255)
    - a: Альфа-канал (0-100 с шагом 2)

    Raises:
    Нет исключений.
    """
    return (
        (r, g, b, a)
        for r in range(256)
        for g in range(256)
        for b in range(256)
        for a in range(0, 101, 2)
    )


def get_colour(index: int) -> Tuple[int, int, int, int]:
    """
    Возвращает RGBA цвет по указанному индексу в последовательности.

    Args:
    index (int): Номер цвета в последовательности.

    Returns:
    Tuple[int, int, int, int]: Кортеж с значениями RGBA.

    Raises:
    IndexError: Если индекс выходит за пределы допустимого диапазона.
    StopIteration: Если генератор исчерпан (теоретически, но на практике обрабатывается через IndexError).
    """
    if index < 1 or index > 256**3 * 51:
        raise IndexError("Colour index out of range")
    rgba = rgba_gen()
    for _ in range(index - 1):
        next(rgba)
    return next(rgba)



def prime_dec(func: Callable[[], Generator[int, None, None]]) -> Callable[[int], int]:
        """
        Декоратор для генератора простых чисел, который модифицирует его поведение:
        возвращает k-е простое число и сохраняет последнее сгенерированное простое число как атрибут.

        Args:
        func (Callable[[], Generator[int, None, None]]): Функция-генератор, возвращающая простые числа.

        Returns:
        Callable[[int], int]: Функция-обертка, которая возвращает k-е простое число и сохраняет последнее значение.

        Raises:
        ValueError: Если k меньше последнего запрошенного значения.
        RuntimeError: Если генератор не вернул значение.
        """
        gen = func()
        last_k: int = 0
        last_prime: Optional[int] = None

        def wrapper(k: int) -> int:
            nonlocal last_k, last_prime

            if k < last_k:
                raise ValueError(
                    "k must be greater than or equal to the last requested value."
                )

            for _ in range(last_k, k):
                last_prime = next(gen)

            last_k = k
            if last_prime is None:
                raise RuntimeError("Prime generator did not yield a value.")

            return last_prime

        return wrapper


def prime_generator() -> Generator[int, None, None]:
    """
        Генератор простых чисел.

        Args:
        Нет аргументов.

        Returns:
        Generator[int, None, None]: Генератор, который возвращает простые числа, начиная с 2.

        Raises:
        Нет исключений.
        """
    num = 2
    flag = True
    while True:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                flag = False
                break
        if flag:
            yield num
        num += 1
        flag = True
