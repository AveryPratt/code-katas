"""Creates a list of prime factors for a series of numbers,
and finds the sum of all the numbers they are a prime factor for."""


import math


def sum_for_list(lst):
    """Returns a list of lists, where each sublist contains a prime factor
    and the sum of all the numbers it is a factor of in the input list."""
    output = []
    factors_kvp = {}
    for item in lst:
        factors = find_prime_factors(item)
        for factor in factors:
            if factor in factors_kvp.keys():
                factors_kvp[factor] += item
            else:
                factors_kvp[factor] = item
    for key in factors_kvp:
        output.append([key, factors_kvp[key]])
    output.sort()
    return output

def find_prime_factors(num):
    """Finds all the prime factors of a specific integer"""
    factors = []
    for pos in range(1, int(math.floor(math.fabs(num) ** .5) + 1)):
        if num % pos == 0:
            factors.append(pos)
            factors.append(math.fabs(int(num / pos)))
    for ind in range(len(factors) - 1, 0, -1):
        factor = factors[ind]
        for pos in range(2, math.floor(factor ** .5) + 1):
            if factor % pos == 0:
                factors.pop(factors.index(factor))
                break
    return factors[1:]
