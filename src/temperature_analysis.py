"""Solution for temperature analysis kata."""


def lowest_temp(t):
    lowest = None
    temps = t.split(" ")
    for temp in temps:
        if temp:
            if lowest is None or int(temp) < lowest:
                lowest = int(temp)
    return lowest
