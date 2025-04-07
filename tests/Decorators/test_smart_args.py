import random
import pytest

from project.Decorators.smart_args import smart_args, Evaluated, Isolated

def get_random_number():
    random.seed(0)
    return random.randint(0, 100)

# Tests
def test_evaluated():

    @smart_args(enable_positional=False)
    def test_func(x=Evaluated(lambda: 0)):
        return x

    result = test_func(x=10)  
    assert result == 10

    result = test_func()  
    assert result == 0

def test_isolated_and_evaluated_in_combination():

    @smart_args()
    def test_func(d=Isolated(), y=Evaluated(lambda: 0)):
        return d, y

    d_value = {"test": 1}
    result_d, result_y = test_func(d=d_value)
    assert result_d is not d_value  
    assert result_d == d_value  
    assert result_y == 0  
    with pytest.raises(ValueError) as exc_info:
        test_func()  
    assert "Argument 'd' must be provided when using Isolated()" in str(exc_info.value)

def test_evaluated_with_positional_argument():

    @smart_args(enable_positional=True)
    def test_func(x=Evaluated(get_random_number)):
        return x

    result = test_func(10)  
    assert result == 10 

    result = test_func()  
    assert isinstance(result, int)  

def test_mixed_arguments_with_evaluated():

    @smart_args(enable_positional=True)
    def test_func(x=Evaluated(get_random_number), y=0):
        return x, y

    result = test_func(1)  
    assert result == (1, 0)

    result = test_func(y=2)  
    assert result[1] == 2

def test_evaluated_called_each_time():

    called_count = 0

    def counter():
        nonlocal called_count
        called_count += 1
        return called_count

    @smart_args()
    def test_func(x=Evaluated(counter)):
        return x

    assert test_func() == 1
    assert test_func() == 2
    assert test_func(x=10) == 10 
    assert called_count == 2

def test_isolated_returns_deep_copy():

    original_dict = {"a": 10}

    @smart_args()
    def test_func(d=Isolated()):
        return d

    result = test_func(d=original_dict)
    assert result is not original_dict
    assert result == original_dict

    result["b"] = 20
    assert "b" not in original_dict

def test_isolated_deep_copy_with_multiple_args():

    @smart_args()
    def test_func(a=Isolated(), b=Isolated()):
        return a, b

    a_val = {"x": 1}
    b_val = {"y": 2}
    result_a, result_b = test_func(a=a_val, b=b_val)

    assert result_a is not a_val
    assert result_b is not b_val
    assert result_a == a_val
    assert result_b == b_val

def test_isolated_without_value():

    @smart_args()
    def test_func(d=Isolated()):
        return d

    with pytest.raises(ValueError, match="Argument 'd' must be provided when using Isolated()"):
        test_func()

def test_positional_arguments_disabled():

    @smart_args(enable_positional=False)
    def test_func(x=0):
        return x

    with pytest.raises(TypeError, match="Positional arguments are disabled for this function"):
        test_func(1)

def test_duplicate_arguments():

    @smart_args(enable_positional=True)
    def test_func(x=0):
        return x

    with pytest.raises(TypeError, match="Got multiple values for argument 'x'"):
        test_func(1, x=2)