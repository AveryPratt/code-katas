"""Deprecates the need for 3rd grade math class"""


import pytest


def test1():
    """checks that 3 * 4 is 12"""
    from src.multiply import multiply
    assert multiply(3, 4) == 12


def test2():
    """checks that we can also multiply by non-integers"""
    from src.multiply import multiply
    assert multiply(2, 5.5) == 11
