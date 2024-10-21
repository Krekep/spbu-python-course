import pytest
from project.concurrent_futures import cartesian_product_sum


@pytest.mark.parametrize(
    "numbers, expected_sum",
    [([1, 2], 12), ([1, 0], 4), ([1, -1], 0), ([2, 4, 3], 54), ([0], 0), ([], 0)],
)
def test_cartesian_product_sum(numbers, expected_sum):
    assert cartesian_product_sum(numbers) == expected_sum
