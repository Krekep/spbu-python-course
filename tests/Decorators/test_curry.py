import pytest
from project.Decorators.curry import curry_explicit

def test_curry_basic():
    f2 = curry_explicit(lambda x, y, z: f"<{x},{y}, {z}>", 3)
    assert f2(1)(2)(3) == "<1,2, 3>"


def test_curry_arity_1():
    f = curry_explicit(lambda x: x * 2, 1)
    assert f(5) == 10


def test_curry_arity_0():
    f = curry_explicit(lambda: "Hello, World!", 0)
    assert f() == "Hello, World!"


def test_curry_type_error():
    f = curry_explicit(lambda x, y: x + y, 2)
    with pytest.raises(TypeError):
        f(1)(2)(3) 


def test_negative_arity():
    with pytest.raises(ValueError):
        curry_explicit(lambda x: x, -1)


def test_curry_proper_usage():
    f = curry_explicit(lambda x, y, z: f"{x} {y} {z}", 3)
    assert f(1)(2)(3) == "1 2 3"
    assert f(1)(2)(0) == "1 2 0"


def test_curry_preserve_arity():
    original_function = lambda a, b, c, d: a + b + c + d
    curried_function = curry_explicit(original_function, 4)

    with pytest.raises(TypeError):
        curried_function(1)(2)(3)(4)(5)

    assert curried_function(1)(2)(3)(4) == 10  
    assert curried_function(1)(1)(1)(1) == 4  
    assert curried_function(1)(2)(3)(-1) == 5  

    assert curried_function(1)(2)(3)(0) == 6  
    assert curried_function(1)(2)(-1)(0) == 2  

    partial_application = curried_function(1)(2)
    assert partial_application(3)(4) == 10  
    assert partial_application(-1)(-1) == 1  


def test_curry_with_builtin_functions():
    curried_max = curry_explicit(max, 3)
    assert curried_max(1)(2)(3) == 3
    assert curried_max(10)(20)(5) == 20

    curried_sum = curry_explicit(sum, 2)
    assert curried_sum([1, 2])(3) == 6
    assert curried_sum([10, 20])(30) == 60

    # написать тесты для вызова от нескольких параметров