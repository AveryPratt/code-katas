"""Solution for pick peaks kata."""


def pick_peaks(arr):
    peaks = {"pos": [], "peaks": []}
    if len(arr) > 2:
        for tup in enumerate(arr[:-1]):
            if tup[0] == 0 or arr[tup[0] - 1] >= tup[1] or check_not_plat(arr, tup[0]):
                continue
            peaks["pos"].append(tup[0])
            peaks["peaks"].append(tup[1])
    return peaks


def check_not_plat(arr, idx):
    peak = arr[idx]
    for num in arr[idx:]:
        if num > peak:
            return True
        elif num < peak:
            return False
    return True
