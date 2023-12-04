data = open('data.txt').read().split('\n')

start = "AA"
valves = dict()
valvesWithPosFR = ["AA"]
distToOtherValves = {}

class Valve:
    def __init__(self, fr, tunnels):
        self.fr = fr
        self.tunnels = tunnels

def bfs(src, dst):
    parents = {}
    explored = []
    Q = []
    explored.append(src)
    Q.append(src)
    while Q:
        v = Q.pop(0)
        if v == dst:
            stepcount = 0
            curr = dst
            while(curr in parents.keys()):
                curr = parents[curr]
                stepcount += 1
            return stepcount
        possibleMoves = [valves[name] for name in v.tunnels]
        for move in possibleMoves:
            if move not in explored:
                explored.append(move)
                parents[move] = v
                Q.append(move)

currPath = []
paths = []

def calcValue(path):
    minutesLeft = 26
    currFlow = 0
    total = 0
    time = 0
    for valve in range(1, len(path)):
        for dst in distToOtherValves[path[valve - 1]]:
            if dst[0] == path[valve]: time = dst[1] + 1
        total += currFlow * time
        minutesLeft -= time
        currFlow += valves[path[valve]].fr
    total += minutesLeft * currFlow
    return total

def findAllPathsFrom(curr, timeLeft, highest):
    currPath.append(curr)
    if timeLeft < 1:
        currPath.pop()
        entry = (calcValue(currPath), currPath[:])
        #optimization based on input knowledge, remove first check to make solution generic but run for minutes
        if entry[0] > 1000 and entry not in paths:
            paths.append(entry)
        return 
    
    for dst in distToOtherValves[curr]:
        if dst[0] in currPath:
            continue
        if timeLeft < (dst[1] + 1):
            entry = (calcValue(currPath), currPath[:])
            if entry[0] > 1000 and entry not in paths:
                paths.append(entry)
            continue
        else:
            findAllPathsFrom(dst[0], timeLeft - (dst[1] + 1), highest)
    currPath.pop()
    return

for i, line in enumerate(data):
    line = line.replace(',', '').replace('=', ' ').replace(';', '').split(' ')
    valve = Valve(int(line[5]), line[10:])
    valves[line[1]] = valve
    if valve.fr > 0:
        valvesWithPosFR.append(line[1])

for src in valvesWithPosFR:
    steps = []
    for dst in valvesWithPosFR:
        if src == dst or dst == start:
            continue
        else:
            steps.append((dst, bfs(valves[src], valves[dst])))
    distToOtherValves[src] = steps

findAllPathsFrom("AA", 26, 0)
paths.sort(reverse=True)
highest = 0
for path1 in paths:
    for path2 in paths:       
        if set(path1[1][1:]).isdisjoint(path2[1][1:]):
            if(path1[0] + path2[0] < highest):
                print(highest)
                exit()
            highest = path1[0] + path2[0]
