openFile = open("day10/input.txt", "r")
instructions = openFile.readlines()
for x in range(0, len(instructions)):
    instructions[x] = instructions[x].strip().split()

array = []
crt = []

reg = 1
array.append(reg)
for x in instructions:
    if x[0] == "noop":
        array.append(reg)
    elif x[0] == "addx":
        array.append(reg)
        reg += int(x[1])
        array.append(reg)

for x in range(0, len(array)):
    if abs(array[x] - x % 40) < 2:
        crt.append("#")
    else:
        crt.append(".")

for x in range(0, 6):
    print("".join(crt[x * 40 : x * 40 + 40]) + "\n")