import re

with open('data.txt') as f:
    data = f.read()

equations = re.findall(r'(mul\([0-9]{1,3},[0-9]{1,3}\))', data)
res = 0
for eq in equations:
    nums = [*map(int, eq[4:-1].split(','))]
    res += (nums[0] * nums[1])

print(res)