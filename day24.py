from collections import deque
import itertools
lines = open("inputs/day24.txt", "r").read().splitlines()

def appendStep(start, pos, steps):
    dist[(start, pos)] = steps
    dist[(pos, start)] = steps

def getSum(start, pp):
    sum = 0
    for i in range(len(pp)-1):
        if i==0:
            sum = dist[((start),(pp[i]))]
        sum += dist[(pp[i]), pp[i+1]]
    s2 = sum + dist[(start),pp[len(pp)-1]]
    return sum, s2
        

# Parse innput
poi={}
p = set()
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if (ch in ['#','.']):
            pass
        else:
            if ch == '0':
                start = (c,r)
                p.add((c,r))
            else:
                poi[(c,r)] = int(ch)
                p.add((c,r))



dist={} # dictionary with steps between nodes.
paths = itertools.combinations(p,2)
for pp in paths:
    dist[(pp[1],pp[0])] = -1
    dist[pp] = -1

directions = ((0,1),(0,-1),(1,0),(-1,0))
nc = len(lines[0])
nr = len(lines)


for n in p:
    vis = set()
    q = deque()
    q.append((n, 0))
    while q:
        pos, s = q.popleft()
        vis.add(pos)
        for d in directions:
            c, r = (pos[0]+d[0], pos[1]+d[1])
            if c<0 or r <0 or c>nc-1 or r>nr-1:
                continue # out of bounds
            if (c,r) in vis:
                continue # been there
            if lines[r][c] == '#':
                continue
            if (c,r) in p:
                # target
                appendStep(n, (c,r), s+1)
                # print((c,r), s+1)
            q.append(((c,r), s+1))
            vis.add((c,r))


# for d in dist:
#     print(d, dist[d])

paths = itertools.permutations(poi,len(poi))
returnNum = None
part1 = None
part2 = None
for i,pp in enumerate(paths):
    _s, _s2 = getSum(start, pp)
    if part1 != None:
        part1 = min(part1, _s)
    else:
        part1 = _s
    if part2 != None:
        part2 = min(part2, _s2)
    else:
        part2 = _s2

print("Part 1:", part1)
print("Part 2:", part2)