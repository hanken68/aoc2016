Lines = open("inputs\day23.txt", "r").read().splitlines()
# instructions = open("inputs\sample.txt", "r").read().splitlines()

## Part 2 takes forever, should have investigated the commented out part where addidion/subtraction could have been used...

def isIntValue(val):
    try:
        int(val)
        return True
    except:
        return False



def toggle(a):
    if a >=0 and a < numOfInstructions:
        parts = instructions[a].split()
        instr = parts[0]
        if len(parts)==2 : # one argument instruction
            if parts[0] == "inc":
                instr = "dec"
            else:
                instr = "inc"
        else: # two argument instruction
            if parts[0] == "jnz":
                instr = "cpy"
            else:
                instr = "jnz"
        pos = instructions[a].find(" ")
        if pos<0: return # do noting, something is wrong
        i = instr + instructions[a][pos:]
        instructions[a]= i
    return
    

for p in [7,12]:
    instructions = Lines.copy()
    numOfInstructions = len(instructions)
    address = 0
    registers = {
        'a': p,
        'b': 0,
        'c': 0,
        'd': 0  
    }
    while address >=0 and address < numOfInstructions:
        parts = instructions[address].split(" ")
        match parts[0]:
            case "tgl":
                if isIntValue(parts[1]):
                    toggle(address + int(parts[1]))
                else:
                    toggle(address + registers[parts[1]])
            case "cpy":
                if (not(isIntValue(parts[2]))):
                    if isIntValue(parts[1]): registers[parts[2]] = int(parts[1])
                    else: registers[parts[2]] = registers[parts[1]]
            case "inc":
                registers[parts[1]] += 1
            case "dec":
                registers[parts[1]] -= 1
            case "jnz":
                jmp = 0
                if isIntValue(parts[1]): jmp = int(parts[1])
                else: jmp = registers[parts[1]]
                if jmp != 0:
                    offset = 0
                    if isIntValue(parts[2]):
                        offset += int(parts[2])
                    else:
                        offset += registers[parts[2]]
                    # if offset == -2:
                    #     if instructions[address + offset + 1][0] == "dec" and instructions[address + offset + 1][1] == instructions[address][1]:
                    #         # try to add/subtract instead of loop
                    #         pass
                    #     else:
                    #         address += offset
                    address += offset
                    continue
        address += 1
    print(f"Part {1 if p==7 else 2}: {registers['a']}")
