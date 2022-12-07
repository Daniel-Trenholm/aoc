file = open("day7/input.txt", "r")
lines = file.readlines()

directoryDict = {}

for x in range(0, len(lines)):
    lines[x] = lines[x].split()

# Parse the data into a workable dictionary
stringBuild = []
directoryName = ""
state = 0
for x in lines:
        if x[1] == "cd" and x[0] == "$":
            if x[2] == "..":
                stringBuild.pop()
            else:
                stringBuild.append(x[2]+"/")
                directoryName = "".join(stringBuild)
                if not directoryName in directoryDict:
                    directoryDict[directoryName] = []
                state = 1
        elif state == 1 and x[1] == "ls" and x[0] == "$":
            state = 2
        elif state == 2:
            if x[0] == "dir":
                directoryDict[directoryName].append(x[1])
            else:
                directoryDict[directoryName].append(int(x[0]))

print(directoryDict)

#now for recursive value calculation

def findDirectorySum(dictKey):
    sum = 0
    for y in directoryDict[dictKey]:
        if type(y) == int:
            sum += y
        elif type(y) == str:
            #print(y)
            address = dictKey+y+"/"
            sum += findDirectorySum(address)
    return sum

#Part one
outerSum = 0
for x in directoryDict:
    keySum = findDirectorySum(x)
    if keySum < 100000:
        outerSum += keySum
    
print(outerSum)

#Part Two
usedSpace = findDirectorySum("//")
currentlyUnused = 70000000 - usedSpace
bottom = 30000000 - currentlyUnused
smallestWorks = usedSpace
directorySizes = []
for x in directoryDict:
    tempSmaller = findDirectorySum(x)
    directorySizes.append(tempSmaller)
    if tempSmaller >= bottom and tempSmaller < smallestWorks:
        smallestWorks = tempSmaller

directorySizes.sort()

print(directorySizes)
print(usedSpace)
print("Bottom is " + str(bottom))
print(smallestWorks)