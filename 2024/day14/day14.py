with open ('data.txt') as f:
    data = [*map(lambda x: (tuple(map(int, x.split(' ')[0][2:].split(',')))), f.read().split())]

width = 101
height = 103
time = 100

robots_init = [(p, v) for p, v in list(zip(data[::2], data[1::2]))]
robots_final = []

for robot in robots_init:
    robots_final.append(((robot[0][0] + (time *robot[1][0])) % width, (robot[0][1] + (time * robot[1][1])) % height))

quadrants = [(0, width//2 - 1, 0, height//2 - 1), (width // 2 + 1, width - 1, 0, height//2 - 1), (0, width//2 - 1, height//2 + 1, height - 1), (width // 2 + 1, width - 1, height//2 + 1, height - 1)]

total = 1
for quadrant in quadrants:
    quadrant_total = 0
    for robot in robots_final:
        if quadrant[0] <= robot[0] <= quadrant[1] and quadrant[2] <= robot[1] <= quadrant[3]:
            quadrant_total += 1
    total *= quadrant_total

print(total)