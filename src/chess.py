"""Finds the total number of available paths between two spaces
on an 8 x 8 chessboard while only moving down and right."""


def travel_chessboard(inp):
    """creates a mini-grid between the two spaces and calculates
    all the possible paths between them."""
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
