def snail(array):
    fin = []
    n = len(array)
    dir = 0
    point = [0, -1]
    for num in range(2 * n, 0, -1):
        for k in range(num // 2):
            if dir % 4 == 0:
                point[1] += 1
            elif dir % 4 == 1:
                point[0] += 1
            elif dir % 4 == 2:
                point[1] -= 1
            else:
                point[0] -= 1
            fin.append(array[point[0]][point[1]])
        dir += 1
    return fin
