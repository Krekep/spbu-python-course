import pytest


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("basic teardown module")


def test_1():
    assert 1 + 1 == 2


def test_2():
    assert "1" + "1" == "11"


@pytest.mark.parametrize("a, b", [(1, 1), ("eq", "eq")])
def test_3(a, b):
    assert a == b
