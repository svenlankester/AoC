data = open("2023/day5/data.txt").read().split("\n\n")

seeds = list(map(int, data[0].split(": ")[1].split(" ")))
results = []
# dict of lists of tuples representing (start, end, addition amount if in range)
ranges = {} 
for n, mapping in enumerate(data[1:]):
    mapping = mapping.split("\n")[1:]
    for entry in mapping:
        entry = entry.split(" ")
        if n not in ranges:
            ranges[n] = [(int(entry[1]), int(entry[1]) + (int(entry[2]) - 1), int(entry[0]) - int(entry[1]))]
        else:
            ranges[n].append((int(entry[1]), int(entry[1]) + (int(entry[2]) - 1), int(entry[0]) - int(entry[1])))

for seed in seeds:
    for key in ranges.keys():
        for entry in ranges[key]:
            if entry[0] <= seed <= entry[1]:
                seed += entry[2]
                break
    results.append(seed)

print(min(results))