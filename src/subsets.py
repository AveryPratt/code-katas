"""Returns the total possible number of subsets in a unique set of a list."""


def est_subsets(arr):
    """Calculates subsets by finding the binary values of the set's length number of digits,
    and subtracts one because of the 0th result.'"""
    arr = set(arr)
    return 2 ** len(arr) - 1

