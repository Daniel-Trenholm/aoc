def findCommons(list1, list2):
    returnList = []
    for x in list1:
        for y in list2:
            if x == y:
                returnList.append(x)
    return returnList

def findSameLetterValue(halfOne, halfTwo):
    for firstHalfItem in halfOne:
        for secondHalfItem in halfTwo:
            if firstHalfItem == secondHalfItem:
                print(firstHalfItem)
                if firstHalfItem.isupper():
                    return ord(firstHalfItem) - 38
                elif firstHalfItem.islower():
                    return ord(firstHalfItem) - 96

one = open("day3/input.txt", "r")
lines = one.readlines()

squadsworth = []

for x in range(0, len(lines), 3):
    squadsworth.append([lines[x], lines[x+1], lines[x+2]])

score = 0
for x in squadsworth:
    score += findSameLetterValue(findCommons(x[0], x[1]), x[2])

print(score)