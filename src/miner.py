"""Solution for miner kata."""


def solve(map, miner, door):
    tried = [miner]
    paths = [[miner, []]]
    while paths:
        for path in paths:
            directions = {
                'up': {'x': path[0]['x'], 'y': path[0]['y'] - 1},
                'down': {'x': path[0]['x'], 'y': path[0]['y'] + 1},
                'left': {'x': path[0]['x'] - 1, 'y': path[0]['y']},
                'right': {'x': path[0]['x'] + 1, 'y': path[0]['y']},
            }
            for place in directions:
                if validate(directions[place], map, tried):
                    tried.append(directions[place])
                    new_path = [directions[place], path[1] + [place]]
                    if new_path[0] == door:
                        return new_path[1]
                    paths.append(new_path)
            paths.remove(path)
    return []


def validate(place, map, tried):
    if (place['x'] >= len(map) or
            place['x'] < 0 or
            place['y'] >= len(map[0]) or
            place['y'] < 0 or
            not map[place['x']][place['y']] or
            place in tried):
        return False
    return True
