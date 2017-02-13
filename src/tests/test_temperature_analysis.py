"""Tests for temperature analysis kata."""


import pytest


def test_temperatures_empty():
    """Tests that with no temperatures input, returns None."""
    from temperature_analysis import lowest_temp
    assert lowest_temp("") is None


def test_temperatures_positive():
    """Test that lowest temperature in string is returned."""
    from temperature_analysis import lowest_temp
    assert lowest_temp("50 20 22 0 10 ") == 0


def test_temperatures_negative():
    """Test that lowest temperature in string is returned."""
    from temperature_analysis import lowest_temp
    assert lowest_temp("-1 50 -4 20 22 -7 0 10 -8") == -8
