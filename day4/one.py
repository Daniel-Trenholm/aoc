def insideAnother(range1, range2):
    if (int(range1[0]) <= int(range2[0]) and int(range1[1]) >= int(range2[1])) or (int(range2[0]) <= int(range1[0]) and int(range2[1]) >= int(range1[1])):
        return True
    #else:
        #print(str(range1[0]) + " " + str(range1[1]) + ", " + str(range2[0]) + " " + str(range2[1]))

one = open("day4/input.txt", "r")
lines = one.readlines()
for x in range(0, len(lines)):
    lines[x] = lines[x].split(",")
    for y in range(0, len(lines[x])):
        lines[x][y] = lines[x][y].split("-")

print(len(lines[0][1]))
score = 0
for idSet in lines:
    if insideAnother(idSet[0], idSet[1]):
        score += 1

print("Final number of pairs is: " + str(score))

print(insideAnother([11, 98], [98, 98]))
print(insideAnother([9, 94], [10, 93]))