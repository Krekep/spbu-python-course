from typing import Generator, Tuple


def rgba_generator() -> Generator[Tuple[int, int, int, int], None, None]:
    """
    Generate an infinite sequence of RGBA color vectors.

    Each color vector is represented as a tuple (R, G, B, A), where:
    - R (Red) is an integer from 0 to 255,
    - G (Green) is an integer from 0 to 255,
    - B (Blue) is an integer from 0 to 255,
    - A (Alpha) is an integer from 0 to 100, taking only even values.

    Yields:
        tuple: A tuple representing an RGBA color vector.
    """
    for r in range(256):
        for g in range(256):
            for b in range(256):
                for a in range(0, 101, 2):
                    yield (r, g, b, a)


def get_rgba_color(i: int) -> Tuple[int, int, int, int]:
    """
    Retrieve the i-th RGBA color from the generator.

    Args:
        i (int): The index of the desired RGBA color vector. Must be a non-negative integer.

    Returns:
        tuple: A tuple representing the RGBA color vector at index i.

    Raises:
        StopIteration: If i is greater than the number of generated colors.

    Example:
        >>> color = get_rgba_color(10)
        >>> print(color)
        (0, 0, 10, 0)  # Example output; actual output may vary
    """
    gen = rgba_generator()
    for _ in range(i):
        color = next(gen)
    return color
