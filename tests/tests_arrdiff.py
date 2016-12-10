"""Tests for arrdiff, which should be called listdiff"""


def test1():
    """a was [1,2], b was [1], expected [2]"""
    from arrdiff import array_diff
    assert array_diff([1, 2], [1]) == [2]


def test2():
    """a was [1,2,2], b was [1], expected [2,2]"""
    from arrdiff import array_diff
    assert array_diff([1, 2, 2], [2]) == [1]


def test3():
    """a was [1,2,2], b was [], expected [1,2,2]"""
    from arrdiff import array_diff
    assert array_diff([1, 2, 2], []) == [1, 2, 2]


def test4():
    """a was [], b was [1,2], expected []"""
    from arrdiff import array_diff
    assert array_diff([], [1, 2]) == []
