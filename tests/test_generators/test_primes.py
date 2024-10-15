import pytest
from project.generators.primes import get_k_prime, prime_generator


@pytest.fixture
def prime_gen():
    return prime_generator()


@pytest.mark.parametrize(
    "k, expected",
    [(1, 2), (2, 3), (3, 5), (4, 7), (5, 11), (6, 13), (10, 29), (100, 541)],
)
def test_get_k_prime_valid_k(k, expected):
    assert get_k_prime(k) == expected


def test_get_k_prime_invalid_k():
    with pytest.raises(AssertionError):
        get_k_prime(0)  # k is less than or equal to 0
    with pytest.raises(AssertionError):
        get_k_prime(-1)  # k is less than or equal to 0


def test_prime_generator_first_primes(prime_gen):
    """Test if the first few prime numbers are generated correctly."""
    assert next(prime_gen) == 2
    assert next(prime_gen) == 3
    assert next(prime_gen) == 5
    assert next(prime_gen) == 7
    assert next(prime_gen) == 11
    assert next(prime_gen) == 13
