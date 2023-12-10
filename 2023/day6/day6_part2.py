import re
from math import sqrt
from functools import reduce
data = open("2023/day6/data.txt").readlines()

times = [str(x.group()) for x in re.finditer(r'\d+', data[0])]
distances = [str(x.group()) for x in re.finditer(r'\d+', data[1])]

time = ""
distance = ""
for i in range(len(times)):
    time += times[i]
    distance += distances[i]

time = int(time)
distance = int(distance)

curr_solutions = 0
for j in range(int(time/10), time):
    result = j * (time - j)
    if (result > distance):
        curr_solutions += 1

print(curr_solutions)