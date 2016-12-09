import pytest
import lightsabers

assert lightsabers.howManyLightsabersDoYouOwn() == 0
assert lightsabers.howManyLightsabersDoYouOwn("Bob") == 0
assert lightsabers.howManyLightsabersDoYouOwn(12) == 0
assert lightsabers.howManyLightsabersDoYouOwn("Zach") == 18