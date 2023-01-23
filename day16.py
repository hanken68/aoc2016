start = "10001001100000001"


def nextIteration(a):
    b = a[::-1]
    newb = ""
    for l in b:
        if l=='0': newb += '1'
        else: newb += '0'
    return a + '0' + newb

def getChecksum(d):
    checksum = ""
    for i in range(0,len(d),2):
        if d[i] == d[i+1]: checksum += "1"
        else: checksum += "0"
    return checksum

diskdata = start
part = 0
for disklen in [272, 35651584]:
    diskdata = start
    part += 1
    while len(diskdata)<disklen:
        diskdata = nextIteration(diskdata)
    diskdata = diskdata[:disklen]

    checksum = getChecksum(diskdata)
    oddeven = len(checksum) % 2

    while oddeven == 0:
        checksum = getChecksum(checksum)
        oddeven = len(checksum) % 2


    print(f"Part {part}:", checksum)
