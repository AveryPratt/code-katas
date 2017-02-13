"""Calculates the frequency of waves in the sea."""


def sea_sick(sea):
    """Returns "Throw up" if waves are too choppy, or "No Problem" if they are calm."""
    cur = sea[0]
    change = 0
    for char in sea:
        if char is not cur:
            cur = char
            change += 1
    if change / float(len(sea)) > .2:
        return "Throw Up"
    return "No Problem"
