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

binary_x = ""
binary_y = ""
binary_z = ""
for key in sorted(wires.keys(), reverse=True):
    match(key[0]):
        case "x": binary_x += str(wires[key])
        case "y": binary_y += str(wires[key])
        case "z": binary_z += str(wires[key])

desired_output = str(bin(int(binary_x, 2) + int(binary_y, 2)))[2:]

for i in range(len(binary_z)):
    if binary_z[i] != desired_output[i]:
        print("z", i, "has an error")

print(desired_output)
print(binary_z)

# The rest was done by hand