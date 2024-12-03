import re

with open('data.txt') as f:
    data = f.read()

equations = re.finditer(r'(mul\([0-9]{1,3},[0-9]{1,3}\))', data)
do = re.finditer(r'do\(\)', data)
dont = re.finditer(r'don\'t\(\)', data)

dos = [(0, 'do')] + [(x.end(0), 'do') for x in do]
donts = [(x.end(0), 'dont') for x in dont]

instructions = sorted(dos + donts, key=lambda x: x[0])

res = 0
for eq in equations:
    start = eq.start(0)
    try:
        last_instruction = instructions[next(x - 1 for x, instruct in enumerate(instructions) if instruct[0] > start)]
    except:
        last_instruction = instructions[-1]

    if last_instruction[1] == 'do':
        nums = [*map(int, data[eq.start(0) + 4:eq.end(0) - 1].split(','))]
        res += (nums[0] * nums[1])

print(res)