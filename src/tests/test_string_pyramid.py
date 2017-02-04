"""Tests for string pyramid kata."""


import pytest


TESTS = [
    [None, None, None, -1, -1],
    ["", "", "", -1, -1],
    ["a", "a", "a", 1, 1],
    ["ab", " b \naaa", "aaa\naba\naaa", 9, 10],
    ["abc", "  c  \n bbb \naaaaa", "aaaaa\nabbba\nabcba\nabbba\naaaaa", 25, 35]
]


@pytest.mark.parametrize("characters, side, top, vis, count", TESTS)
def test_pyramid_count(characters, side, top, vis, count):
    from string_pyramid import count_all_characters_of_the_pyramid
    assert count_all_characters_of_the_pyramid(characters) == count


@pytest.mark.parametrize("characters, side, top, vis, count", TESTS)
def test_pyramid_vis(characters, side, top, vis, count):
    from string_pyramid import count_visible_characters_of_the_pyramid
    assert count_visible_characters_of_the_pyramid(characters) == vis


@pytest.mark.parametrize("characters, side, top, vis, count", TESTS)
def test_pyramid_side(characters, side, top, vis, count):
    from string_pyramid import watch_pyramid_from_the_side
    assert watch_pyramid_from_the_side(characters) == side


@pytest.mark.parametrize("characters, side, top, vis, count", TESTS)
def test_pyramid_top(characters, side, top, vis, count):
    from string_pyramid import watch_pyramid_from_above
    assert watch_pyramid_from_above(characters) == top
