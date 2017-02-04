"""Tests for piano keys kata."""


import pytest


TESTS = [
    [1, "white"],
    [5, "black"],
    [12, "black"],
    [42, "white"],
    [88, "white"],
    [89, "white"],
    [92, "white"],
    [100, "black"],
    [111, "white"],
    [200, "black"],
    [2017, "white"],
    [5571, "black"],
    [866, "white"],
    [3107, "black"]
]


@pytest.mark.parametrize("key_number, color", TESTS)
def test_piano_key_color(key_number, color):
    from piano_keys import black_or_white_key
    assert black_or_white_key(key_number) == color
