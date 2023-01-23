disks = open("inputs\day15.txt", "r").read().splitlines()
# disks = open("inputs\sample.txt", "r").read().splitlines()

d = {}
md = 0
for disk in disks:
    parts = disk.split(" ")
    disknum = int(parts[1][1:])
    diskpos = int(parts[3])
    diskpos0 = int(parts[11][:len(parts[11])-1])
    d[disknum] = [diskpos, diskpos0]
    md=max(md, disknum)

d[(md+1)] = [11, 0]


def timeSuccess(time, disks):
    for d in sorted(disks):
        if (time + d + disks[d][1]) % disks[d][0] != 0:
            return False
    return True


t = 0

while not(timeSuccess(t,d)):
    t += 1

print("Part 2:", t)