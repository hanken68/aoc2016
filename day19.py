from collections import deque

numOfElves = 3014603
# numOfElves = 5

q = deque()
for i in range(1,numOfElves +1):
    q.append((i,1))

while len(q)>1:
    elve, numOfPackets = q.popleft()
    elveFrom, stealtPackets = q.popleft()
    q.append((elve, numOfPackets+stealtPackets))

elve, numOfPackets = q.pop()
print("Part 1:", elve)

q = deque()
for i in range(1,numOfElves +1):
    q.append((i,1))
lenq = len(q)
while lenq>1:
    elve, numOfPackets = q.popleft()
    itemNum = len(q)//2-1
    elveFrom, stealtPackets = q[itemNum]
    del q[itemNum]
    q.append((elve, numOfPackets+stealtPackets))
    lenq = len(q)
    if lenq % 10000 == 0: print(lenq)
print("Part 2:", elve)
