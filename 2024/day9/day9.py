with open('data.txt') as f:
    data = [*map(int, list(f.read().strip()))]


occurence = {i//2: data[i] for i in range(len(data)) if i % 2 == 0}
checksum = 0
disk_ptr = 0

for i in range(len(data)):
    if all(0 == n for n in occurence.values()):
        break
    if (i % 2 == 0):
        checksum += (i // 2) * sum(range(disk_ptr, disk_ptr + occurence[i//2]))
        occurence[i//2] = 0
    else:
        for index in range(disk_ptr, disk_ptr + data[i]):
            first_nonzero = 0

            for id in range(list(occurence.keys())[-1], 0, -1):
                if occurence[id] != 0:
                    first_nonzero = id
                    break
            
            checksum += index * first_nonzero
            occurence[first_nonzero] -= 1

    disk_ptr += data[i]

print(checksum)


