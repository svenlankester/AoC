with open('data.txt') as f:
    data = [*map(int, list(f.read().strip()))]

disk = []

for i in range(len(data)):
    if (i % 2) == 0:
        disk.append([i // 2] * data[i])
    else:
        disk.append(["."] * data[i])

disk = [x for group in disk for x in group]

while "." in disk:
    disk[disk.index('.')] = disk[-1]
    next_id = disk[-1] - 1
    disk = disk[:-1]
    if disk[-1] == ".":
        disk.reverse()
        disk = disk[disk.index(next_id):]
        disk.reverse()

checksum = 0
for i, val in enumerate(disk):
    checksum += i * val
print(checksum)