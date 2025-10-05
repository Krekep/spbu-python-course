import pytest
from funktools import reduce
from typing import Callable, Iterable
from your_module import dataGen, pipeline, to_list, to_dict, to_set, filter_triad, cube


@pytest.fixture
def small_dataset()
    return dataGen(5)

@pytest.fixture
def zero_dataset()
    return dataGen(0)

@pytest.fixture
def my_operatio()
    return{
        'filter_triad': filter_triad
        'cube': cube
    }

@putest.fixture
def classic_operatio()
    return{
        'd_map': lambda x: map(lambda y: y*2, x)
        'z_filter': lambda x: filter(lambda y: y%2 == 0, x)
        'add_zip': lambda x: zip(lambda y: y+10, x)
    }
