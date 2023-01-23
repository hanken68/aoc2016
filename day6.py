from collections import Counter
import numpy
lines = open("inputs\day6.txt","r").read().splitlines()
# lines = open("inputs\sample.txt","r").read().splitlines()

arr = []
for l in lines:
    arr.append([*l])

transposed = numpy.array(arr).transpose()
part1 = ""
part2 = ""
for t in transposed:
    cCount = Counter(t)
    cOrdered = sorted(cCount.items(), key=lambda ct: ct[1], reverse=True)
    c = cOrdered[0][0]
    part1 += c
    cOrdered = sorted(cCount.items(), key=lambda ct: ct[1])
    c = cOrdered[0][0]
    part2 += c


print ("Part 1:", part1)
print ("Part 2:", part2)
