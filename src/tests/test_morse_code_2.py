"""Tests for morse code kata part 2."""


import pytest


MORSE_TESTS = [
    ['1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011', '.... . -.--   .--- ..- -.. .'],
]


REAL_TESTS = [
    ['1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011', 'HEY JUDE'],
]


@pytest.mark.parametrize("bits, morse", MORSE_TESTS)
def test_bits_to_morse(bits, morse):
    from morse_code_2 import decodeBits
    assert decodeBits(bits) == morse


@pytest.mark.parametrize("bits, result", REAL_TESTS)
def test_bits_to_result(bits, result):
    from morse_code_2 import decodeBits
    from morse_code_1 import decodeMorse
    morse = decodeBits(bits)
    assert decodeMorse(morse) == result
