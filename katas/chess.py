"""Finds the total number of available paths between two spaces on a chessboard while only moving down and right."""


def travel_chessboard(s):
    dx = 1 + int(s[6]) - int(s[1])
    dy = 1 + int(s[8]) - int(s[3])
    grid = []
    for col in range(0, dx):
        lst = []
        grid.append(lst)
        for row in range(0, dy):
            lst.append(1)
    for col in range(1, len(grid)):
        for row in range(0, len(grid[col])):
            total = 0
            for ind in range(0, row + 1):
                total += grid[col - 1][ind]
            grid[col][row] = total
    return grid[dx - 1][dy - 1]