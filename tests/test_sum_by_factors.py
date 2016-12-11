"""Tests for finding the sum of listed numbers for which each prime factor is a prime factor for"""


import pytest


def test1():
    """tests for a list of 1 number"""
    from src.sum_by_factors import sum_for_list
    assert sum_for_list([12]) == [[2, 12], [3, 12]]


def test2():
    """tests for a list of 2 numbers"""
    from src.sum_by_factors import sum_for_list
    assert sum_for_list([12, 15]) == [[2, 12], [3, 27], [5, 15]]


def test3():
    """tests for a list of 2 numbers, one being negative"""
    from src.sum_by_factors import sum_for_list
    assert sum_for_list([-15, 15]) == [[3, 0], [5, 0]]


def test4():
    """tests for a list containing a very large number"""
    from src.sum_by_factors import sum_for_list
    assert sum_for_list([2000000018]) == [[2, 2000000018], [1000000009, 2000000018]]
