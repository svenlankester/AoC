from heapq import *
with open('data.txt') as f:
    data = [tuple(map(int, line.split(','))) for line in f.read().split('\n')]

add_tuple = lambda a, b: tuple(map(lambda x, y: x + y, a, b))

size = 71
start = (0, 0)
end = (size - 1, size - 1)
corrupted = set()
dists = {}

def get_valid_moves(pos):
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    moves = []
    for dir in dirs:
        new_pos = add_tuple(pos, dir)
        if 0 <= new_pos[0] < size and 0 <= new_pos[1] < size and new_pos not in corrupted:
            moves.append(new_pos)
    return moves

def check_dijkstra(pos):
    dirs = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1, -1), (1,-1), (-1,1)]
    corrupt_count = 0
    wall_count = 0
    for dir in dirs:
        new_pos = add_tuple(pos, dir)
        if new_pos in corrupted:
            corrupt_count += 1
        elif not (0 <= new_pos[0] < size) or not (0 <= new_pos[1] < size):
            wall_count += 1
    return (corrupt_count > 1) or (wall_count > 0 and corrupt_count > 0)


for i in range(1024):
    corrupted.add(data[i])

def dijkstra():
    for y in range(size):
        for x in range(size):
            dists[(x,y)] = float('inf')
    dists[start] = 0

    prio_queue = [(0, start)]
    while prio_queue:
        dist, source = heappop(prio_queue)

        if dist != dists[source]:
            continue

        if source == end:
            return dist

        for neighbour in get_valid_moves(source):
            alt = dists[source] + 1
            if alt < dists[neighbour]:
                dists[neighbour] = alt
                heappush(prio_queue, (alt, neighbour))
    return(dists[end])

for i in range(1024,len(data)):
    new_corrupt = data[i]
    corrupted.add(new_corrupt)
    if check_dijkstra(new_corrupt):
        if dijkstra() == float('inf'):
            print(new_corrupt)
            break