import itertools
from collections import deque

lines = open("inputs/day22.txt", "r").read().splitlines()
# lines = open("inputs/sample.txt", "r").read().splitlines()

def moveSpace(s, d, a): #source, destination, avoid (where G is)
    _q = deque()
    _q.append((s,0))
    _v=set()
    while _q:
        (x1,y1), _s = _q.popleft()
        _v.add((x1,y1))
        for _d in directions:
            x = x1+_d[0]; y = y1+_d[1]
            if (x,y) == a or (x,y) in _v: 
                continue
            if (x,y) in nodes and not((x,y) in full):
                if (x,y) == d: # at destination
                    return _s+1
                _q.append(((x,y),_s+1))
    return -1

full=set()
size={}
used={}
avail={}
usep={}
nodes=set()
xmax=0
for i,l in enumerate(lines):
    if i<2:
        continue
    p = l.split()
    c = p[0].split("-")
    x = int(c[1][1:]); y = int(c[2][1:])
    if y==0:
        xmax = max(x, xmax)
        target = (xmax,y)
    coord = (x,y)
    size[coord] = int(p[1][:-1])
    used[coord] = int(p[2][:-1])
    avail[coord] = int(p[3][:-1])
    usep[coord] = int(p[4][:-1])
    nodes.add(coord)
    if used[coord] == 0:
        empty = coord

viable=0
for c in itertools.combinations(nodes,2):
    a=c[0]; b=c[1]
    if (used[a]>0 and avail[b]>=used[a]) or (used[b]>0 and avail[a]>=used[b]):
        viable += 1


print("Part 1:", viable)
# print("Empty:", empty)
# print("MaxX:", target, size[target])


# generate new nodes
capacity = size[empty]
for a in nodes:
    if used[a]>capacity :
        full.add(a)

# print(full)


q = deque()
r = deque() # que for return
vis = set()

#first move empty towards target

q.append((empty, 0))
directions = [(0,1),(0,-1),(1,0),(-1,0)]

while q:
    (x1,y1), s = q.popleft()
    vis.add((x1,y1))
    for d in directions:
        x = x1+d[0]; y = y1+d[1]
        if ((x,y) in nodes) and not((x,y) in full): # existing node
            if (x,y) in vis:
                continue # bin here...
            if(x,y) == target:
                if(((x1,y1),s+1,(x,y)) not in r):
                    r.append(((x1,y1),s+1,(x,y)))
                continue
            q.append(((x,y),s+1))
            vis.add((x,y))
            
# start over with return trip.
vis=set()
vis.add(target)

returnedToHome = False
while r:
    (x1,y1), s, space = r.popleft()
    vis.add((x1,y1))
    for d in directions:
        x = x1+d[0]; y = y1+d[1]
        if (x,y) in nodes and not((x,y) in full): # existing node 
            if (x,y) in vis:
                continue
            _s = moveSpace(space, (x,y), (x1,y1))
            if (x,y) == (0,0): # back home :-)
                returnedToHome = True
                print("Part 2:", s + _s + 1)
                exit(0)
            r.append(((x,y), s + _s + 1,(x1,y1)))
            vis.add((x,y))
            




