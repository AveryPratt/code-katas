def count_smileys(arr):
    count = 0
    for face in arr:
        eyes = ";", ":"
        mouths = "D", ")"
        noses = "-", "~"
        if len(face) == 2:
            if face[0] in eyes and face[1] in mouths:
                count += 1
        elif len(face) == 3:
            if face[0] in eyes and face[1] in noses and face[2] in mouths:
                count += 1
    return count
