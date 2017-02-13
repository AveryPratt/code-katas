"""Tests for pick_peaks kata."""


import pytest


TESTS = [
    [[1, 2, 3, 6, 4, 1, 2, 3, 2, 1], {"pos":[3, 7], "peaks":[6, 3]}],
    [[3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3], {"pos":[3, 7], "peaks":[6, 3]}],
    [[3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1], {"pos":[3, 7, 10], "peaks":[6, 3, 2]}],
    [[2, 1, 3, 1, 2, 2, 2, 2, 1], {"pos":[2, 4], "peaks":[3, 2]}],
    [[2, 1, 3, 1, 2, 2, 2, 2], {"pos":[2], "peaks":[3]}]
]


@pytest.mark.parametrize("horizon, solution", TESTS)
def test_pick_peaks(horizon, solution):
    from pick_peaks import pick_peaks
    assert pick_peaks(horizon) == solution
