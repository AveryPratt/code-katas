"""Tests if wavey water (string input) will cause seasickness
(return 'Throw Up', or 'No Problem')."""


import pytest


def test1():
    """Tests single wave. 0%"""
    from seasick import sea_sick
    assert sea_sick("~") == "No Problem"

def test2():
    """11 wave changes out of 28 spaces: 39%"""
    from seasick import sea_sick
    assert sea_sick("_~~~~~~~_~__~______~~__~~_~~") == "Throw Up"


def test3():
    """4 wave changes out of 12 spaces: 25%"""
    from seasick import sea_sick
    assert sea_sick("______~___~_") == "Throw Up"


def test4():
    """No wave changes. 0 %"""
    from seasick import sea_sick
    assert sea_sick("____") == "No Problem"


def test5():
    """9 wave changes out of 21 spaces: 43%"""
    from seasick import sea_sick
    assert sea_sick("_~~_~____~~~~~~~__~_~") == "Throw Up"


def test6():
    """same as test5 but with different 'waves'"""
    from seasick import sea_sick
    assert sea_sick("baababbbbaaaaaaabbaba") == "Throw Up"
