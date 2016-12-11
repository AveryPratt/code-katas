"""Tests est_subsets for the correct number of subsets in a unique set."""


import pytest


def test1():
    """tests for small subset"""
    from src.subsets import est_subsets
    assert est_subsets([1, 2, 3, 4]) == 15


def test2():
    """tests for small subset with repeat members"""
    from src.subsets import est_subsets
    assert est_subsets(['a', 'b', 'c', 'd', 'd']) == 15


def test3():
    """tests for larger subset with repeat members"""
    from src.subsets import est_subsets
    arr = [2, 3, 4, 5, 5, 6, 6, 7, 8, 8]
    assert est_subsets(arr) == 127


def test4():
    """tests for even larger subset"""
    from src.subsets import est_subsets
    arr = ['a', 'z', 'z', 'z', 'b', 'j', 'f', 'k', 'b', 'd', 'j', 'j', 'n', 'm', 'm']
    assert est_subsets(arr) == 511


def test5():
    """tests for subset of all repeat members"""
    from src.subsets import est_subsets
    arr = [1] * 8
    assert est_subsets(arr) == 1


def test6():
    """tests for empty list"""
    from src.subsets import est_subsets
    arr = []
    assert est_subsets(arr) == 0
