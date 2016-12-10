"""Tests if travel_chessboard returns the correct number of moves"""

def test():
    """iteratively runs several tests for travel_chessboard()"""
    from chess import travel_chessboard
    tests = [
        "(1 1)(3 3)",
        "(2 3)(4 8)",
        "(1 8)(4 8)",
        "(8 1)(8 6)",
        "(1 2)(8 7)",
        "(3 6)(8 7)",
        "(3 1)(7 8)",
        ]
    results = [6, 21, 1, 1, 792, 6, 330]

    for i in range(len(tests)):
        assert travel_chessboard(tests[i]) == results[i]
