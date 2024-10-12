import itertools


def prime_generator():
    primes = [2]
    yield 2

    n = 3
    while True:
        is_prime = True
        sqrt_n = int(n**0.5) + 1
        for prime in primes:
            if prime > sqrt_n:
                break
            if n % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(n)
            yield n

        n += 2


def get_k(k):
    if not isinstance(k, int):
        return "Error: k must be an integer."
    if k <= 0:
        return "Error: k must be greater than 0."

    def decorator(func):
        def wrapper(*args, **kwargs):
            generator = func(*args, **kwargs)
            k_element = next(itertools.islice(generator, k - 1, k), None)
            return k_element if k_element else "Error: index out of range."

        return wrapper

    return decorator
