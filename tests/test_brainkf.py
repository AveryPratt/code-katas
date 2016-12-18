


BRAINFK_TESTS = [
    [',+[-.,+]', 'Codewars' + chr(255), 'Codewars'],
    [',[.[-],]', 'Codewars' + chr(0), 'Codewars'],
    [',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9), chr(72)]
]


import pytest


@pytest.mark.parametrize("code, input, result", BRAINFK_TESTS)
def test1(code, input, result):
    """Tests code commands against input to see if desired result is achieved."""
    from src.brainfk import brain_luck
    assert brain_luck(code, input) == result


# Echo until byte(255) encountered
# Echo until byte(0) encountered
# Two numbers multiplier
