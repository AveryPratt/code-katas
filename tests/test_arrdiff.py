"""Tests for arrdiff, which finds values in one array (list) but not the other"""

import sys
print(sys.path)
import pytest


def test1():
    """a was [1,2], b was [1], expected [2]"""
    from src.arrdiff import array_diff
    assert array_diff([1, 2], [1]) == [2]


def test2():
    """a was [1,2,2], b was [1], expected [2,2]"""
    from src.arrdiff import array_diff
    assert array_diff([1, 2, 2], [2]) == [1]


def test3():
    """a was [1,2,2], b was [], expected [1,2,2]"""
    from src.arrdiff import array_diff
    assert array_diff([1, 2, 2], []) == [1, 2, 2]


def test4():
    """a was [], b was [1,2], expected []"""
    from src.arrdiff import array_diff
    assert array_diff([], [1, 2]) == []


def test5():
    """a was [], b was [], expected []"""
    from src.arrdiff import array_diff
    assert array_diff([], []) == []


def test6():
    """a was [], b was [], expected []"""
    from src.arrdiff import array_diff
    assert array_diff([1, 2, 3], [1, 2, 3]) == []
