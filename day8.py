lines = open("inputs\day8.txt","r").read().splitlines()

def printGrid(printout):
    numLit = 0
    for r in grid:
        row = ""
        for c in r:
            if c == "#": numLit += 1
            row += c
        if printout: print(row)
    return numLit


# 6 rows and 50 columns
rl = 50
cl = 6


grid = []
row = " " * rl
for r in range(cl):
    grid.append(list(row))

for line in lines:
    parts = line.split()
    match parts[0]:
        case 'rect':
            c1, r1 = list(map(int, parts[1].split("x")))
            for r in range(r1):
                for c in range(c1):
                    grid[r][c] = '#'
        case 'rotate':
            start = int(parts[2].split("=")[1])
            num = int(parts[4])
            match parts[1]:
                case 'row':
                    memory = grid[start].copy()
                    for c in range(len(memory)):
                        dest = (c + num) % rl
                        grid[start][dest]=memory[c]  
                case 'column':
                    memory = []
                    for r in grid:
                        memory.append(r[start])
                    for r in range(cl):
                        dest = (r + num) % cl
                        grid[dest][start] = memory[r]

part1 = printGrid(False)


print("Part 1:", part1)
print("Part 2:")
printGrid(True)