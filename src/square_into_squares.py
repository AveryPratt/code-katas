"""Solution for Square into Squares kata."""


def decompose(num):
    square = num ** 2
    others = []
    for k in range(num - 1, 0, -1):
        others.append(k ** 2)
    stack = []
    start = 0
    try:
        while True:
            for other in others[start:]:
                if sum(stack) + other > square:
                    continue
                stack.append(other)
                if sum(stack) == square:
                    for idx, item in enumerate(stack):
                        stack[idx] = item ** .5
                    stack.reverse()
                    return stack
            start = others.index(stack.pop()) + 1
    except IndexError:
        return None
