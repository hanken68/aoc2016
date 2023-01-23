instructionsRight = open("inputs/day21.txt", "r").read().splitlines()

pw = "fbgdceah"
pw = "gcedfahb"


instructions=[]
while len(instructionsRight)>0:
    instructions.append(instructionsRight.pop())

for i in instructions:
    p = i.split(" ")
    match p[0]:
        case "rotate":
            pa = list(pw)
            pl = len(pa)
            dir = p[1]
            if dir == "based":
                numOfRotations = pw.find(p[6]) + 1
                if numOfRotations>4: numOfRotations += 1
                dir = "left"
            else:
                numOfRotations = int(p[2])
            for _ in range(numOfRotations):   
                match dir:
                    case "right":
                        l = pa[0]
                        for i in range(pl-1):
                            pa[i]= pa[i+1]
                        pa[pl-1] = l
                    case "left":
                        l = pa[pl-1]
                        for i in range(pl-1, -1, -1):
                            pa[i]= pa[i-1]
                        pa[0] = l
            pw = "".join(pa)
        case "swap":
            pa = list(pw)
            if p[1]=="position":
                p1 = int(p[2]); p2 = int(p[5])
            else:
                p1 = pw.find(p[2]); p2 = pw.find(p[5])
            l1 = pw[p1]; l2 = pw[p2]
            pa[p1] = l2; pa[p2] = l1
            pw = "".join(pa)
        case "reverse":
            pa = list(pw)
            f = int(p[2])
            t = int(p[4])
            d = (t-f+1)//2
            for i in range(d):
                l= pa[i+f]
                pa[i+f]= pa[t-i]
                pa[t-i]= l
            pw = "".join(pa)
        case "move":
            pa = list(pw)
            f = int(p[5])
            t = int(p[2])
            l = pa[f]
            pa.pop(f)
            pa.insert(t,l)
            pw = "".join(pa)
        
print ("Part 1:", pw)