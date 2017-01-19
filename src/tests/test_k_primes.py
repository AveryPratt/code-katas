"""Tests for k-primes function"""


import pytest


PRIMES = [
    [2, 3],
    [3, 5],
    [5, 7],
    [7, 11],
    [11, 13]
]


TESTS = [
    [2, 0, 100, [4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95]],
    [3, 0, 100, [8, 12, 18, 20, 27, 28, 30, 42, 44, 45, 50, 52, 63, 66, 68, 70, 75, 76, 78, 92, 98, 99]],
    [5, 1000, 1100, [1020, 1026, 1032, 1044, 1050, 1053, 1064, 1072, 1092, 1100]],
    [5, 500, 600, [500, 520, 552, 567, 588, 592, 594]]
]


@pytest.mark.parametrize("prime, nxt", PRIMES)
def test_nxt_prime(prime, nxt):
    """Checks that nxt prime of a number returns the nxt lowest value prime."""
    from k_primes import nxt_prime
    assert nxt_prime(prime) == nxt



@pytest.mark.parametrize("k, start, end, result", TESTS)
def test_k_primes(k, start, end, result):
    """Checks lists of all k-primes in a range of start to end."""
    from k_primes import count_Kprimes
    assert count_Kprimes(k, start, end) == result
