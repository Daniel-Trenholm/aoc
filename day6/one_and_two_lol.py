one = open("day6/input.txt", "r")
line = one.readline()

checkList = []

def list_check(checkList):
    for x in range(0, len(checkList) - 1):
        for y in range(x+1, len(checkList)):
            if checkList[x] == checkList[y]:
                return False
    return True

def start_of_message_finder(size, message):
    for x in range(0, len(line)):
        if list_check(checkList) and len(checkList) == size:
            return x
        else:
            checkList.append(line[x])
            if len(checkList) > size:
                checkList.pop(0)
    
print("Part One's answer is: " + str(start_of_message_finder(4, line)))
print("Part Two's answer is: " + str(start_of_message_finder(14, line)))