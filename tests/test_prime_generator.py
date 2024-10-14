import pytest
from project.prime_generator import prime_generator, prime_generator_decorated


@pytest.mark.parametrize("expected_primes", [[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]])
def test_prime_generator(expected_primes):
    gen = prime_generator()
    generated_primes = [next(gen) for _ in range(10)]

    assert generated_primes == expected_primes


@pytest.mark.parametrize(
    "k, expected",
    [
        (1, 2),
        (2, 3),
        (5, 11),
        (10, 29),
    ],
)
def test_k_prime(k, expected):
    assert prime_generator_decorated(k) == expected


@pytest.mark.parametrize(
    "k, expected_error",
    [
        (0, "Error: k must be greater than 0."),
        (-1, "Error: k must be greater than 0."),
        ("a", "Error: k must be an integer."),
    ],
)
def test_invalid_k(k, expected_error):
    assert prime_generator_decorated(k) == expected_error
