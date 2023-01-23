import hashlib
from collections import deque
passcode = "udskfozm"
# passcode = "kglvqrro"

def getDoorStatus(path, passcode):
    doorStatus = [False, False, False, False] # up, down, left and right
    hashstr = hashlib.md5((passcode+path).encode()).hexdigest().lower()
    # print(hashstr[0:4])
    for i in range(4):
        doorStatus[i] = hashstr[i] in 'bcdef'
    return doorStatus


s =0
r, c = [0, 0]
q = deque()
q.append((r,c,"",s)) # r,c, path, stepnum
longestPath = 0
while q:
    r,c, path, s = q.popleft()
    # print(r,c,path,s)
    if r ==3 and c == 3: # at location
        if longestPath == 0:
            print("Part 1:", path)
        longestPath = max(longestPath,s)
    else:
        doorStatus = getDoorStatus(path,passcode)
        for i, d in enumerate(doorStatus): # [(0,-1),(0,1),(-1,0),(1,0)]:
            if d :
                match i:
                    case 0: # up
                        if r > 0:
                            q.append((r-1,c,path + "U", s+1))
                    case 1: # down
                        if r< 3:
                            q.append((r+1,c,path + "D", s+1))
                    case 2: # left
                        if c> 0:
                            q.append((r,c-1,path + "L", s+1))
                    case 3: # right
                        if c< 3:
                            q.append((r,c+1,path + "R", s+1))
print("Part 2:", longestPath)
    
