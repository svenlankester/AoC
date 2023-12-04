data = open('data.txt').read().split('\n')
total = 0
cubes = set()
dirs = [(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)]
airBlocks = set()
maxX, maxY, maxZ = 0, 0 ,0

def getNeighbours(cube):
    global maxX, maxY, maxZ
    moves = []
    for dir in dirs:
        if -1 <= (cube[0] + dir[0]) <= maxX + 2 and -1 <= (cube[1] + dir[1]) <= maxY + 2 and -1 <= (cube[2] + dir[2]) <= maxZ + 2:
            moves.append((cube[0] + dir[0], cube[1] + dir[1], cube[2] + dir[2]))
    return moves

for line in data:
    cube = tuple(map(int, line.split(',')))
    cubes.add(cube)
    maxX = max(maxX, cube[0])
    maxY = max(maxX, cube[1])
    maxZ = max(maxX, cube[2])

visited = set()
surfaceAir = set()
queue = [(-1, -1, -1)]
while queue:
    curr = queue.pop(0)
    visited.add(curr)
    neighbours = getNeighbours(curr)
    for neighbour in neighbours:
        if neighbour in cubes:
            surfaceAir.add(curr)
        elif neighbour not in visited and neighbour not in queue:
            queue.append(neighbour)
    
for cube in surfaceAir:
    for dir in dirs:
        if (cube[0] + dir[0], cube[1] + dir[1], cube[2] + dir[2]) in cubes: 
            total += 1

print(total)