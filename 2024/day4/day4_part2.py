with open('data.txt') as f:
    data = f.read().strip().split()

# in y, x
directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
letters = "MS"
total = 0 

for y in range(1, len(data) - 1):
    for x in range(1, len(data[y]) - 1):
        if data[y][x] == "A":
            cross = [data[y + dir[0]][x + dir[1]] for dir in directions]
            if ("X" not in cross) and ("A" not in cross) and (cross[0] != cross[1]) and (cross[2] != cross[3]):
                total += 1    

print(total)