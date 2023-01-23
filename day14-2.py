import hashlib
salt = 'yjdafjpo'
# salt = 'abc'


def getStretchHash(salt, num, numberOfrepetitions):
    tempHash = salt + str(i)
    if i in hashDict:
        return hashDict[i]
    for t in range(numberOfrepetitions):
        tempHash = hashlib.md5((tempHash).encode()).hexdigest().lower()
    hashDict[i] = tempHash
    return tempHash

i = 0


chardict = {}
fivehash = ""
fivehashnum = 0
keyset = set()
keynum = 0
hashDict = {}
while True:
    hashstr = getStretchHash(salt, i, 2017)
    if fivehash == "":
        for c in range(len(hashstr)-2):
            if hashstr[c] == hashstr[c+1] and hashstr[c] == hashstr[c+2]:
                fivehash = hashstr[c]*5
                key = hashstr
                bookmark = i
                limit = i + 1000
                break
    else:
        keyfound = hashstr.find(fivehash)>=0
        if keyfound: # valid key
            keynum += 1
            keyset.add(key)
            print(keynum, bookmark, i, key)
            if len(keyset)==64:
                print(bookmark)
                break

        if (i >=limit ) or keyfound:
            i = bookmark 
            fivehash = ""

    i += 1
    
    # 22551 is too high