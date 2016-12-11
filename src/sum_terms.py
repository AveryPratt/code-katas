"""Defines a series of numbers rounded to 2 decimal points."""


def series_sum(num):
    """Returns the sum of the 0-based series x = 1 / (1 + n * 3)"""
    total = 0
    for denom in range(1, 1 + num * 3, 3):
        total += 1 / denom
    return "{0:.2f}".format(total)
