"""Tests string_manipulation to see if it manipulates strings properly."""


import pytest


def test1():
    """checks simple case"""
    from src.string_manipulation import reverse_and_mirror
    str_1, str_2 = "FizZ", "buZZ"
    assert reverse_and_mirror(str_1, str_2) == "zzUB@@@zZIffIZz"


def test2():
    """checks case with spaces"""
    from src.string_manipulation import reverse_and_mirror
    str_1, str_2 = "String Reversing", "Changing Case"
    assert reverse_and_mirror(str_1, str_2) == "ESAc GNIGNAHc@@@GNISREVEr GNIRTssTRING rEVERSING"