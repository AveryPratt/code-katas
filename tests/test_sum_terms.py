"""Test for finding a number in a series."""


import pytest

@pytest.mark.parametrize("inp, result", [[0, "0.00"], [1, "1.00"], [2, "1.25"], [3, "1.39"]])
def test1(inp, result):
    """check first number in series x = 1 / (1 + n * 3)"""
    from src.sum_terms import series_sum
    assert series_sum(inp) == result
