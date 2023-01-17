import numpy
lines = open("inputs\day3.txt","r").read().splitlines()
part1 = 0
numlist = []
for line in lines:
    numbers = list(map(int,line.split()))
    numlist.append(numbers)
    s = sum(numbers)
    nmin = min(numbers)
    nmax = max(numbers)
    if s-nmax > nmax: part1 += 1

# Part 2:
part2 = 0
r = 0
numoflines = len(numlist)
newNumbers = []
while r < numoflines:
    n = numpy.array(numlist[r:r+3]).transpose()
    for t in n:
        s = sum(t)
        nmin = min(t)
        nmax = max(t)
        if s-nmax > nmax: part2 += 1
    r += 3
   

print("Part 1:", part1)
print("Part 2:", part2)