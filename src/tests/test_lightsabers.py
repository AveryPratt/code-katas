"""Tests to see if Zach has 18 lightsabers and everyone else has 0."""


import pytest


def test1():
    """checks that if no one is selected, 0 lightsabers will be returned"""
    from lightsabers import how_many_lightsabers_do_you_own
    assert how_many_lightsabers_do_you_own() == 0


def test2():
    """checks to see if Bob has 0 lightsabers"""
    from lightsabers import how_many_lightsabers_do_you_own
    assert how_many_lightsabers_do_you_own("Bob") == 0


def test3():
    """checks if the number 12 has 0 lightsabers"""
    from lightsabers import how_many_lightsabers_do_you_own
    assert how_many_lightsabers_do_you_own(12) == 0


def test4():
    """checks if Zach has 18 lightsabers"""
    from lightsabers import how_many_lightsabers_do_you_own
    assert how_many_lightsabers_do_you_own("Zach") == 18
