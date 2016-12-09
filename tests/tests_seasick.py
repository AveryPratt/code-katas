"""Tests if snorkelers and boat-goers will throw up."""


import seasick


assert sea_sick("~") == "No Problem"
assert sea_sick("_~~~~~~~_~__~______~~__~~_~~") == "Throw Up"
assert sea_sick("______~___~_") == "Throw Up"
assert sea_sick("____") == "No Problem"
assert sea_sick("_~~_~____~~~~~~~__~_~") == "Throw Up"