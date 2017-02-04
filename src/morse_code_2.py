"""Solution for morse_code kata part 2."""


def decodeBits(bits):
    bits = bits.strip("0")
    downs = bits.split("0")
    downs = filter(lambda d: d != "", downs)
    for idx in enumerate(downs):
        downs[idx[0]] = len(idx[1])
    ups = bits.split("1")
    ups = filter(lambda d: d != "", ups)
    for idx in enumerate(ups):
        ups[idx[0]] = len(idx[1])
    if downs and ups:
        unit = min(min(ups), min(downs))
    elif downs:
        unit = min(downs)
    elif ups:
        unit = min(ups)
    downs = [down / unit for down in downs]
    ups = [up / unit for up in ups]
    for idx in enumerate(downs):
        if idx[1] == 1:
            downs[idx[0]] = '.'
        elif idx[1] == 3:
            downs[idx[0]] = '-'
    for idx in enumerate(ups):
        if idx[1] == 1:
            ups[idx[0]] = ''
        elif idx[1] == 3:
            ups[idx[0]] = ' '
        elif idx[1] == 7:
            ups[idx[0]] = '   '
    fin = []
    down = True
    while downs or ups:
        if down:
            fin.append(downs[0])
            downs = downs[1:]
            down = False
        else:
            fin.append(ups[0])
            ups = ups[1:]
            down = True
    return "".join(fin)
