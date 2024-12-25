with open('data.txt') as f:
    data = f.read().split('\n\n')

keys = []
locks = []

for entry in data:
    entry = entry.split()
    curr = []
    curr_char = entry[0][0]
    for x in range(len(entry[0])):
        length = -1
        for y in range(len(entry)):
            if entry[y][x] == curr_char: length += 1
        if curr_char == ".": length = 5 - length
        curr.append(length)
    if curr_char == '.': keys.append(curr)
    else: locks.append(curr)

matches = 0
for lock in locks:
    for key in keys:
        does_match = True
        for i in range(len(lock)):
            if lock[i] + key[i] > 5:
                does_match = False
                break
        matches += bool(does_match)

print(matches)
