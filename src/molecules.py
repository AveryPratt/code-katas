"""Solution for molecules to atoms kata."""


def parse_molecule (formula):
    """Return a dictionary containing the number of each atom in the molecule."""
    open_parens = "([{"
    closed_parens = "}])"
    space_ind = []
    for char in enumerate(formula):
        if (char[1].isupper() or
                char[1] in open_parens or
                char[1] in closed_parens):
            space_ind.append(char[0])
    for ind in space_ind[::-1]:
        formula = formula[:ind] + " " + formula[ind:]
    item_list = formula.split()
    mult = []
    atoms = {}
    for item in item_list[::-1]:
        if len(item) == 1:
            if item[0] in open_parens:
                mult.pop()
            elif item[0] in closed_parens:
                mult.append(1)
            else:
                multiplier = 1
                for num in mult:
                    multiplier *= num
                try:
                    atoms[item] += multiplier
                except KeyError:
                    atoms[item] = multiplier
        else:
            if item[0] in closed_parens:
                mult.append(int(item[1:]))
            elif item[1].isdigit():
                multiplier = int(item[1:])
                for num in mult:
                    multiplier *= num
                try:
                    atoms[item[:1]] += multiplier
                except KeyError:
                    atoms[item[:1]] = multiplier
            elif len(item) > 2:
                multiplier = int(item[2:])
                for num in mult:
                    multiplier *= num
                try:
                    atoms[item[:2]] += multiplier
                except KeyError:
                    atoms[item[:2]] = multiplier
            else:
                multiplier = 1
                for num in mult:
                    multiplier *= num
                try:
                    atoms[item] += multiplier
                except KeyError:
                    atoms[item] = multiplier
    return atoms
