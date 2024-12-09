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
        size_leftover = data[i]
        temp_diskptr = disk_ptr
        for id in range(list(occurence.keys())[-1], 0, -1):
            if size_leftover > 0 and 0 < occurence[id] <= size_leftover:
                checksum += sum(range(temp_diskptr, temp_diskptr + occurence[id])) * id
                temp_diskptr += occurence[id]
                size_leftover -= occurence[id]
                occurence[id] = 0

    disk_ptr += data[i]

print(checksum)


