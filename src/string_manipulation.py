"""Returns a deformed concatination of two strings."""


def reverse_and_mirror(s_1, s_2):
    """Manipulates two strings in several different ways to get an obscure result."""
    return (s_2[::-1] + "@@@" + s_1[::-1] + s_1).swapcase()
