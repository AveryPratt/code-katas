"""Defines a series of numbers rounded to 2 decimal points."""


def series_sum(num):
    """Returns the sum of the 0-based series x = 1/(1+n/3)"""
    denom = 1
    total = 0
    for ind in range(0, num):
        total += 1 / denom
        denom += 3
    return "{0:.2f}".format(total)
