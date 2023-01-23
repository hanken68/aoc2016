import re
from collections import deque
import itertools
import copy

lines = open("inputs\day11.txt","r").read().splitlines()
# lines = open("inputs\sample.txt","r").read().splitlines()

def printItems(it, e):
    for i in it:
        if e == i:
            print(i, 'E', it[i])
        else:
            print(i, ' ', it[i])

def floorBaseline(floor, items):
    candidates = {}
    numOfGenerators = 0
    for g in items[floor]:
        if not(g[1] in candidates):
            candidates[g[1]] = [False, False]
        if g[0] == 'g': 
            candidates[g[1]][0] = True
            numOfGenerators += 1
        else: candidates[g[1]][1] = True
    return candidates, numOfGenerators

def addFloorToBaseline(floorbaseline, floortoadd, generators):
    possibleCombinations = []
    itemsAdded = []
    
    for g in items[floortoadd]:
        fbt = copy.deepcopy(floorbaseline)
        if not(g[1] in fbt):
            fbt[g[1]] = [False, False]
        if g[0] == 'g': 
            fbt[g[1]][0] = True
        else: 
            fbt[g[1]][1] = True
        if checkValidity(fbt):
            possibleCombinations.append(fbt)
            itemsAdded.append([g])

    for i in itertools.combinations(items[e],2):
        fbt = copy.deepcopy(floorbaseline)
        for g in i:
            if not(g[1] in fbt):
                fbt[g[1]] = [False, False]
            if g[0] == 'g': 
                fbt[g[1]][0] = True
            else: 
                fbt[g[1]][1] = True
        if checkValidity(fbt):
            possibleCombinations.append(fbt)
            itemsAdded.append(i)
    return possibleCombinations, itemsAdded


def checkValidity(floorbaseline):
    numOfGenerators = len([i for i in floorbaseline if floorbaseline[i][0]==True])

    # check if single chips can be fried
    for g in floorbaseline:
        test = floorbaseline[g][0]
        if floorbaseline[g][0] == False: # Single chip, if generators on flor, fried.
            if numOfGenerators>0:
                return False
    return True

def checkVisited(it,e):
    arr = str(e)
    for e in it:
        arr += str(e) + str(sorted(it[e]))
    if arr in visited:
        return True
    else:
        visited.add(arr)
        return

itemsStart= {} # dictionary with floor as key, containing tuples, first identifieng type m or g, seco
numOfItems = 0
for i, line in enumerate(lines):
    generators = re.findall(r"(\w+)(?=\s+generator)", line)
    microchips = re.findall(r"(\w+)(?=\-compatible microchip)", line)
    itemsStart[i+1] = []
    for g in generators:
        numOfItems += 1
        itemsStart[i+1].append(('g', g))
    for m in microchips:
        numOfItems += 1
        itemsStart[i+1].append(('m', m))

print (itemsStart)


q = deque()
visited = set()

# lift must carry 1 or 2 devices
e = 1  # lift starts at first flore

print(numOfItems)
checkVisited(itemsStart, e)
q.append((e, itemsStart, 0)) # floor, items, step num


while q:
    e, items, s = q.popleft()
    # print(s)
    # printItems(items, e)
    # print()
    for ep in [-1, 1]:
        nf = e + ep # New floor
        if nf > 0 and nf < 5: # Valid new floor
            fb, gens = floorBaseline(nf, items)
            possibleCombinations, itemsAdded = addFloorToBaseline(fb, e, gens)
            # for c in possibleCombinations:
            #     print(c)
            for iArr in itemsAdded:
                newItems = copy.deepcopy(items)
                for i in iArr:
                    newItems[e].remove(i)
                    newItems[nf].append(i)
                if len(newItems[4]) == numOfItems: # all items on 4. floor, finished
                    print("Part 1:", s+1)
                    printItems(newItems, nf)
                    exit(0)
                fb, gens = floorBaseline(e, newItems)
                if checkValidity(fb):
                    if not (checkVisited(newItems,nf)):
                        q.append((nf, newItems, s+1))

for v in visited:
    print(v)
