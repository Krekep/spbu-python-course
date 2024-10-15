import pytest
import random
from project.decorators.smart_arguments import smart_args, Isolated, Evaluated


@smart_args
def check_isolation(*, d=Isolated()):
    d["a"] = 0
    return d


@smart_args
def check_evaluation(*, x=5, y=Evaluated(lambda: random.randint(0, 100))):
    return x, y


# Tests
def test_check_isolation():
    no_mutable = {"a": 10}
    result = check_isolation(d=no_mutable)
    assert result == {"a": 0}
    assert no_mutable == {"a": 10}


def test_check_evaluation_fixed():
    result = check_evaluation(x=10, y=20)
    assert result == (10, 20)


def test_check_evaluation_evaluated():
    result = check_evaluation(x=10)
    assert result[0] == 10
    assert isinstance(result[1], int)
    assert 0 <= result[1] <= 100


def test_check_evaluation_multiple_calls():
    results = set()
    for _ in range(10):
        results.add(check_evaluation(x=10)[1])
    assert len(results) > 1


def test_isolated_assertion_error():
    with pytest.raises(AssertionError):
        check_isolation({}, Isolated())


def test_mixture_assertion_error():
    with pytest.raises(AssertionError):

        @smart_args
        def mixed_function(*, a=Evaluated(lambda: 1), b=Isolated()):
            return a, b

        mixed_function(b=[[1], [2]])


def test_isolated_argument_must_be_provided():
    @smart_args
    def example_function(*, d=Isolated()):
        return d

    with pytest.raises(ValueError, match="Argument 'd' must be provided."):
        example_function()
