
lines = open("inputs\day10.txt","r").read().splitlines()
# lines = open("inputs\sample.txt","r").read().splitlines()

def createBot(botid):
    if not(botid in bots):
        bots[botid] = [None, None, []]

def addValueToBin(binid, value):
    if binid in bins:
        bins[binid].append(value)
    else:
        bins[binid] = [value]

def addValueToBot(botid, value):
    createBot(botid)
    bots[botid][2].append(value)

bots = {}  # keeps botid , low, high, values
bins = {}  #

def printBots(withTwo):
    for b in sorted(bots):
        if withTwo and len(bots[b][2]) != 2:
            continue
        print(b, bots[b])

for line in lines:
    parts = line.split(" ")
    match parts[0]:
        case 'value':
            chip = int(parts[1])
            bot = int(parts[5])
            addValueToBot(bot, chip)
        case 'bot':
            bnum = int(parts[1])
            low = int(parts[6])
            high = int(parts[11])
            createBot(bnum)
            if parts[5] == 'bot': 
                createBot(low)
                bots[bnum][0]=low
            else: 
                bots[bnum][0]=low*-1
            if parts[10] == 'bot': 
                createBot(high)
                bots[bnum][1]=high
            else: 
                bots[bnum][1]=high*-1

finished = False
while not(finished):

    # printBots(True)
    finished = True
    for b in bots:
        if len(bots[b][2]) == 2:
            finished = False
            v1, v2 = sorted(bots[b][2])
            if v1 == 17 and v2 == 61:
                print("Part 1:", b)
            if bots[b][0]<0:
                addValueToBin((bots[b][0]+1)*-1, v1)
            else:
                addValueToBot(bots[b][0], v1)
            if bots[b][1]<0:
                addValueToBin((bots[b][1]+1)*-1, v2)
            else:
                addValueToBot(bots[b][1], v2)
            bots[b][2] = []


# printBots(False)
multi = 1
for i, b in enumerate(sorted(bins)):
    if i< 3:
        multi *= bins[b][0]
print("Part 2:", multi)



