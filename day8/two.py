openFile = open("day8/input.txt", "r")
forest = openFile.readlines()

for x in range(0, len(forest)):
    forest[x] = forest[x].strip()

rowLength = len(forest[0])

columnHeight = len(forest)

def toTheRight(forest, x, y):
    counter = 0
    right = x + 1
    while right < rowLength:
        counter += 1
        if forest[y][x] <= forest[y][right]:
            break
        right += 1
    return counter

def toTheLeft(forest, x, y):
    counter = 0
    left = x - 1
    while left >= 0:
        counter += 1
        if forest[y][x] <= forest[y][left]:
            break
        left -= 1
    return counter

def toTheUp(forest, x, y):
    counter = 0
    up = y - 1
    while up >= 0:
        counter += 1
        if forest[y][x] <= forest[up][x]:
            break
        up -= 1
    return counter

def toTheDown(forest, x, y):
    counter = 0
    down = y + 1
    while down < columnHeight:
        counter += 1
        if forest[y][x] <= forest[down][x]:
            break
        down += 1

        
    return counter

score = 0

for rowIndex in range(1, rowLength - 1):
    for columnIndex in range(1, columnHeight - 1):
        tempRight = toTheRight(forest, rowIndex, columnIndex)
        tempLeft = toTheLeft(forest, rowIndex, columnIndex)
        tempUp = toTheUp(forest, rowIndex, columnIndex)
        tempDown = toTheDown(forest, rowIndex, columnIndex)
        tempScore = tempRight * tempLeft * tempUp * tempDown
        if score < tempScore:
            score = tempScore

print(score)
            