lines = open("inputs\day20.txt").read().splitlines()

blocklist = set()
allowlist = set()
allowlist.add((0,4294967295))

def splitAllowList(b):
    for a in allowlist:
        if b[0] >= a[0] and b[0] <= a[1]: # start in range
            if b[1]> a[1]: # shrink range at top
                n = (a[0], b[0]-1)
                allowlist.remove(a)
                allowlist.add(n)
                return
            else: # split range
                n1 = (a[0], b[0]-1)
                n2 = (b[1]+1, a[1])
                allowlist.remove(a)
                if n1[1] >= n1[0]:
                    allowlist.add(n1)
                if n2[1] >= n2[0]:
                    allowlist.add(n2)
                return
        elif b[1]>=a[0] and b[1] <= a[1]: # end in range 
            if b[0]<=a[0]: # shrink range at bottom
                n = (b[1]+1, a[1])
                allowlist.remove(a)
                allowlist.add(n)
                return
        elif b[0]<=a[0] and b[1]>= a[1]:
            allowlist.remove(a)
            return



for line in lines:
    s , e = list(map(int,line.split("-")))
    blocklist.add((s,e))

lowIP = 0
for i in sorted(blocklist):
    splitAllowList(i)
    if lowIP == None:
        lowIP = i[1] +1
    else:
        if i[0] <= lowIP and i[1] >= lowIP: lowIP = i[1] + 1

print("Part 1:", lowIP)
numOfIpAllowed = 0
for a in sorted(allowlist):
    numOfIpAllowed += (a[1] - a[0] + 1)

print("Part 2:", numOfIpAllowed)



