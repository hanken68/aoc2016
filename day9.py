
line = open("inputs\day9.txt","r").read()

def decompSection(section, start, stop, recurse):
    p=start
    decomp = 0
    while p < stop:
        l = section[p]
        if l != '(': 
            decomp += 1
            p += 1
        else:
            close = section.find(")",p)
            marker = section[p+1:close]
            t1, t2 = list(map(int, marker.split('x')))
            p = close + 1
            if recurse:
                newString = section[p:p+t1] * t2
                decomp += decompSection(section, p, p+t1, True) * t2
            else:
                decomp += t1 * t2
            p += t1
    return decomp

part1 = decompSection(line, 0, len(line), False)
print("Part 1:", part1)
part2 = decompSection(line, 0, len(line), True)
print("Part 2:", part2)

