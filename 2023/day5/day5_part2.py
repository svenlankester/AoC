data = open("2023/day5/data.txt").read().split("\n\n")

seeds_line = data[0].split(": ")[1].split(" ")
seeds = []
for x in  range(0, len(seeds_line), 2):
    seeds.append((int(seeds_line[x]), int(seeds_line[x]) + int(seeds_line[x + 1]) - 1))
day_1_result = 57075758
results = []
final_index = 0

# dict of lists of tuples representing (start, end, addition amount if in range)
ranges = {} 
for n, mapping in enumerate(data[1:]):
    final_index = n
    mapping = mapping.split("\n")[1:]
    for entry in mapping:
        entry = entry.split(" ")
        if n not in ranges:
            ranges[n] = [(int(entry[0]), int(entry[0]) + (int(entry[2]) - 1), int(entry[1]) - int(entry[0]))]
        else:
            ranges[n].append((int(entry[0]), int(entry[0]) + (int(entry[2]) - 1), int(entry[1]) - int(entry[0])))

estimation = 0
estimation_range = 10000
for i in range(0, day_1_result, estimation_range):
    i_copy = i
    for j in range(final_index, -1, -1):
        for entry in ranges[j]:
            if entry[0] <= i_copy <= entry[1]:
                i_copy += entry[2]
                break
    for seedrange in seeds:
        if seedrange[0] <= i_copy <= seedrange[1]:
            estimation = i
            break
    if estimation != 0:
        break

for i in range(estimation - estimation_range, estimation):
    i_copy = i
    for j in range(final_index, -1, -1):
        for entry in ranges[j]:
            if entry[0] <= i_copy <= entry[1]:
                i_copy += entry[2]
                break
    for seedrange in seeds:
        if seedrange[0] <= i_copy <= seedrange[1]:
            print(i)
            exit()