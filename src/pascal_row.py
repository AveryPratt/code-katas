"""O(k) solution for finding a row in pascal's triangle."""
    

def find_row(row_num):
    """Return the row of pascal's triangle corresponding to the input number."""
    row_num -= 1
    row_str = str(11 ** row_num)
    print(row_str)
    pasc = []
    carry = 0
    prev_carry = 0
    for idx in range(row_num // 2 + 1):
        inner = int(row_str[:-row_num + idx])
        outer = int(row_str[-idx - 1])
        print(carry)
        print(outer)
        print(inner)
        print()
        prev_carry = carry
        carry = inner - outer
        pasc.append(outer + 10 * prev_carry)
        row_str = row_str[-row_num + idx:]
    if row_num % 2:
        pasc.extend(pasc[::-1])
    else:
        pasc.extend(pasc[len(pasc) - 2::-1])
    return pasc
