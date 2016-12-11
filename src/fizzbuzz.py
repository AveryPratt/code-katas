"""Returns various strings based on the time input into fizz_buzz_cuckoo_clock."""


def fizz_buzz_cuckoo_clock(time):
    """Cuckoos every half hour, fizzes every 3 minutes, and buzzes every 5 minutes."""
    minute = int(time[3:])
    fizz = False
    buzz = False
    if minute % 3 == 0:
        fizz = True
    if minute % 5 == 0:
        buzz = True
    if minute == 0:
        hour = int(time[:2]) % 12
        return ("Cuckoo " * hour)[:-1]
    elif minute == 30:
        return "Cuckoo"
    elif fizz and buzz:
        return "Fizz Buzz"
    elif fizz:
        return "Fizz"
    elif buzz:
        return "Buzz"
    else:
        return "tick"
