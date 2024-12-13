with open("data.txt") as f:
    data = f.read().split()

dirs = [(-1, 0), (0, 1), (0, -1), (1, 0)]
dir_pairs = [
    [(-1, 0), (0, 1)], 
    [(-1, 0), (0, -1)],
    [(1, 0), (0, 1)],
    [(1, 0), (0, -1)] 
]
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

def calc_corners(region):
    corners = 0
    for location in region:
        for vertical, horizontal in dir_pairs:
            loc_h = tuple(map(lambda x, y: x + y, location, horizontal))
            loc_v = tuple(map(lambda x, y: x + y, location, vertical))
            diagonal = tuple(map(lambda x, y, z: x + y + z, horizontal, vertical, location))
            if loc_h not in region and loc_v not in region:
                corners += 1
            if loc_h in region and loc_v in region and diagonal not in region:
                corners += 1

    return corners

for y in range(len(data)):
    for x in range(len(data[0])):
        if (y, x) not in explored:
            new_region = get_region((y, x), data[y][x])
            regions.append(new_region)
            starts.append((y,x))

total = 0
for region in regions:
    area = len(region)
    sides = calc_corners(region)
    total += area * sides

print(total)

