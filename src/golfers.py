"""Solution for Social Golfer Problem Validator kata."""


def valid(a):
    golfers = {}
    group_num = None
    group_size = None
    for day in a:
        if not group_num:
            group_num = len(day)
        else:
            if len(day) != group_num:
                return False
        for group in day:
            if not group_size:
                group_size = len(group)
            else:
                if len(group) != group_size:
                    return False
            active = []
            for golfer in group:
                if golfer in active:
                    return False
                active.append(golfer)
                if day is a[0]:
                    golfers[golfer] = []
                if not golfer in golfers.keys():
                    return False
                for partner in group:
                    if partner is not golfer:
                        if partner in golfers[golfer]:
                            return False
                        golfers[golfer].append(partner)
    return True
