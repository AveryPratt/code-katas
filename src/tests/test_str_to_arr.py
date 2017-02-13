"""Tests str_to_arr to see if strings turn into arrays."""


import pytest


def test1():
    """tests 2 word string"""
    from str_to_arr import string_to_array
    assert string_to_array("Robin Singh") == ["Robin", "Singh"]


def test2():
    """tests 1 word string"""
    from str_to_arr import string_to_array
    assert string_to_array("CodeWars") == ["CodeWars"]


def test3():
    """tests many-word string"""
    from str_to_arr import string_to_array
    assert string_to_array("I love arrays they are my favorite") == [
        "I",
        "love",
        "arrays",
        "they",
        "are",
        "my",
        "favorite",
        ]


def test4():
    """tests numbers in a string"""
    from str_to_arr import string_to_array
    assert string_to_array("1 2 3") == ["1", "2", "3"]


def test5():
    """tests an empty string"""
    from str_to_arr import string_to_array
    assert string_to_array("") == [""]
