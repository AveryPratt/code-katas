"""Tests for forbes.py challenge."""


import pytest


TESTS = [
    ["forbes.json", "\nyoungest billionaire:\nname: Mark Zuckerberg:\nnet worth: 44600000000\nindustry: Facebook\n\noldest billionaire under 80:\nname: Phil Knight:\nnet worth: 24400000000\nindustry: Nike\n"],
    ["other.json", "\nyoungest billionaire:\nname: Avery Pratt:\nnet worth: 0.5\nindustry: Orbitroids\n\noldest billionaire under 80:\nname: Avery Pratt:\nnet worth: 0.5\nindustry: Orbitroids\n"]
]


@pytest.mark.parametrize("file_name, output", TESTS)
def test_forbes(file_name, output):
    """Test that inputing different files into
    find_billionaires function returns correct results."""
    from forbes import find_billionaires
    assert find_billionaires(file_name) == output


def test_forbes_no_input():
    from forbes import find_billionaires
    assert find_billionaires() == "\nyoungest billionaire:\nname: Mark Zuckerberg:\nnet worth: 44600000000\nindustry: Facebook\n\noldest billionaire under 80:\nname: Phil Knight:\nnet worth: 24400000000\nindustry: Nike\n"


def test_forbes_file_not_found():
    from forbes import find_billionaires
    with pytest.raises(FileNotFoundError):
        find_billionaires("dummy_file.json")


def test_forbes_bad_file():
    from forbes import find_billionaires
    with pytest.raises(OSError):
        find_billionaires(42)


def test_forbes_non_json_file():
    from forbes import find_billionaires
    from json import JSONDecodeError
    with pytest.raises(JSONDecodeError):
        find_billionaires("k_primes.py")
