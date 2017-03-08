"""Tests for anagrams kata."""


import pytest


TESTS = [
    ['A', 1],
    ['ABAB', 2],
    ['AAAB', 1],
    ['BAAA', 4],
    ['QUESTION', 24572],
    ['BOOKKEEPER', 10743]
]


@pytest.mark.parametrize("word, number", TESTS)
def test_anagrams(word, number):
    from anagrams import listPosition
    assert listPosition(word) == number
