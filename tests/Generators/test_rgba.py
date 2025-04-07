import pytest
from project.Generators.generators import rgba_gen, get_colour


@pytest.mark.parametrize(
    "index, expected_rgba",
    [
        (1, (0, 0, 0, 0)),
        (2, (0, 0, 0, 2)),
        (52, (0, 0, 1, 0)),
    ],
)
def test_rgba_gen_indexed(index, expected_rgba):
    rgba = rgba_gen()
    for _ in range(index - 1):
        next(rgba)
    assert next(rgba) == expected_rgba


@pytest.mark.parametrize(
    "index, expected_rgba",
    [
        (1, (0, 0, 0, 0)),
        (161024, (0, 12, 85, 32)),
        (-1, IndexError),
        (10e8, IndexError),
    ],
)
def test_get_colour(index, expected_rgba):
    if isinstance(expected_rgba, type) and issubclass(expected_rgba, Exception):
        with pytest.raises(expected_rgba):
            get_colour(index)
    else:
        assert get_colour(index) == expected_rgba