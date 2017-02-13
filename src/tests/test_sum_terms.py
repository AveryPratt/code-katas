"""Test for finding a number indexed in a series for the function x = 1 / (1 + n * 3)."""


import pytest


@pytest.mark.parametrize("inp, result", [[-1, "0.00"], [0, "0.00"], [1, "1.00"], [2, "1.25"], [3, "1.39"]])
def test1(inp, result):
    """checks numbers by index in the series defined by x = 1 / (1 + n * 3)"""
    from sum_terms import series_sum
    assert series_sum(inp) == result
