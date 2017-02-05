"""Tests for morse code kata part 2."""


import pytest


MORSE_TESTS = [
    ['0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000', '.... . -.--   .--- ..- -.. .'],
]


REAL_TESTS = [
    ['0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000', 'HEY JUDE'],
]


@pytest.mark.parametrize("bits, morse", MORSE_TESTS)
def test_bits_to_morse(bits, morse):
    from morse_code_3 import decodeBitsAdvanced
    assert decodeBitsAdvanced(bits) == morse


@pytest.mark.parametrize("bits, result", REAL_TESTS)
def test_bits_to_result(bits, result):
    from morse_code_3 import decodeBitsAdvanced
    from morse_code_1 import decodeMorse
    morse = decodeBitsAdvanced(bits)
    assert decodeMorse(morse) == result
