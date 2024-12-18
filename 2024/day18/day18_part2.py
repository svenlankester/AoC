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

for i in range(1024):
    corrupted.add(data[i])

def dijkstra():
    for y in range(size):
        for x in range(size):
            dists[(x,y)] = float('inf')
    dists[start] = 0
    prev = {}

    prio_queue = [(0, start)]
    while prio_queue:
        dist, source = heappop(prio_queue)

        if dist != dists[source]:
            continue

        if source == end:
            return dist, prev

        for neighbour in get_valid_moves(source):
            alt = dists[source] + 1
            if alt < dists[neighbour]:
                dists[neighbour] = alt
                prev[neighbour] = source
                heappush(prio_queue, (alt, neighbour))
    return dists[end], prev

_, prevs = dijkstra()
path = set()
curr = end
while curr != start:
    path.add(curr)
    curr = prevs[curr]

for i in range(1024,len(data)):
    new_corrupt = data[i]
    corrupted.add(new_corrupt)
    if new_corrupt in path:
        dist, prevs = dijkstra()
        if dist == float('inf'):
            print(new_corrupt)
            break
        path = set()
        curr = end
        while curr != start:
            path.add(curr)
            curr = prevs[curr]
