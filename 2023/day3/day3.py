import re

data = open("2023/day3/data.txt", "r").readlines()

sum = 0

symbols = [(row, col) for row in range(len(data)) for col in range(len(data[0]) - 1) if data[row][col] not in "1234567890."]
symboledges = []
for coord in symbols:
    for i in range(-1, 2):
        for j in range(-1, 2):
            if coord[0] + i >= 0 and coord[0] + i < len(data) and coord[1] + j >= 0 and coord[1] + j < len(data[0]) - 1:
                symboledges.append((coord[0] + i, coord[1] + j))


for row, line in enumerate(data):
    for i in re.finditer(r'\d+', line):
        for col in range(i.start(), i.end()):
            if (row, col) in symboledges:
                sum += int(i.group())
                break

print(sum)