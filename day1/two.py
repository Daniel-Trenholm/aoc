one = open("day1/input.txt", "r")
lines = one.readlines()
for x in lines:
    x = x.strip()
top = [0, 0, 0]
newNum = 0
for x in lines:
    if x == "\n":
        if newNum > top[0] or newNum > top[1] or newNum > top[2]:
            top[2] = newNum
            top.sort(reverse=True)
        newNum = 0
    else:
        newNum += int(x)
print(top[0]+top[1]+top[2])