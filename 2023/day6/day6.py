import re
from functools import reduce
data = open("2023/day6/data.txt").readlines()

times = [int(x.group()) for x in re.finditer(r'\d+', data[0])]
distances = [int(x.group()) for x in re.finditer(r'\d+', data[1])]
solutions = []

for i, time in enumerate(times):
    dist = distances[i]
    curr_solutions = 0
    for j in range(1, time):
        result = j * (time - j)
        if (result > dist):
            curr_solutions += 1
    solutions.append(curr_solutions)

print(reduce(lambda x, y: x * y, solutions))