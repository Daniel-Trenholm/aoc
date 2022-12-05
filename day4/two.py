def isOverlap(range1, range2):
    if not (range1[0] > range2[1] or range1[1] < range2[0]) or not (range2[0] > range1[1] or range2[1] < range1[0]):
        return True

one = open("day4/input.txt", "r")
lines = one.readlines()
for x in range(0, len(lines)):
    lines[x] = lines[x].split(",")
    for y in range(0, len(lines[x])):
        lines[x][y] = lines[x][y].split("-")
        for z in range(0, len(lines[x][y])):
            lines[x][y][z] = int(lines[x][y][z])

score = 0
for x in lines:
    if isOverlap(x[0], x[1]):
        score += 1

print(score)