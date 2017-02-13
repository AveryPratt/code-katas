"""Tests for Social Golfer Problem Validator kata."""


import pytest


TESTS = [
    [[], True],
    [[[]], True],
    [[[], []], True],
    [[[], [], []], True],
    [["AB"], True],
    [[["AB", "CD"], ["AD", "BC"], ["BD", "AC"]], True],
    [[['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'], ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'], ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'], ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'], ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']], True],
    [[["AB", "CD", "EF", "GH"], ["AC", "BD", "EG", "FH"], ["AD", "CE"], ["AE", "BG", "CH", "FD"]], False],
    [[["ABC", "DEF"], ["ADE", "CBF"]], False],
]


@pytest.mark.parametrize("solution, result", TESTS)
def test_golfers(solution, result):
    from golfers import valid
    assert valid(solution) == result
