"""Tests for base_conversion kata."""


import pytest
from base_conversion import ALPHABETS


TESTS = [
    ["15", ALPHABETS["dec"], ALPHABETS["bin"], "1111"],
    ["15", ALPHABETS["dec"], ALPHABETS["oct"], "17"],
    ["1010", ALPHABETS["bin"], ALPHABETS["dec"], "10"],
    ["1010", ALPHABETS["bin"], ALPHABETS["hex"], "a"],
    ["0", ALPHABETS["dec"], ALPHABETS["alpha"], "a"],
    ["27", ALPHABETS["dec"], ALPHABETS["allow"], "bb"],
    ["hello", ALPHABETS["allow"], ALPHABETS["hex"], "320048"],
    ["SAME", ALPHABETS["allup"], ALPHABETS["allup"], "SAME"],
]


@pytest.mark.parametrize("src, start_lib, end_lib, result", TESTS)
def test_base_conversion(src, start_lib, end_lib, result):
    from base_conversion import convert
    assert convert(src, start_lib, end_lib) == result
