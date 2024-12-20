with open('data.txt') as f:
    data = f.read().split()

start, end = None, None

add_tuple = lambda a, b: tuple(map(lambda x, y: x + y, a, b))
get_dist = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "S": start = (y, x)
        if data[y][x] == "E": end = (y, x)

path = [start]

dirs = [(0,1), (1,0), (0,-1), (-1,0)]
skips = set()

curr = start
last_dir = None
while curr != end:
    for i, dir in enumerate(dirs):
        if dir != last_dir:
            y, x = add_tuple(curr, dir)
            if data[y][x] == "." or data[y][x] == "E":
                last_dir = dirs[(i + 2) % 4]
                curr = (y,x)
                path.append(curr)
                break

for start_idx, cheat_start in enumerate(path):
    for end_idx, cheat_end in enumerate(path):
        if abs(cheat_start[0] - cheat_end[0]) + abs(cheat_start[1] - cheat_end[1]) == 2 and (cheat_start, cheat_end) not in skips and (cheat_end, cheat_start) not in skips and abs(start_idx - end_idx) - 2 >= 100:
            skips.add((cheat_start, cheat_end))

print(len(skips))