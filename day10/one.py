openFile = open("day10/input.txt", "r")
instructions = openFile.readlines()
for x in range(0, len(instructions)):
    instructions[x] = instructions[x].strip().split()

array = []
reg = 1
for x in instructions:
    if x[0] == "noop":
        array.append(reg)
    elif x[0] == "addx":
        array.append(reg)
        reg += int(x[1])
        array.append(reg)

sum = 0
for x in range(18, 225, 40):
    print(str(array[x]) + " " + str(x + 2))
    print(array[x] * (x + 2))
    sum += array[x] * (x + 2)

print(sum)
print(len(array))
print(array)