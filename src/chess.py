"""Finds the total number of available paths between two spaces on a chessboard."""


def travel_chessboard(inp):
    """player can only move down and right."""
    d_x = 1 + int(inp[6]) - int(inp[1])
    d_y = 1 + int(inp[8]) - int(inp[3])
    grid = []
    for col in range(0, d_x):
        lst = []
        grid.append(lst)
        for row in range(0, d_y):
            lst.append(1)
    for col in range(1, len(grid)):
        for row in range(0, len(grid[col])):
            total = 0
            for ind in range(0, row + 1):
                total += grid[col - 1][ind]
            grid[col][row] = total
    return grid[d_x - 1][d_y - 1]
