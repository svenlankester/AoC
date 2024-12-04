with open('data.txt') as f:
    data = f.read().strip().split()

# in y, x
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, -1), (1, 1), (-1, 1)]
word = "XMAS"
total = 0 

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "X":
            for dir in directions:
                tempx = x
                tempy = y
                correct = True
                for letter in word:
                    if not (0 <= tempx < len(data[0]) and 0 <= tempy < len(data)) or data[tempy][tempx] != letter:
                        correct = False
                        break
                    tempy += dir[0]
                    tempx += dir[1]
                total += bool(correct)

print(total)