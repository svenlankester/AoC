stream = open('data.txt').read()
curr = 0
highestRock = 0
obstructed = set([(i, 0) for i in range(7)])

def generateRock(index, top):
    match index:
        case 0: return [(i, top + 4) for i in range(2, 6)]
        case 1: return [(3, top + 6), (2, top + 5), (3, top + 5), (4, top + 5), (3, top + 4)]
        case 2: return [(4, top + 6), (4, top + 5), (2, top + 4), (3, top + 4), (4, top + 4)]
        case 3: return [(2, top + i) for i in range(7, 3, -1)]
        case 4: return [(2, top + 5), (3, top + 5), (2, top + 4), (3, top + 4)]

def canDrop(shape):
    return not any(list(filter(lambda rock: rock in obstructed, list(map(lambda rock: (rock[0], rock[1] - 1), shape)))))

def canShift(shape, dir):
    return not any(list(filter(lambda rock: rock in obstructed or not -1 < rock[0] < 7, list(map(lambda rock: (rock[0] + (1 if dir == ">" else -1), rock[1]), shape)))))

def push(shape, dir):
    return list(map(lambda rock: (rock[0] + (1 if dir == ">" else -1), rock[1]), shape)) if canShift(shape, dir) else shape

def dropOne(shape):
    return list(map(lambda rock: (rock[0], rock[1] - 1), shape))

def dropRock(shape):
    # push -> fall
    global curr, highestRock
    while (True):
        shape = push(shape, stream[curr])
        curr = (curr + 1) % (len(stream))
        if(not canDrop(shape)): break
        shape = dropOne(shape)
    for i in shape: obstructed.add(i)
    highestRock = max(highestRock, max(list(map(lambda i: i[1], shape))))

patternStart = tuple()
pattern = tuple()
for i in range(999999):
    # Reduces runtime from 21 seconds to 0.6! keeps the array to match against short... (delete 4.4 (average length of new piece) * interval tiles everytime you add an interval of tiles, keeps list as constant length)
    # if (i % 25 == 0 and i > 25):
    #     del obstructed[:int(25 * 4.4)]
    # find pattern
    if (i == 1000):
        patternStart = (i % 5, highestRock, curr % len(stream), i)
    elif (i > 1000):
        if i % 5 == patternStart[0] and curr % len(stream) == patternStart[2]:
            pattern = (i - 1, highestRock - patternStart[1], curr % len(stream), i - patternStart[3])
            break
    shape = generateRock(i % 5, highestRock)
    dropRock(shape)

loopsInRemainder = (1000000000000 - pattern[0]) // pattern[3]
addedHeight = loopsInRemainder * pattern[1] #loop height
itersToGo = 1000000000000 - (loopsInRemainder * pattern[3]) - (pattern[0] + 1) # start 1 above the final processed line when detecting pattern

for i in range(itersToGo):
    shape = generateRock(i % 5, highestRock)
    dropRock(shape)

print(highestRock + addedHeight)