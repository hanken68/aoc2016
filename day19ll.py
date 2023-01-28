from collections import deque

numOfElves = 3014603
# numOfElves = 8

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
    q.append(i)
lenq = len(q)
while lenq>1:
    elve = q.popleft()
    lenq = len(q)
    itemNum = (lenq + 1)//2 -1
    elveFrom = q[itemNum]
    del q[itemNum]
    q.append(elve)
    if lenq % 10000 == 0: print(lenq)
print("Part 2:", elve)

# 2043398 is too high