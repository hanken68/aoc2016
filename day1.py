infile = 'inputs\day1.txt'
line = open(infile, "r").read()
dir = line.split(", ")

x, y = (0,0)
direction = (1, 0)
visited = set()
twice = None
for d in dir:
    cd = d[:1]
    steps = int(d[1:])
    match direction:
        case (1,0):
            direction =  (0,-1) if cd == "L" else (0, 1)
        case (-1,0):
            direction =  (0,1) if cd == "L" else (0, -1)
        case (0,1):
            direction =  (1,0) if cd == "L" else (-1, 0)
        case (0,-1):
            direction =  (-1,0) if cd == "L" else (1, 0)
    for i in range(steps):
        x += direction[0] * 1    
        y += direction[1] * 1
        if (x,y) in visited:
            if twice == None:
                print("Twice")
                twice = (x,y)
        else:
            visited.add((x,y))

print("Part 1:", x+y)
print("Part 2:", twice[0]+twice[1])



