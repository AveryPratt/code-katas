def count_Kprimes(k, start, end):
    last = 2 ** k
    primes = []
    while last < end:
        if last > start:
            primes.append(int(last))
        pos = []
        mults = [2] * k
        while mults[-1] ** k <= last:
            tmp = 0
            while tmp <= last:
                mults[0] = nxt_prime(mults[0])
                tmp = comp_mults(mults)
            pos.append(tmp)
            mults[1] = nxt_prime(mults[1])
            mults[0] = mults[1]
        last = min(pos)
        for i in range(len(pos)):
            if last == pos[i]:
                mults[i] = nxt_prime(mults[i])
    return primes


def comp_mults(mults):
    val = 1
    for mult in mults:
        val *= mult
    return val


def nxt_prime(num):
    import math
    is_prime = False
    while not is_prime:
        num += 1
        root = math.floor(num ** .5) + 1
        # import pdb; pdb.set_trace()
        stopped = False
        for i in range(2, root):
            if num % i == 0:
                stopped = True
                break
        if not stopped:
            is_prime = True
    return int(num)

def puzzle(s):
    # your code 
    pass
