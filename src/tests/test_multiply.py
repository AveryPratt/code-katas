"""Tests a multiplication function."""


import pytest


def test1():
    """checks that 3 * 4 is 12"""
    from multiply import multiply
    assert multiply(3, 4) == 12


def test2():
    """checks that we can also multiply by non-integers"""
    from multiply import multiply
    assert multiply(2, 5.5) == 11


def test3():
    """checks that we can also multiply by negatives"""
    from multiply import multiply
    assert multiply(-2, 5.5) == -11
