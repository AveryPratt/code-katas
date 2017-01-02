"""Tests that sort_cards function returns a sorted version of the input deck."""


import pytest


DECKS = [
    [list('A23456789TJQK'), list('A23456789TJQK')],
    [list('39A5T824Q7J6K'), list('A23456789TJQK')],
    [list('Q286JK395A47T'), list('A23456789TJQK')],
    [list('54TQKJ69327A8'), list('A23456789TJQK')],
    [[], []],
    [list('54TQK27A8'), list('A24578TQK')],
    [list('54T38T9QKJ693J27A8J'), list('A23345678899TTJJJQK')],
]


@pytest.mark.parametrize("unsorted, result", DECKS)
def test_sort1(unsorted, result):
    """Checks that decks are sorted by sort_cards function."""
    from sort_cards import sort_cards
    assert sort_cards(unsorted) == result
