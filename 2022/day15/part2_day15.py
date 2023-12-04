data = open('data.txt').read().split('\n')
sensors = []
posCoefficients = set()
negCoefficients = set()

def addCoefficients():
    for sensor in sensors:
        x, y, radius = sensor[0], sensor[1], sensor[2]
        posCoefficients.add(y - x + radius + 1)
        posCoefficients.add(y - x - radius - 1)
        negCoefficients.add(x + y + radius + 1)
        negCoefficients.add(x + y - radius - 1)

def isUndetectable(x, y):
    res = True
    for sensor in sensors:
        if (abs(sensor[0] - x) + abs(sensor[1] - y)) <= sensor[2]: res = False
    return res

for line in data:
    coords = list(map(int, line.replace('Sensor at x=', '').replace(': closest beacon is at x=', ', y=').split(', y=')))
    sx, sy, bx, by = coords[0], coords[1], coords[2], coords[3]
    sensors.append((sx, sy, abs(sx - bx) + abs(sy - by)))

addCoefficients()
for l1 in posCoefficients:
    for l2 in negCoefficients:
        x, y = (l2 - l1) // 2, (l1 + l2) // 2
        if 0 <= x <= 4000000 and 0 <= y <= 4000000:
            if (isUndetectable(x, y)):
                print(x * 4000000 + y)
                exit()