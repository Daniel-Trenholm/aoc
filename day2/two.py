one = open("day2/input.txt", "r")
lines = one.readlines()
for x in range(0, len(lines)):
    lines[x] = lines[x].split()
score = 0
for x in lines:
    if x[1] == 'Y':
        score += ord(x[0])-64
        print((ord(x[0]))-64)
    elif x[1] == 'Z':
        score += (ord(x[0])-65 + 1) % 3 + 1
    elif x[1] == "X":
        score += (ord(x[0])-65 - 1) % 3 + 1
    score += (ord(x[1])-88) * 3
   # print((ord(x[1])-88) * 3)
print(score)