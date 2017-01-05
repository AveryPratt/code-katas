


def brain_luck(code, txt):
    cells = [0]
    final = ""
    pointer = 0
    skip_forward = False
    skip_backward = False
    inc = 1
    cmd = 0
    nest = 0
    while cmd in range(0, len(code)):
        if code[cmd] == "[":
            if skip_backward:
                nest -= 1
                if nest == 0:
                    skip_backward = False
                    inc = 1
            elif cells[pointer] == 0:
                nest += 1
                skip_forward = True
        elif code[cmd] == "]":
            if skip_forward:
                nest -= 1
                if nest == 0:
                    skip_forward = False
            elif cells[pointer] != 0:
                nest += 1
                skip_backward = True
                inc = -1
        elif not skip_forward and not skip_backward:
            if code[cmd] == '>':
                pointer += 1
                if len(cells) == pointer:
                    cells.append(0)
            elif code[cmd] == '<':
                if pointer >= 1:
                    pointer -= 1
            elif code[cmd] == '+':
                cells[pointer] += 1
                if cells[pointer] > 255:
                    cells[pointer] -= 256
            elif code[cmd] == '-':
                cells[pointer] -= 1
                if cells[pointer] < 0:
                    cells[pointer] += 256
            elif code[cmd] == '.':
                final += chr(cells[pointer])
            elif code[cmd] == ',':
                cells[pointer] = ord(txt[0])
                txt = txt[1:]
        cmd += inc
    for ind in range(len(cells)):
        cells[ind] = chr(cells[ind])
    return final
