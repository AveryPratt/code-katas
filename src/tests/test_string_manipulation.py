"""Tests string_manipulation to see if it manipulates strings properly."""


import pytest


def test1():
    """checks simple case"""
    from string_manipulation import reverse_and_mirror
    str_1, str_2 = "FizZ", "buZZ"
    assert reverse_and_mirror(str_1, str_2) == "zzUB@@@zZIffIZz"


def test2():
    """checks case with spaces"""
    from string_manipulation import reverse_and_mirror
    str_1, str_2 = "String Reversing", "Changing Case"
    assert reverse_and_mirror(str_1, str_2) == "ESAc GNIGNAHc@@@GNISREVEr GNIRTssTRING rEVERSING"


def test3():
    """checks case with empty string"""
    from string_manipulation import reverse_and_mirror
    str_1, str_2 = "", ""
    assert reverse_and_mirror(str_1, str_2) == "@@@"


def test4():
    """checks simple case"""
    from string_manipulation import reverse_and_mirror
    str_1, str_2 = "", "buZZ"
    assert reverse_and_mirror(str_1, str_2) == "zzUB@@@"


def test5():
    """checks simple case"""
    from string_manipulation import reverse_and_mirror
    str_1, str_2 = "FizZ", ""
    assert reverse_and_mirror(str_1, str_2) == "@@@zZIffIZz"
