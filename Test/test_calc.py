import pytest
from src.calc import add


def test_add():
    assert add(1, 2) == 3
    assert add(2, 1) == 3


def test_add_with_neg_num():
    assert add(-2, 1) == -1
    assert add(-20, 1) == -19


# if __name__ == "__main__":
#     # Run test when starting program
#     try:
#         test_add()
#         test_add_failing()
#     except AssertionError as err:
#         print("Test failed")
#         raise
#     print("All tests passed!")