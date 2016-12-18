def brain_luck(code, input):
    pointer = 0
    pointed_byte = 0
    for cmd in range(0, len(code)):
        if cmd == '>':
            pointer += 1
        elif cmd == '<':
            pointer -= 1
        elif cmd == '+':
            val = ord(input[pointer]) + 1
            if val > 255:
                val -= 256
            input[pointer] = chr(val)
        elif cmd == '-':
            val = ord(input[pointer]) - 1
            if val < 0:
                val += 256
            input[pointer] = chr(val)
        elif cmd == '.':
            input[pointer] = pointed_byte
        elif cmd == ',':
            pointed_byte = input[pointer]
        elif cmd == '[' and pointed_byte == 0:
            while True:
                pointer += 1
                if input[pointer] == "]":
                    pointer += 1
                    break
        elif cmd == ']' and pointed_byte != 0:
            while True:
                pointer -= 1
                if input[pointer] == "]":
                    pointer -= 1
                    break
    return input
