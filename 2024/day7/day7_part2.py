with open('data.txt') as f:
    data = [[*map(int, x.split())] for x in f.read().replace(":", "").split("\n")]

def is_valid(ans, input):
    if len(list(filter(lambda x: x != [], input))) == 1:
        return input[0] == ans
    
    return is_valid(ans, [input[0] + input[1]] + input[2:]) or is_valid(ans, [input[0] * input[1]] + input[2:]) or is_valid(ans, [int(str(input[0]) + str(input[1]))] + input[2:])

total = 0
for line in data:
    ans, eq = line[0], line[1:]
    total += bool(is_valid(ans, eq)) * ans

print(total)