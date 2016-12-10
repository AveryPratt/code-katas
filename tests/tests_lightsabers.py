"""Reveals the undercover jedi in the room"""


import pytest


def test1():
    """checks that if no one is selected, 0 lightsabers will be returned"""
    from lightsabers import how_many_lightsabers_do_you_own
    assert how_many_lightsabers_do_you_own() == 0


def test2():
    """disarms Bob"""
    from lightsabers import how_many_lightsabers_do_you_own
    assert how_many_lightsabers_do_you_own("Bob") == 0


def test3():
    """Starts thinking metaphysically about who could be a jedi"""
    from lightsabers import how_many_lightsabers_do_you_own
    assert how_many_lightsabers_do_you_own(12) == 0


def test4():
    """Zach's the one! KILL HIM!"""
    from lightsabers import how_many_lightsabers_do_you_own
    assert how_many_lightsabers_do_you_own("Zach") == 18
