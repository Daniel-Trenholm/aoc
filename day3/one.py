def findSameLetterValue(halfOne, halfTwo):
    for firstHalfItem in halfOne:
        for secondHalfItem in halfTwo:
            if firstHalfItem == secondHalfItem:
                if firstHalfItem.isupper():
                    return ord(firstHalfItem) - 38
                elif firstHalfItem.islower():
                    return ord(firstHalfItem) - 96

one = open("day3/input.txt", "r")
lines = one.readlines()

for x in range(0, len(lines)):
    lines[x] = [lines[x][0:len(lines[x])//2], lines[x][len(lines[x])//2:]]

sum = 0

for line in lines:
    sum += findSameLetterValue(line[0], line[1])

print(sum)
