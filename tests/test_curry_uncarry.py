import pytest
from project.curry_uncarry import curry_explicit, uncurry_explicit


def test_curry_function():
    """Test the curried function."""
    curried_add = curry_explicit(lambda x, y: x + y, 2)
    assert curried_add(3)(4) == 7  # Test the curried function


def test_uncurry_function():
    """Test the uncurried function."""
    curried_add = curry_explicit(lambda x, y: x + y, 2)
    uncurried_add = uncurry_explicit(curried_add, 2)
    assert uncurried_add(5, 7) == 12  # Test the uncurried function
