"""Tests noob_debug kata."""


import pytest


def test_noob_debug():
    from noob_debug import add
    assert add('a', 'b') == 195
