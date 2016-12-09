"""Tests str_to_arr to see if strings turn into arrays."""


import str_to_arr

assert str_to_arr.string_to_array("Robin Singh") == ["Robin", "Singh"])
assert str_to_arr.string_to_array("CodeWars") == ["CodeWars"])
assert str_to_arr.string_to_array("I love arrays they are my favorite") == ["I", "love", "arrays", "they", "are", "my", "favorite"])
assert str_to_arr.string_to_array("1 2 3") == ["1", "2", "3"])
assert str_to_arr.string_to_array("") == [""])