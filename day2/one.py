one = open("day2/input.txt", "r")
lines = one.readlines()
for x in range(0, len(lines)):
    lines[x] = lines[x].split()
score = 0
for x in lines:
    compareNum = ord(x[1])-ord(x[0])
    if compareNum == 23:
        score += 3
    elif compareNum == 24 or compareNum == 21:
        score += 6
    score += ord(x[1])-87
    print(ord(x[1])-87)
print(score)