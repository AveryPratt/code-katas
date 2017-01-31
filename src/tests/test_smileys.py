"""Tests for smileys kata."""


import pytest


SMILEYS = [
    [[], 0],
    [[':D',':~)',';~D',':)'], 4],
    [[':)',':(',':D',':O',':;'], 2],
    [[';]', ':[', ';*', ':$', ';-D'], 1],
]


@pytest.mark.parametrize("smileys, result", SMILEYS)
def test_smileys(smileys, result):
    """Test that the number of smiley faces in the smileys array is equal to the result."""
    from smileys import count_smileys
    assert count_smileys(smileys) == result
