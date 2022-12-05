one = open("day5/input.txt", "r")
lines = one.readlines()
stack =  []
for x in range(0, 9):
    stack.append([])


#Read in initial stack
for x in range(0, 8):
    for y in range(0, 9):
        print(len(lines[x]))
        if 1+4*y < len(lines[x]):
            if lines[x][1+4*y] != " ":
                print(stack)
                stack[y].append(lines[x][1+4*y])

instructionWords = []
instructions = []
#Read in instructions
for x in range(10, len(lines)):
    instructionWords.append(lines[x].strip().split(" "))
for x in instructionWords:
    instructions.append([int(x[1]), int(x[3]), int(x[5])])

print(instructions[0])

#Put the items in the stacks initial states

for x in range(0, len(stack)):
    stack[x].reverse()

#Execute all instructions
for x in instructions:
    for y in range(0, x[0]):
        stack[x[2]-1].append(stack[x[1]-1].pop())

resultList = []
for x in stack:
    resultList.append(x[-1])
finalString = "".join(str(e) for e in resultList)

print(finalString)