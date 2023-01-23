from collections import deque

puzzleInput = 1364
target = (31,39)
# puzzleInput = 10
# target = (7,4)

def isOpenSpace(x,y, favnum):
    bnum = list(bin((x*x + 3*x + 2*x*y + y + y*y) + favnum))
    l = len([i for i in bnum if i == '1'])
    return l % 2 == 0
   
x, y = (1,1)


visited = set()
visited50 = set()

q = deque()
q.append((1,1,0))
while q:
    x,y,s = q.popleft()
    if s <= 50: visited50.add((x,y))
    visited.add((x,y))
    for d in [(1,0), (-1,0), (0,1), (0,-1)]:
        x1 = x + d[0]; y1 = y + d[1]
        if x1 < 0 or y1 <0:
            continue
        if x1 == target[0] and y1 == target[1]: # goal
            print("Part 1:", s+1)
            print("Part 2:", len(visited50))
            exit(0)
        if not((x1,y1) in visited):
            if isOpenSpace(x1,y1, puzzleInput): # possible to go here
                q.append((x1,y1,s+1))
