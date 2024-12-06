with open('data.txt') as f:
    data = [*map(list, f.read().strip().split())]

#up right down left
dirs = [(-1, 0), (0, 1), (1, 0), (0,-1)]
currdir = 0
total = 0
agent = None

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "^":
            agent = (i, j)

def in_bounds(pos):
    return 0 <= pos[0] < len(data) and 0 <= pos[1] < len(data[0])

while(in_bounds(agent)):
    next_step = tuple(map(lambda x, y: x + y, agent, dirs[currdir]))

    if (in_bounds(next_step) and data[next_step[0]][next_step[1]] == "#"):
        currdir = (currdir + 1) % len(dirs)
        continue 

    if (data[agent[0]][agent[1]] != "X"):
        total += 1
    data[agent[0]][agent[1]] = "X"
    agent = next_step

print(total)
