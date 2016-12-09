"""Returns "Throw up" if waves are too choppy, or No Problem if they are calm.""" 


def sea_sick(sea):
    cur = sea[0]
    change = 0
    for char in sea:
        if char is not cur:
            cur = char
            change += 1
    if change / len(sea) > .2:
        return "Throw Up"
    return "No Problem"