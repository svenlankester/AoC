from itertools import combinations

with open('data.txt') as f:
    data = f.read().split()

antinodes = set()
antennas = {}

for y in range(len(data)):
    for x in range(len(data[y])):
        antenna_id = data[y][x]
        if antenna_id != '.':
            if antenna_id not in antennas:
                antennas[antenna_id] = set([(y, x)])
            else:
                antennas[antenna_id].add((y, x))

for key in antennas:
    for pair in combinations(antennas[key], 2):
        left, right = sorted(pair, key=lambda entry: entry[0])
        diff = tuple(map(lambda x, y: x - y, left, right))
        while 0 <= left[0] < len(data) and 0 <= left[1] < len(data[0]):
            antinodes.add(left)
            left = tuple(map(lambda x, y: x + y, left, diff))
        while 0 <= right[0] < len(data) and 0 <= right[1] < len(data[0]):
            antinodes.add(right)
            right = tuple(map(lambda x, y: x - y, right, diff))

print(len(antinodes))