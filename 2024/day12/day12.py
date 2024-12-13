with open("data.txt") as f:
    data = f.read().split()

dirs = [(-1, 0), (0, 1), (0, -1), (1, 0)]
regions = []
starts = []

explored = set()

def get_region(start, identifier):
    explored.add(start)
    region = set([start])
    to_add = set(filter(lambda test_dir: (0 <= test_dir[0] < len(data)) and (0 <= test_dir[1] < len(data[0]) and (data[test_dir[0]][test_dir[1]] == identifier)) and (test_dir not in region), [tuple(map(lambda x, y: x + y, start, dir)) for dir in dirs]))

    for entry in to_add:
        region.add(entry)

    while len(to_add) > 0:
        next_to_check = to_add.pop()
        region.add(next_to_check)
        explored.add(next_to_check)
        to_add = to_add.union(set(filter(lambda test_dir: (0 <= test_dir[0] < len(data)) and (0 <= test_dir[1] < len(data[0]) and (data[test_dir[0]][test_dir[1]] == identifier)) and (test_dir not in region), [tuple(map(lambda x, y: x + y, next_to_check, dir)) for dir in dirs])))

    return region

for y in range(len(data)):
    for x in range(len(data[0])):
        if (y, x) not in explored:
            new_region = get_region((y, x), data[y][x])
            regions.append(new_region)
            starts.append((y,x))

total = 0
for region in regions:
    area = len(region)
    perimiter = 0
    for item in region:
        perimiter += 4 - len(list(filter(lambda x: x in region, [tuple(map(lambda x, y: x + y, item, dir)) for dir in dirs])))
    total += (area * perimiter)

print(total)

