import pytest
import project.ThreadPool.cartesian_product_sums as cps

@pytest.mark.parametrize(
    "threads_num, list_of_sets, expected_sum",
    [(3, [[1], [2]], 3), (3, [[1, 2], [3, 4]], 20), (3, [[1, 2], [3, 4], [5, 6]], 84), (3, [[1, 2, 3], [4, 5], [6]], 75)],
)
def test_parallel_cartesian_sum(threads_num, expected_sum, list_of_sets):
    assert expected_sum == cps.cartesian_product_sum(threads_num, list_of_sets)