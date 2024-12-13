with open("data.txt") as f:
    data = [x.split() for x in f.read().split('\n\n')]

machines = []

for entry in data:
    machines.append(((int(entry[2][2:-1]), int(entry[3][2:])), (int(entry[6][2:-1]), int(entry[7][2:])), (int(entry[9][2:-1]), int(entry[10][2:]))))

def get_minimal_cost(machine):
    minimal = float('inf')
    a, b, end = machine
    for i in range(100):
        for j in range(100):
            if tuple(map(lambda x, y: (x * i) + (y * j), a, b)) == end:
                minimal = min(i * 3 + j, minimal)
    return minimal if minimal != float('inf') else 0

print(sum(map(get_minimal_cost, machines)))