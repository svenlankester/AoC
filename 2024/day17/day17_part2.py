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

shortest = 99460
dists = {(start, 1): 0}
all_sp_nodes = set()

nodes = [(start, 1)]
path = set([start])

def walk(dist):
    last_dir = nodes[-1][1]
    loc = nodes[-1][0]

    if dist > shortest: return
    if dist == shortest and loc == end: all_sp_nodes.update(path)
    
    for dir, cost in [(last_dir, 1), ((last_dir + 1) % 4, 1001), ((last_dir - 1) % 4, 1001)]:
        new_dir = dirs[dir]
        next = add_tuple(new_dir, loc)

        if maze[next[0]][next[1]] != "#" and next not in path:
            next_entry = (next, dir)
            new_dist = dist + cost
            if next_entry not in dists or new_dist <= dists[next_entry]:
                dists[next_entry] = new_dist
                path.add(next)
                nodes.append(next_entry)
                walk(new_dist)
                path.remove(next)
                nodes.pop()

walk(0)
print(len(all_sp_nodes))