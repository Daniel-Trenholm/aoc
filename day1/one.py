one = open("day1/input.txt", "r")
lines = one.readlines()
compareNum = 0
newNum = 0
for x in lines:
    x = x.strip()
for x in lines:
    if x == "\n":
        if newNum > compareNum:
            compareNum = newNum
        newNum = 0
    else:
        newNum += int(x)
print(compareNum)

