one = open("day5/input.txt", "r")
lines = one.readlines()
stack =  []
for x in range(0, 9):
    stack.append([])


#Read in initial stack
for x in range(0, 8):
    for y in range(0, 9):
        if 1+4*y < len(lines[x]):
            if lines[x][1+4*y] != " ":
                stack[y].append(lines[x][1+4*y])

instructionWords = []
instructions = []
#Read in instructions
for x in range(10, len(lines)):
    instructionWords.append(lines[x].strip().split(" "))
for x in instructionWords:
    instructions.append([int(x[1]), int(x[3]), int(x[5])])

#Put the items in the stacks initial states

for x in range(0, len(stack)):
    stack[x].reverse()

#Execute all instructions
#But this time flip the section of the list before appending and popping
for x in instructions:
    stack[x[1]-1][-1 * x[0]: len(stack[x[1]-1])] = stack[x[1]-1][-1 * x[0]: len(stack[x[1]-1])][::-1]
    for y in range(0, x[0]):
        stack[x[2]-1].append(stack[x[1]-1].pop())
print(stack)
print(len(stack[1][-1 * 6: len(stack[1])]))

#Get results
resultList = []
for x in stack:
    resultList.append(x[-1])
finalString = "".join(str(e) for e in resultList)

print(finalString)