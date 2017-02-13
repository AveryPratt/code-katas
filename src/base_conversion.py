"""solution for base conversion kata."""

# Alphabet = {}
# Alphabet.BINARY = "01"
# Alphabet.OCTAL = "01234567"
# Alphabet.DECIMAL = "0123456789"
# Alphabet.HEXA_DECIMAL = "0123456789abcdef"
# Alphabet.ALPHA_LOWER = "abcdefghijklmnopqrstuvwxyz"
# Alphabet.ALPHA_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Alphabet.ALPHA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Alphabet.ALPHA_NUMERIC = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


ALPHABETS = {
        "bin": "01",
        "oct": "01234567",
        "dec": "0123456789",
        "hex": "0123456789abcdef",
        "allow": "abcdefghijklmnopqrstuvwxyz",
        "allup": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "alpha": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "alphanum": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    }


def convert(inp, source, target):
    mult = 1
    cum = 0
    for char in inp[::-1]:
        idx = source.index(char)
        cum += idx * mult
        mult *= len(source)
    out_str = ""
    while cum >= len(target):
        out_str += target[cum % len(target)]
        cum = cum // len(target)
    out_str += target[cum]
    return out_str[::-1]
