import pytest
from project.generators.primes import get_k_prime, prime_generator


@pytest.mark.parametrize(
    "k, expected",
    [(1, [2, 3]), (3, [5, 7]), (10, [29, 31])],
)
def test_get_k_prime_valid_k(k, expected):
    decorated_gen = get_k_prime(prime_generator)
    for exp in expected:
        assert decorated_gen(k) == exp
        k += 1


@pytest.mark.parametrize("k", [-1, 0])
def test_get_k_prime_invalid_k(k):
    decorated_gen = get_k_prime(prime_generator)
    with pytest.raises(AssertionError):
        decorated_gen(k)


def test_prime_generator_first_primes():
    """Test if the first few prime numbers are generated correctly."""
    gen = prime_generator()
    assert next(gen) == 2
    assert next(gen) == 3
    assert next(gen) == 5
    assert next(gen) == 7
    assert next(gen) == 11
    assert next(gen) == 13
