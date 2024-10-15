import pytest
from project.generators.rgba import get_rgba_color, rgba_generator


@pytest.mark.parametrize(
    "index, expected",
    [
        (1, (0, 0, 0, 0)),
        (2, (0, 0, 0, 2)),
        (52, (0, 0, 1, 0)),
        (256 * 51, (0, 0, 255, 100)),
        (256 * 51 + 1, (0, 1, 0, 0)),
    ],
)
def test_get_rgba_color(index, expected):
    assert get_rgba_color(index) == expected


def test_rgba_generator_first_colors():
    gen = rgba_generator()
    assert next(gen) == (0, 0, 0, 0)
    assert next(gen) == (0, 0, 0, 2)
    assert next(gen) == (0, 0, 0, 4)
    assert next(gen) == (0, 0, 0, 6)
    assert next(gen) == (0, 0, 0, 8)
