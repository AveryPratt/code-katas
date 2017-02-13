"""Tests for miner kata."""


import pytest


MAPS = [
    [[True]], # 1x1
    [[True, False], [True, True]], # 2x2
    [[True], [True], [True], [True]], # 1x4
    [[True, True, True], [False, False, True], [True, True, True]], # 3x3
]


TESTS = [
    [MAPS[0], {'x':0,'y':0}, {'x':0,'y':0}, []],
    [MAPS[1], {'x':0,'y':0}, {'x':1,'y':0}, ['right']],
    [MAPS[1], {'x':0,'y':0}, {'x':1,'y':1}, ['right', 'down']],
    [MAPS[2], {'x':0,'y':0}, {'x':3,'y':0}, ['right', 'right', 'right']],
    [MAPS[2], {'x':3,'y':0}, {'x':0,'y':0}, ['left', 'left', 'left']],
    [MAPS[3], {'x':0,'y':0}, {'x':2,'y':0}, ['down', 'down', 'right', 'right', 'up', 'up']],
]


@pytest.mark.parametrize("map, miner, exit, solution", TESTS)
def test_miner(map, miner, exit, solution):
    from miner import solve
    assert solve(map, miner, exit) == solution
