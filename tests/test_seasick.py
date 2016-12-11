"""Tests if snorkelers and boat-goers will throw up."""


import pytest


def test1():
    """That little wave can't hurt me :)'"""
    from src.seasick import sea_sick
    assert sea_sick("~") == "No Problem"

def test2():
    """11 wave changes out of 28 spaces: 39%"""
    from src.seasick import sea_sick
    assert sea_sick("_~~~~~~~_~__~______~~__~~_~~") == "Throw Up"


def test3():
    """4 wave changes out of 12 spaces: 25%"""
    from src.seasick import sea_sick
    assert sea_sick("______~___~_") == "Throw Up"


def test4():
    """No wave changes"""
    from src.seasick import sea_sick
    assert sea_sick("____") == "No Problem"


def test5():
    """9 wave changes out of 21 spaces: 43%"""
    from src.seasick import sea_sick
    assert sea_sick("_~~_~____~~~~~~~__~_~") == "Throw Up"
