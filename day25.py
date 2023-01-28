instructions = open("inputs\day25.txt", "r").read().splitlines()

def isIntValue(val):
    try:
        int(val)
        return True
    except:
        return False


numOfInstructions = len(instructions)

address = 0
registers = { 'a': 0, 'b': 0, 'c': 0, 'd': 0}

a = 0
digitcount =0
while digitcount < 100:
    address = 0
    registers = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0
    }
    registers['a']=a
    lastdigit = 1
    happy = True
    iterations = 0
    digitcount = 0
    digits = ""
    a += 1
    while (address >=0 and address < numOfInstructions) and happy and digitcount < 100:
        iterations += 1
        parts = instructions[address].split(" ")
        # if instructions[address] == "cpy d a":
        #     print( "Break")
        match parts[0]:
            case "cpy":
                if isIntValue(parts[1]):
                    registers[parts[2]] = int(parts[1])
                else: registers[parts[2]] = registers[parts[1]]
            case "out":
                digit = -1
                digitcount += 1
                if isIntValue(parts[1]):
                    digit = parts[1]
                else:
                    digit = registers[parts[1]]
                digits += str(digit)
                if not(digit in [0,1]):
                    print("nasty")
                happy = (digit != lastdigit) 
                lastdigit = digit
                # if not(happy):
                #     print("Møkk")
            case "inc":
                registers[parts[1]] += 1
            case "dec":
                registers[parts[1]] -= 1
            case "jnz":
                jmp = 0
                if isIntValue(parts[1]): 
                    jmp = int(parts[1])
                else: jmp = registers[parts[1]]
                if jmp != 0:
                    address += int(parts[2])
                    continue
        address += 1


print("Part 1:", a)
