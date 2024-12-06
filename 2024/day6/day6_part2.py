with open('data.txt') as f:
    data = [*map(list, f.read().strip().split())]

#up right down left
dirs = [(-1, 0), (0, 1), (1, 0), (0,-1)]
traversed = {0: set(),
             1: set(),
             2: set(),
             3: set()}
currdir = 0
total = 0
orig_agent = None

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "^":
            orig_agent = (i, j)

def in_bounds(pos):
    return 0 <= pos[0] < len(data) and 0 <= pos[1] < len(data[0])

def detect_loop(test_loc):
    data[test_loc[0]][test_loc[1]] = "#"
    currdir = 0
    agent = orig_agent
    traversed_temp = {0: set(),
                1: set(),
                2: set(),
                3: set()}
    while(in_bounds(agent)):
        next_step = tuple(map(lambda x, y: x + y, agent, dirs[currdir]))

        if agent in traversed_temp[currdir]:
            data[test_loc[0]][test_loc[1]] = "."
            return True

        if (in_bounds(next_step) and data[next_step[0]][next_step[1]] == "#"):
            currdir = (currdir + 1) % len(dirs)
            continue 
        

        traversed_temp[currdir].add(agent)
        agent = next_step

    data[test_loc[0]][test_loc[1]] = "."
    return False

# generate map of original traversal
agent = orig_agent
while(in_bounds(agent)):
    next_step = tuple(map(lambda x, y: x + y, agent, dirs[currdir]))

    if (in_bounds(next_step) and data[next_step[0]][next_step[1]] == "#"):
        currdir = (currdir + 1) % len(dirs)
        continue 

    traversed[currdir].add(agent)
    agent = next_step

total = 0
checked = set()
for dir in traversed:
    perpendircular = (dir + 1) % 4
    for loc in traversed[dir]:
        if loc != orig_agent and loc not in checked:
            checked.add(loc)
            if detect_loop(loc): 
                total += 1

print(total)
        
