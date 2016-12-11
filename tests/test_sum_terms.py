"""Test for finding a number in a series."""


import pytest


def test1():
    """check first number in series x = 1 / (1 + n * 3)"""
    from src.sum_terms import series_sum
    assert series_sum(1) == "1.00"


def test2():
    """check second number in series x = 1 / (1 + n * 3)"""
    from src.sum_terms import series_sum
    assert series_sum(2) == "1.25"


def test3():
    """check third number in series x = 1 / (1 + n * 3)"""
    from src.sum_terms import series_sum
    assert series_sum(3) == "1.39"
