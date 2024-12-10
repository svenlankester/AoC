with open("data.txt") as f:
    data = [[*map(int, list(line))] for line in f.read().split()]

dirs = [(-1, 0), (0, 1), (0, -1), (1, 0)]

def walk(to_try, prev_val):
    if prev_val == 9:
        return (len(to_try))

    next_to_try = [*filter(lambda test_dir: (0 <= test_dir[0] < len(data)) and (0 <= test_dir[1] < len(data[0]) and (data[test_dir[0]][test_dir[1]] == prev_val + 1)), [tuple(map(lambda x, y: x + y, loc, dir)) for loc in to_try for dir in dirs])]
    return walk(next_to_try, prev_val + 1)

total = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == 0:
            total += walk([(y, x)], 0)

print(total)