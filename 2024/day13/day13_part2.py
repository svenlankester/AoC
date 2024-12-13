import numpy as np

with open("data.txt") as f:
    data = [x.split() for x in f.read().split('\n\n')]

machines = []

for entry in data:
    machines.append(((int(entry[2][2:-1]), int(entry[3][2:])), (int(entry[6][2:-1]), int(entry[7][2:])), (int(entry[9][2:-1]) + 10000000000000, int(entry[10][2:]) + 10000000000000)))

def get_minimal_cost(machine):
    a, b, end = machine
    input = np.array([[a[0], b[0]], [a[1], b[1]]])
    output = np.array([end[0], end[1]])
    res = np.linalg.solve(input, output)
    
    return int(3 * res[0] + res[1]) if (int(res[0]) * a[0] + int(res[1]) * b[0], int(res[0]) * a[1] + int(res[1]) * b[1]) == end else 0

print(sum(map(get_minimal_cost, machines)))