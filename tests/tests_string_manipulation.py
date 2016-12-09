"""Tests string_manipulation to see if it manipulates strings properly."""


import string_manipulation


s1, s2 ="FizZ", "buZZ"
assert reverseAndMirror(s1,s2) == "zzUB@@@zZIffIZz"

s1, s2 ="String Reversing", "Changing Case"
assert reverseAndMirror(s1,s2) == "ESAc GNIGNAHc@@@GNISREVEr GNIRTssTRING rEVERSING"
