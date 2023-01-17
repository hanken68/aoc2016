lines = open("inputs\day2.txt","r").read().splitlines()

keypad= [(1,2,3),
        (4,5,6),
        (7,8,9)]

r , c = (1,1)
digits = ""
for l in lines:
    for ch in l:
        match ch:
            case "U": r -= 1
            case "D": r += 1
            case "R": c += 1
            case "L": c -= 1
        if c <0: c=0
        if c>2: c=2
        if r <0: r=0
        if r>2: r=2
    digits += str(keypad[r][c])
part1 = digits
keypad= [(0,0,1,0,0),
        (0,2,3,4,0),
        (5,6,7,8,9),
        (0,'A','B','C',0),
        (0,0,'D',0,0)]

# Part 2
r , c = (3,0)
digits = ""
for l in lines:
    for ch in l:
        r1 = r; c1 = c
        match ch:
            case "U": r1 -= 1
            case "D": r1 += 1
            case "R": c1 += 1
            case "L": c1 -= 1
        if c1<0: c1=0
        if c1>4: c1=4
        if r1<0: r1=0
        if r1>4: r1=4
        if keypad[r1][c1] != 0:
            r=r1; c=c1
    digits += str(keypad[r][c])
part2 = digits

print("Part 1:", part1)
print("Part 2:", part2)