import pytest

from Src.calc import add, sub


def test_add():
    assert add(1, 2) == 3
    assert add(2, 1) == 3


def test_add_with_neg_num():
    assert add(-2, 1) == -1
    assert add(-20, 1) == -19


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 1, 0),
        (-5, -3, -2),
        (0, 0, 0),
        (10, 20, -10),
        (10, 5, 8),
    ]
)
def test_sub(x, y, expected):
    assert sub(x, y) == expected

# if __name__ == "__main__":
#     # Run test when starting program
#     try:
#         test_add()
#         test_add_failing()
#     except AssertionError as err:
#         print("Test failed")
#         raise
#     print("All tests passed!")
