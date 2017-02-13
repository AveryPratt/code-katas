"""Tests the get_parenthetics_status function in proper_parenthetics."""


import pytest


TEST_TABLE = [
    ["", 0],
    ["()", 0],
    [")()", -1],
    ["(()", 1],
    ["words(more words)", 0],
    ["lalalala(la))))", -1],
    [")))hi(((", -1],
    ["()()((((()", 1],
    ["^(0.0)^", 0],
]


@pytest.mark.parametrize("input_string, result", TEST_TABLE)
def test1(input_string, result):
    """Tests that get_parenthetics_status returns the correct number
    depending on the offset of pairs of parenthesis in the input string."""
    from proper_parenthetics import get_parenthetics_status
    assert get_parenthetics_status(input_string) == result
