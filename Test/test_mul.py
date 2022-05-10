import pytest

from Src.calc import mul


@pytest.mark.parametrize(
    "x, y, expected",
 [
    (3, 3, 9),
    (-3, 3, -9),
    (-3, -3, 9),
 ]
)


def test_mul(x, y, expected):
    assert mul(x,y) == expected