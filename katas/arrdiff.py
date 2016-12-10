"""This is called arrdiff just for consistency with the code wars problem. I understand that I am actually using lists."""


def array_diff(a, b):
    """returns list a without any of the numbers that are in list b."""
    to_pop = []
    for num_b in b:
        for ind_a in range(len(a) - 1, -1, -1):
            if a[ind_a] == num_b:
                a.pop(ind_a)
    return a