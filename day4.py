from collections import Counter
lines = open("inputs\day4.txt","r").read().splitlines()

part1= 0
part2= 0

for line in lines:
    l= line.split("[")
    letters = l[0].split("-")
    let2 = ''.join(letters[:-1])
    sum = int(letters[-1])
    charshiftcount = sum % 26
    sentence = ""
    
    for i, w in enumerate(letters):
        word=""
        for c in w:
            cord = ord(c)-97
            newOrd = (cord + charshiftcount) % 26
            word += chr(newOrd + 97)
        charcount = Counter(let2)
        if i>0: sentence +=" "
        sentence += word
    if sentence.find("northpole") >=0: 
        part2 = sum
    
    charsOrdered = sorted(charcount.items(), key=lambda ct: (ct[1]*-1, ct[0]))
    ordered = ""
    for t in range(5):
        ordered += charsOrdered[t][0]
    checksum = l[1][:-1]
    if ordered == checksum:
        part1 += sum


print("Part 1:", part1)
print("Part 2:", part2)
