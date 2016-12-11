"""Returns a deformed concatination of two strings."""


def reverse_and_mirror(s_1, s_2):
    """Puts some strings in a garbage disposal and returns result."""
    return (s_2[::-1] + "@@@" + s_1[::-1] + s_1).swapcase()
