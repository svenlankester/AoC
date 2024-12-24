with open('data.txt') as f:
    init, instructions = [*map(lambda x: x.split('\n'), f.read().split('\n\n'))]

wires = {}
for line in init:
    key, val = line.split(": ")
    wires[key] = int(val)

for i in range(len(instructions)):
    split = instructions[i].split(" ")
    instruction = (split[0], split[1], split[2], split[4])
    instructions[i] = instruction

while instructions:
    done = []
    for instruction in instructions:
        first, op, second, out = instruction
        if first in wires and second in wires:
            match(op):
                case "AND": wires[out] = wires[first] & wires[second]
                case "OR": wires[out] = wires[first] | wires[second]
                case "XOR": wires[out] = wires[first] ^ wires[second]
            done.append(instruction)
    for entry in done:
        instructions.remove(entry)

binary = ""
for key in sorted(wires.keys(), reverse=True):
    if key[0] == "z":
        binary += str(wires[key])

print(int(binary, 2))