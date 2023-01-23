import re
from collections import Counter
import numpy
lines = open("inputs\day7.txt","r").read().splitlines()
# lines = open("inputs\sample.txt","r").read().splitlines()


def containsABBA(abba):
    for i in range(len(abba)-3):
        if abba[i] == abba[i+3] and abba[i+1] == abba[i+2] and abba[i] != abba[i+1]:
            return True
    return False

def getABA(abba):
    retArr= []
    for i in range(len(abba)-2):
        if abba[i] == abba[i+2] and abba[i] != abba[i+1]:
            retArr.append(abba[i:i+3])
    return retArr

def containsBAB(hypernet, aba):
    for h in hypernet:
        for a in aba:
            bab = a[1] + a[0] + a[1]
            if h.find(bab) >=0:
                return True
    return False

    

part1 = 0
part2 = 0

for line in lines:
    tls = True
    hypernet  = re.findall(r'\[.*?\]', line) # Find all
    supernet  = re.split(r'\[.*?\]',  line)
    # Check if hypernet contains abb
    for h in hypernet:
        if containsABBA(h):
            tls=False
            break
    if tls:
        tls = False
        for t in supernet:
            if containsABBA(t):
                tls = True
                break
    if tls:
        part1 += 1

    # Part 2
    aba =[]
    for s in supernet:
        aba += getABA(s)
    if containsBAB(hypernet, aba):
        part2 += 1




print ("Part 1:", part1)
print ("Part 2:", part2)