"""Tests for morse code kata part 1."""


import pytest


TESTS = [
    ['.... . -.--   .--- ..- -.. .', 'HEY JUDE'],
    [' .... . -.--   .--- ..- -.. . ', 'HEY JUDE'],
    ['   .... . -.--   .--- ..- -.. .   ', 'HEY JUDE'],
    ['.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. .---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'],
]


@pytest.mark.parametrize("code, result", TESTS)
def test_morse_code(code, result):
    from morse_code_1 import decodeMorse
    assert decodeMorse(code) == result
