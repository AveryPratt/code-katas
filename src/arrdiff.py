"""Subtracts one list from the other to see which values are inconsistent."""


def array_diff(lst_a, lst_b):
    """returns list a without any of the numbers that are in list b."""
    for num_b in lst_b:
        for ind_a in range(len(lst_a) - 1, -1, -1):
            if lst_a[ind_a] == num_b:
                lst_a.pop(ind_a)
    return lst_a
