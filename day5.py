import hashlib
input = "uqwqemis"

i = 0
part1 = ""
part2 = "        "
pwlen = 8
pwfound = 2
while pwfound > 0:
    hash = hashlib.md5((input + str(i)).encode('utf-8')).hexdigest()
    if hash[0:5] == "00000":
        c6 = hash[5]
        if pwlen > 0:   
            part1 += c6
            pwlen -= 1
            if pwlen == 0:
                print("Part 1:", part1)
        c7 = hash[6]
        if c6.isnumeric():
            c6 = int(c6)
            if 0 <= c6 < 8:
                if part2[c6] == " ": 
                    part2 = part2[0:c6] + c7 + part2[c6+1:]
                if part2.find(" ")<0:
                    print("Part 2:", part2)
                    break
    i += 1
