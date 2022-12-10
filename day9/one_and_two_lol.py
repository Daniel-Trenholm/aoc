class coordinate:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

fileOpen = open("day9/input.txt", "r")
instructions = fileOpen.readlines()
for x in range(0, len(instructions)):
    instructions[x] = instructions[x].strip().split()

seenTiles = {}
seenTiles2 = {}

head = coordinate(0, 0)
tail = coordinate(0, 0)

def moveTail(newHeadLocation: coordinate, oldTailLocation: coordinate):
    #print("Old: " + str(oldHeadLocation.x) + " " + str(oldHeadLocation.y))
    #print("New: " + str(newHeadLocation.x) + " " + str(newHeadLocation.y))
    #print(str(newHeadLocation.x) + " " + str(newHeadLocation.y) + " VS: " + str(oldTailLocation.x) + " " + str(oldTailLocation.y))
    vector = coordinate(0, 0)
    if (abs(newHeadLocation.x - oldTailLocation.x) < 2 and abs(newHeadLocation.y - oldTailLocation.y) < 2):
        return coordinate(oldTailLocation.x, oldTailLocation.y)
    elif abs(newHeadLocation.x - oldTailLocation.x) + abs(newHeadLocation.y - oldTailLocation.y) >= 3:
        if newHeadLocation.x - oldTailLocation.x > 0:
            if newHeadLocation.y - oldTailLocation.y > 0:
                vector = coordinate(1, 1)
            else:
                vector = coordinate(1, -1)
        else:
            if newHeadLocation.y - oldTailLocation.y > 0:
                vector = coordinate(-1, 1)
            else:
                vector = coordinate(-1, -1)
        return coordinate(oldTailLocation.x + vector.x, oldTailLocation.y + vector.y)
    elif abs(newHeadLocation.x - oldTailLocation.x) + abs(newHeadLocation.y - oldTailLocation.y) == 2:
        if (newHeadLocation.x - oldTailLocation.x) == 0:
            if (newHeadLocation.y - oldTailLocation.y) > 1:
                vector = coordinate(0, 1)
            else:
                vector = coordinate(0, -1)
        elif (newHeadLocation.y - oldTailLocation.y) == 0:
            if (newHeadLocation.x - oldTailLocation.x) > 1:
                vector = coordinate(1, 0)
            else:
                vector = coordinate(-1, 0)
        return coordinate(oldTailLocation.x + vector.x, oldTailLocation.y + vector.y)
    #print(str(abs(newHeadLocation.x - oldTailLocation.x)) + " " + str(abs(newHeadLocation.y - oldTailLocation.y)))

#Part 1    
for item in instructions:
    for times in range(0, int(item[1])):
        if item[0] == "U":
            head.y += 1
        elif item[0] == "D":
            head.y -= 1
        elif item[0] == "L":
            head.x -= 1
        elif item[0] == "R":
            head.x += 1
        tail = moveTail(head, tail)

        tileString = str(tail.x) + " " + str(tail.y)
        if tileString not in seenTiles.keys():
            #print(tileString)
            seenTiles[tileString] = True

#Part 2

coords = []
for x in range(10):
    coords.append(coordinate(0, 0))

for item in instructions:
    for times in range(0, int(item[1])):
        if item[0] == "U":
            coords[0].y += 1
        elif item[0] == "D":
            coords[0].y -= 1
        elif item[0] == "L":
            coords[0].x -= 1
        elif item[0] == "R":
            coords[0].x += 1
        for index in range(1, len(coords)):
            coords[index] = moveTail(coordinate(coords[index - 1].x, coords[index - 1].y), coordinate(coords[index].x, coords[index].y)) 
        tileString = str(coords[9].x) + " " + str(coords[9].y)
        if tileString not in seenTiles2.keys():
            #print(tileString)
            seenTiles2[tileString] = True

#print(len(seenTiles))
print(len(seenTiles2))