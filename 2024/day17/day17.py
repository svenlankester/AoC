import re

instructions = [*map(int, re.findall(r'\d+', open('data.txt').read()))]
regs =  [instructions.pop(0), instructions.pop(0), instructions.pop(0)]

def decode(opcode, operand, instruction_ptr, output):
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
            if output:
                output.append(f',{operand % 8}')
            else:
                output.append(f'{operand % 8}')
        case 6:
            operand = regs[operand%4] if operand > 3 else operand
            regs[1] = int(regs[0] / 2**operand)
        case 7:
            operand = regs[operand%4] if operand > 3 else operand
            regs[2] = int(regs[0] / 2**operand)
    return instruction_ptr + 2

instruction_ptr = 0
output = []
while instruction_ptr < len(instructions):
    instruction_ptr = decode(instructions[instruction_ptr], instructions[instruction_ptr + 1], instruction_ptr, output)

print(''.join(output))