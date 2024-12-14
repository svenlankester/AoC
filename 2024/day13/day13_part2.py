import numpy as np

with open("data.txt") as f:
    data = [x.split() for x in f.read().split('\n\n')]

machines = []

for entry in data:
    machines.append(((int(entry[2][2:-1]), int(entry[3][2:])), (int(entry[6][2:-1]), int(entry[7][2:])), (int(entry[9][2:-1]) + 10000000000000, int(entry[10][2:]) + 10000000000000)))

def get_minimal_cost(machine):
    a, b, output = machine
    input = [[a[0], b[0]], [a[1], b[1]]]
    determinant_orig = input[0][0] * input[1][1] - input[0][1] * input[1][0]
    determinant_x = output[0] * input[1][1] - output[1] * input[0][1]
    determinant_y = output[1] * input[0][0] - output[0] * input[1][0]

    num_a = determinant_x/determinant_orig if determinant_x % determinant_orig  == 0 else 0
    num_b = determinant_y/determinant_orig if determinant_y % determinant_orig  == 0 else 0

    return int(3 * num_a + num_b)


print(sum(map(get_minimal_cost, machines)))