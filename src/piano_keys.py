"""Solution for piano keys kata.
(differs from kata in that player plays up and down, rather than repeatedly playing up)
"""


def black_or_white_key(key_press_count):
    key_press_count -= 1
    black_keys = [1, 4, 6, 9, 11]
    if (key_press_count // 88) % 2 == 1:
        black_keys[0] = 2
    if (key_press_count % 88) % 12 in black_keys:
        return "black"
    return "white"
