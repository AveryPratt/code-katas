import math


def count_primes():
    with open('primes.txt', 'w') as fial:
        start = 2
        while start < 100000:
            fial.write(str(start) + " ")


def count_Kprimes(k, start, end):
    primes = set()
    mults = [2] * k
    done = False
    while not done:
        pointer = 0
        tmp = comp_mults(mults)
        caught = True
        while tmp <= end:
            caught = False
            if start <= tmp:
                primes.add(int(tmp))
            tmp /= mults[pointer]
            mults[pointer] = nxt_prime(mults[pointer])
            tmp *= mults[pointer]
        if len(mults) == 1:
            done = True
        if caught:
            try:
                while mults[pointer] == mults[pointer + 1]:
                    pointer += 1
                    if pointer >= len(mults) - 1:
                        done = True
                        break
            except IndexError:
                done = True
        if not done:
            base = nxt_prime(mults[pointer + 1])
            for i in range(pointer + 2):
                mults[i] = base
    return sorted(list(primes))


def comp_mults(mults):
    val = 1
    for mult in mults:
        val *= mult
    return val


def nxt_prime(num):
    is_prime = False
    while not is_prime:
        num += 1
        root = math.floor(math.sqrt(num)) + 1
        stopped = False
        for i in range(2, int(root)):
            if num % i == 0:
                stopped = True
                break
        if not stopped:
            is_prime = True
    return int(num)


def puzzle(s):
    count = 0
    set_a = count_Kprimes(1, 0, s - 136)
    set_b = count_Kprimes(3, 0, s - 130)
    set_c = count_Kprimes(7, 0, s - 10)
    for c in set_c:
        for b in set_b:
            for a in set_a:
                if a + b + c == s:
                    count += 1
    return count
