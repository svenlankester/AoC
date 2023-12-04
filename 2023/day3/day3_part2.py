import re

data = open("2023/day3/data.txt", "r").readlines()

sum = 0

gears = {(row, col): [] for row in range(len(data)) for col in range(len(data[0]) - 1) if data[row][col] == "*"}


for row, line in enumerate(data):
    for i in re.finditer(r'\d+', line):
        hitbox = []
        for r in range(row - 1, row + 2):
            for c in range(i.start() - 1, i.end() + 1):
                hitbox.append((r, c))
        
        for coord in hitbox:
            if coord in gears.keys():
                gears[coord].append(int(i.group()))

for coord in gears.keys():
    if len(gears[coord]) == 2:
        sum += (gears[coord][0] * gears[coord][1])
  
print(sum)