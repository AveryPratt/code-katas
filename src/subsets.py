"""Solution to https://www.codewars.com/kata/584703d76f6cf6ffc6000275"""


def est_subsets(arr):
    """returns the total possible number of subsets in a unique set of a list."""
    arr = set(arr)
    return 2 ** len(arr) - 1

