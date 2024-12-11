from copy import copy
with open("data.txt") as f:
    data = [*map(int, f.read().strip().split(' '))]

stones = {stone: 1 for stone in data}

for i in range(75):
    next_stones = {}
    for stone in stones.keys():
        if stone == 0:
            next_stones[1] = next_stones.get(1, 0) + stones[stone]
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            next_stones[int(str_stone[:len(str_stone)//2])] = next_stones.get(int(str_stone[:len(str_stone)//2]), 0) + stones[stone] 
            next_stones[int(str_stone[len(str_stone)//2:])] = next_stones.get(int(str_stone[len(str_stone)//2:]), 0) + stones[stone]
        else:
            next_stones[stone * 2024] = next_stones.get(stone*2024, 0) + stones[stone]
    stones = next_stones

print(sum(list(stones.values())))
