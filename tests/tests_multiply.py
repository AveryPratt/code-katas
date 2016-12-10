"""Deprecates the need for 3rd grade math class"""


def test1():
    """checks that 3 * 4 is 12"""
    from multiply import multiply
    assert multiply.multiply(3, 4) == 12


def test2():
    """checks that we can also multiply by non-integers"""
    from multiply import multiply
    assert multiply.multiply(2, 5.5) == 11
