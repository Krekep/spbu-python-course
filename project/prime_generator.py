import itertools


def prime_generator():
    yield 2

    n = 3
    while True:
        is_prime = True
        sqrt_n = int(n**0.5) + 1

        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                is_prime = False
                break

        if is_prime:
            yield n

        n += 2


def get_k(func):
    def wrapper(k):
        if not isinstance(k, int):
            return "Error: k must be an integer."
        if k <= 0:
            return "Error: k must be greater than 0."

        generator = func()
        k_prime = next(itertools.islice(generator, k - 1, k), None)

        return k_prime

    return wrapper


@get_k
def prime_generator_decorated():
    return prime_generator()
