"""Returns various strings based on the time input into fizz_buzz_cuckoo_clock"""


def fizz_buzz_cuckoo_clock(time):
    min = int(time[3:])
    fizz = False
    buzz = False
    if min % 3 == 0:
        fizz = True
    if min % 5 == 0:
        buzz = True
    if min == 0:
        hr = int(time[:2]) % 12
        return ("Cuckoo " * hr)[:-1]
    elif min == 30:
        return "Cuckoo"
    elif fizz and buzz:
        return "Fizz Buzz"
    elif fizz:
        return "Fizz"
    elif buzz:
        return "Buzz"
    else:
        return "tick"