from typing import Generator, Callable


def prime_generator() -> Generator[int, None, None]:
    """
    A generator that yields a sequence of prime numbers.

    Yields:
        int: The next prime number in the sequence.
    """
    prime = 2
    while True:
        is_prime = True
        for den in range(2, int(prime**0.5) + 1):
            if prime % den == 0:
                is_prime = False
                break
        if is_prime:
            yield prime
        prime += 1


def get_k_prime(generator: Callable[[], Generator[int, None, None]]) -> Callable:
    """
    Retrieve the k-th prime number.

    Parameters:
        gen: Generator[Any, None, None]
            Generator for our prime sequence

    Returns:
        Callable: the function which gives the k-th prime number.

    Raises:
        AssertionError: If k is not greater than 0.
    """
    gen = generator()
    index = 0

    def inner(k: int) -> int | None:
        assert k > 0
        nonlocal gen
        nonlocal index

        if k <= index:
            gen = generator()
            index = 0

        result = None
        while index != k:
            result = next(gen)
            index += 1
        return result

    return inner
