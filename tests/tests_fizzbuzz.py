"""Tests fizz_buzz_cuckoo_clock to make sure the correct results are returned at various times."""


def test1():
    """tests tick"""
    from fizzbuzz import fizz_buzz_cuckoo_clock
    assert fizz_buzz_cuckoo_clock("13:34") == "tick"


def test2():
    """tests for "Cuckoo"s on the hour"""
    from fizzbuzz import fizz_buzz_cuckoo_clock
    assert fizz_buzz_cuckoo_clock("21:00") == ("Cuckoo " * 9)[:-1]


def test3():
    """tests for "Fizz Buzz" every 15 minutes"""
    from fizzbuzz import fizz_buzz_cuckoo_clock
    assert fizz_buzz_cuckoo_clock("11:15") == "Fizz Buzz"


def test4():
    """tests for "Fizz" every 3 minutes"""
    from fizzbuzz import fizz_buzz_cuckoo_clock
    assert fizz_buzz_cuckoo_clock("03:03") == "Fizz"


def test5():
    """tests for "Cuckoo" every half hour"""
    from fizzbuzz import fizz_buzz_cuckoo_clock
    assert fizz_buzz_cuckoo_clock("14:30") == "Cuckoo"


def test6():
    """tests for "Buzz" every 5 minutes"""
    from fizzbuzz import fizz_buzz_cuckoo_clock
    assert fizz_buzz_cuckoo_clock("08:55") == "Buzz"
