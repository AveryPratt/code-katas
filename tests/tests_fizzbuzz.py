"""Tests fizzbuzz.py to make sure the correct results are returned at various times."""


import fizzbuzz

   
assert(fizzbuzz.fizz_buzz_cuckoo_clock("13:34") == "tick"
assert(fizzbuzz.fizz_buzz_cuckoo_clock("21:00") == "Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo"
assert(fizzbuzz.fizz_buzz_cuckoo_clock("11:15") == "Fizz Buzz"
assert(fizzbuzz.fizz_buzz_cuckoo_clock("03:03") == "Fizz"
assert(fizzbuzz.fizz_buzz_cuckoo_clock("14:30") == "Cuckoo"
assert(fizzbuzz.fizz_buzz_cuckoo_clock("08:55") == "Buzz"