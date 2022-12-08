openFile = open("day8/input.txt", "r")
forest = openFile.readlines()

for x in range(0, len(forest)):
    forest[x] = forest[x].strip()

rowLength = len(forest[0])

columnHeight = len(forest)

totalTrees = 0
totalTrees += 2 * rowLength + 2 * columnHeight - 4

def toTheRight(forest, x, y):
    right = x + 1
    while right < rowLength:
        if forest[y][x] <= forest[y][right]:
            return False
        right += 1
    return True

def toTheLeft(forest, x, y):
    left = x - 1
    while left >= 0:
        if forest[y][x] <= forest[y][left]:
            return False
        left -= 1
    return True

def toTheUp(forest, x, y):
    up = y - 1
    while up >= 0:
        if forest[y][x] <= forest[up][x]:
            return False
        up -= 1
    return True

def toTheDown(forest, x, y):
    down = y + 1
    while down < columnHeight:
        if forest[y][x] <= forest[down][x]:
            return False
        down += 1
    return True

for rowIndex in range(1, rowLength - 1):
    for columnIndex in range(1, columnHeight - 1):
        if (toTheRight(forest, rowIndex, columnIndex) 
        or toTheLeft(forest, rowIndex, columnIndex) 
        or toTheUp(forest, rowIndex, columnIndex) 
        or toTheDown(forest, rowIndex, columnIndex)):
            totalTrees += 1

print(totalTrees)
            