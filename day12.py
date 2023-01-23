instructions = open("inputs\day12.txt", "r").read().splitlines()

numOfInstructions = len(instructions)

for part in [1,2]:
    address = 0
    registers = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0
    }
    if part == 2:
        registers['c'] = 1

    while address >=0 and address < numOfInstructions:
        parts = instructions[address].split(" ")
        match parts[0]:
            case "cpy":
                if parts[1].isnumeric(): registers[parts[2]] = int(parts[1])
                else: registers[parts[2]] = registers[parts[1]]
            case "inc":
                registers[parts[1]] += 1
            case "dec":
                registers[parts[1]] -= 1
            case "jnz":
                jmp = 0
                if parts[1].isnumeric(): jmp = int(parts[1])
                else: jmp = registers[parts[1]]
                if jmp != 0:
                    address += int(parts[2])
                    continue
        address += 1

    print(f"Part {part}:", registers['a'] ) 
