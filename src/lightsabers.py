"""Returns number of lightsabers owned by a programmer. (Zach has 18, everyone else has 0)"""


def how_many_lightsabers_do_you_own(programmer=""):
    """Returns 18 lightsabers if you are Zach, and 0 if you are anyone else."""
    if programmer == "Zach":
        return 18
    else:
        return 0
