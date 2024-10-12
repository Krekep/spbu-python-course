import pytest
from project.rgba_generator import rgba_generator, get_rgba_element


def test_rgba_generator():
    gen = rgba_generator()
    assert next(gen) == (0, 0, 0, 0)
    assert next(gen) == (0, 0, 0, 2)
    assert next(gen) == (0, 0, 0, 4)
    assert next(gen) == (0, 0, 0, 6)
    for _ in range(51 - 4):
        next(gen)
    assert next(gen) == (0, 0, 1, 0)


@pytest.mark.parametrize(
    "i, expected",
    [
        (1, (0, 0, 0, 0)),
        (10, (0, 0, 0, 18)),
        (51 + 1, (0, 0, 1, 0)),
        (51 * 256 + 1, (0, 1, 0, 0)),
        (51 * 256 * 256 + 1, (1, 0, 0, 0)),
    ],
)
def test_get_rgba_element(i, expected):
    assert get_rgba_element(i) == expected


@pytest.mark.parametrize(
    "i, expected_error",
    [
        (
            -1,
            "Error: i must be greater than 0. The numbering of elements in a set of vectors starts from 1.",
        ),
        (
            0,
            "Error: i must be greater than 0. The numbering of elements in a set of vectors starts from 1.",
        ),
        (
            256**3 * 51 + 1,
            "Error: i must be within the number of possible vectors.",
        ),
        ("a", "Error: i must be an integer."),
    ],
)
def test_get_rgba_element_errors(i, expected_error):
    assert get_rgba_element(i) == expected_error
