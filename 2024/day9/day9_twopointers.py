with open('data.txt') as f:
    data = [*map(int, list(f.read().strip()))]

disk = []
for i in range(len(data)):
    if i % 2 == 0:
        disk.append([i // 2] * data[i])
    else:
        disk.append([None] * data[i])

disk = [x for entry in disk for x in entry]
i, j = 0, len(disk) - 1

checksum = 0
while i < j:
    if disk[i] != None:
        checksum += i * disk[i]
    else:
        while disk[j] == None:
            j -= 1
        checksum += i * disk[j]
        j -= 1
    i += 1
print(checksum)