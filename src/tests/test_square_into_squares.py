"""Tests for Square into Squares kata."""


import pytest


TESTS = [
    [0, None],
    [1, None],
    [2, None],
    [3, None],
    [4, None],
    [5, [3, 4]],
    [6, None],
    [7, [2, 3, 6]],
    [8, None],
    [9, [1, 4, 8]],
    [10, [6, 8]],
    [11, [1, 2, 4, 10]],
    [50, [1, 3, 5, 8, 49]]
]


@pytest.mark.parametrize("num, result", TESTS)
def test_square_into_squares(num, result):
    from square_into_squares import decompose
    assert decompose(num) == result
