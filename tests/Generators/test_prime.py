import pytest
from project.Generators.generators import prime_generator, prime_dec


@pytest.mark.parametrize(
    "count,expected_primes",
    [
        (5, [2, 3, 5, 7, 11]),
        (10, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
    ],
)
def test_prime_generator(count, expected_primes):
    gen = prime_generator()
    primes = [next(gen) for _ in range(count)]
    assert primes == expected_primes


@prime_dec
def decorated_prime_generator():
    return prime_generator()


@pytest.mark.parametrize(
    "k,expected",
    [
        (1, 2),
        (10, 29),
        (10, 29),
        (100, 541),
        (99, ValueError),
    ],
)
def test_prime_dec(k, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            decorated_prime_generator(k)
    else:
        assert decorated_prime_generator(k) == expected


@pytest.mark.parametrize(
    "invalid_k",
    [
        -1,
        0,
        1.5,
        "three",
        None,
    ],
)
def test_invalid_k(invalid_k):
    with pytest.raises((TypeError, ValueError)):
        decorated_prime_generator(invalid_k)