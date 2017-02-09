"""Tests for molecules to atoms kata."""


import pytest


TESTS = [
    ["H2O", {'H': 2, 'O' : 1}],
    ["Mg(OH)2", {'Mg': 1, 'O' : 2, 'H': 2}],
    ["K4[ON(SO3)2]2", {'K': 4, 'O': 14, 'N': 2, 'S': 4}]
]


@pytest.mark.parametrize("formula, dct", TESTS)
def test_parse_molecule(formula, dct):
    """Tests that parse molecule function returns the correct number of atoms for each formula."""
    from molecules import parse_molecule
    assert parse_molecule(formula) == dct
