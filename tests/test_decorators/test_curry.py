import pytest
from project.decorators.curry import curry_explicit, uncurry_explicit


def test_curry_single_argument():
    f = curry_explicit(lambda x: x + 1, 1)
    assert f(5) == 6


def test_curry_multiple_arguments():
    f = curry_explicit(lambda x, y, z: x + y + z, 3)
    curried = f(1)(2)
    assert curried(3) == 6


def test_uncurry_single_argument():
    f = curry_explicit(lambda x: x * 2, 1)
    uncurried = uncurry_explicit(f, 1)
    assert uncurried(10) == 20


def test_uncurry_multiple_arguments():
    f = curry_explicit(lambda x, y, z: x * y * z, 3)
    uncurried = uncurry_explicit(f, 3)
    assert uncurried(2, 3, 4) == 24


def test_curry_multiple_at_once_arguments():
    f = curry_explicit(lambda x, y: x + y, 2)
    with pytest.raises(TypeError):
        assert f(5, 6) == 11


def test_curry_arity_mismatch():
    f = curry_explicit(lambda x, y: x + y, 2)
    with pytest.raises(TypeError):
        f(1, 2, 3)


def test_uncurry_arity_mismatch():
    f = curry_explicit(lambda x, y: x + y, 2)
    uncurried = uncurry_explicit(f, 2)
    with pytest.raises(TypeError):
        uncurried(1)


def test_curry_negative_arity():
    with pytest.raises(ValueError):
        curry_explicit(lambda x: x + 1, -1)


def test_uncurry_negative_arity():
    f = curry_explicit(lambda x: x + 1, 1)
    with pytest.raises(ValueError):
        uncurry_explicit(f, -1)


def test_curry_arity_zero():
    f = curry_explicit(lambda: "hello", 0)
    assert f() == "hello"


def test_uncurry_arity_zero():
    f = curry_explicit(lambda: "world", 0)
    uncurried = uncurry_explicit(f, 0)
    assert uncurried() == "world"
