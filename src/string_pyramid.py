"""Solution for string pyramid kata."""


def watch_pyramid_from_the_side(characters):
    """return the view of pyramid blocks looking horizontally from one side."""
    if characters == "":
        return ""
    elif characters:
        rows = []
        for enum in enumerate(characters[::-1]):
            idx = enum[0] + 1
            row = " " * len(characters[idx:]) + enum[1] * (2 * idx - 1) + " " * len(characters[idx:])
            rows.append(row)
        return "\n".join(rows)
    return None


def watch_pyramid_from_above(characters):
    """return the view of pyramid blocks looking down from above."""
    if characters == "":
        return ""
    elif characters:
        rows = []
        for enum in enumerate(characters):
            rows.append(characters[:enum[0]] + enum[1] * len(characters[enum[0]:]))
        for enum in enumerate(rows):
            rows[enum[0]] += enum[1][-2::-1]
        rows.extend(rows[-2::-1])
        return "\n".join(rows)
    return None


def count_visible_characters_of_the_pyramid(characters):
    """return the number of blocks that are visible from the top view."""
    if characters:
        return (2 * len(characters) - 1) ** 2
    return -1


def count_all_characters_of_the_pyramid(characters):
    """return the number of blocks in the (solid) pyramid."""
    if characters:
        count = 0
        for enum in enumerate(characters):
            count += (2 * enum[0] + 1) ** 2
        return count
    return -1
