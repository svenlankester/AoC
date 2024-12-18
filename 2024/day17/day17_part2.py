import re

instructions = [*map(int, re.findall(r'\d+', open('data.txt').read()))][3:]

def decode(opcode, operand, instruction_ptr, output, regs):
    
    match opcode:
        case 0:
            operand = regs[operand%4] if operand > 3 else operand
            regs[0] = int(regs[0] / (2**operand))
        case 1:
            regs[1] = regs[1] ^ operand
        case 2:
            operand = regs[operand%4] if operand > 3 else operand
            regs[1] = operand % 8
        case 3:
            if regs[0] != 0: return operand
        case 4:
            regs[1] = regs[1] ^ regs[2]
        case 5:
            operand = regs[operand%4] if operand > 3 else operand
            output.append(operand % 8)
        case 6:
            operand = regs[operand%4] if operand > 3 else operand
            regs[1] = int(regs[0] / 2**operand)
        case 7:
            operand = regs[operand%4] if operand > 3 else operand
            regs[2] = int(regs[0] / 2**operand)
    return instruction_ptr + 2

def get_a(a, nums_found):
    if nums_found == len(instructions):
        return a
    for i in range(8):
        output = []
        instruction_ptr = 0
        new_a = a * 8 + i
        regs = [new_a, 0, 0]
        while instruction_ptr < len(instructions):
            instruction_ptr = decode(instructions[instruction_ptr], instructions[instruction_ptr + 1], instruction_ptr, output, regs)
        if output and output[0] == instructions[-nums_found - 1]:
            ret = get_a(new_a, nums_found + 1)
            if ret: 
                return ret

print(get_a(0, 0))