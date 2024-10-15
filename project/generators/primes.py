from typing import Generator


def prime_generator() -> Generator[int, None, None]:
    """
    A generator that yields a sequence of prime numbers.

    Yields:
        int: The next prime number in the sequence.
    """
    primes = [2]
    i = 2
    yield 2

    while True:
        i += 1
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
            yield i
        i += 1


def get_k_prime(k: int) -> int:
    """
    Retrieve the k-th prime number.

    Parameters:
        k (int): The index of the prime number to retrieve (1-based).

    Returns:
        int: The k-th prime number.

    Raises:
        AssertionError: If k is not greater than 0.
    """
    assert k > 0

    gen = prime_generator()
    prime = 0
    for _ in range(k):
        prime = next(gen)
    return prime
