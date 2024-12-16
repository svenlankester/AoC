from heapq import *

with open('data.txt') as f:
    maze = f.read().split()

dirs = [(-1,0), (0,1), (1,0), (0,-1)]
add_tuple = lambda a, b: tuple(map(lambda x, y: x + y, a, b))

start, end = None, None
for y in range(len(maze)):
    for x in range(len(maze[0])):
        if maze[y][x] == "S":
            start = (y,x)
        if maze[y][x] == "E":
            end = (y,x)

# in location : direction
dists = {(start, 1): 0}
prio_queue = [(0, (start, 1))]

while len(prio_queue) > 0:
    dist, (source, dir) = heappop(prio_queue)

    if dist != dists[(source, dir)]:
        continue

    if source == end:
        print(dist)
        exit()
    
    currdir = dirs[dir]
    next = add_tuple(source, currdir)
    if maze[next[0]][next[1]] != "#":
        next = (next, dir)
        new_dist = dist + 1
        if next not in dists or new_dist < dists[next]:
            dists[next] = new_dist
            heappush(prio_queue, (new_dist, next))
            
    for rotated_dir in [(dir - 1) % 4, (dir + 1) % 4]:
        next = (source, rotated_dir)
        new_dist = dist + 1000
        if next not in dists or new_dist < dists[next]:
            dists[next] = new_dist
            heappush(prio_queue, (new_dist, next)) 

