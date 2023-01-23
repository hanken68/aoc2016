traps = ".^.^..^......^^^^^...^^^...^...^....^^.^...^.^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^"

part1num = 40
numOfLines = 400000

def countTraps(row):
    return len([i for i in list(row) if i == '^'])

def getNextRow(row):
    nextRow = ""
    testRow = "." + row + "."
    for i in range(len(row)):
        if testRow[i:i+3] in ['^^.', '.^^', '^..','..^'] :
            nextRow += '^'
        else:
            nextRow += '.'
    return nextRow
numOfTraps = len(traps) - countTraps(traps)
for i in range(numOfLines-1):
    traps = getNextRow(traps)
    numOfTraps += (len(traps) - countTraps(traps))
    if i == part1num-2:
        print("Part 1:", numOfTraps)

print("Part 2:", numOfTraps)