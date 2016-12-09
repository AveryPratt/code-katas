"""Returns a deformed concatination of two strings."""


def reverseAndMirror(s1,s2):
    return (s2[::-1] + "@@@" + s1[::-1] + s1).swapcase()