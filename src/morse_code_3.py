"""Solution for morse_code kata part 3."""


def decodeBitsAdvanced(bits):
    bits = bits.strip("0")
    downs = bits.split("0")
    downs = filter(lambda d: d != "", downs)
    for idx in enumerate(downs):
        downs[idx[0]] = len(idx[1])
    ups = bits.split("1")
    ups = filter(lambda d: d != "", ups)
    for idx in enumerate(ups):
        ups[idx[0]] = len(idx[1])
    print("Downs: " + str(downs))
    print("Ups: " + str(ups))
    if downs:
        if min(downs) < float(max(downs)) / 2:
            unit = float(min(downs) + max(downs)) / 4
        else:
            d_unit = float(min(downs) + max(downs)) / 2
            if ups:
                u_unit = min(ups)
                if d_unit >= 3 * u_unit:
                    unit = d_unit / 3
                else:
                    unit = d_unit
            else:
                unit = d_unit
        print unit
    else:
        print("no message")
    for idx in enumerate(downs):
        if float(idx[1]) / unit < 2:
            downs[idx[0]] = '.'
        else:
            downs[idx[0]] = '-'
    for idx in enumerate(ups):
        if float(idx[1]) / unit < 2:
            ups[idx[0]] = ''
        elif float(idx[1]) / unit < 4.5:
            ups[idx[0]] = ' '
        else:
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
