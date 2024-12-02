with open('data.txt', 'r') as f:
    data = f.readlines()

def check_valid(input):
    for i in range(len(input)+1):
        entries = list(input)
        if i < len(input): entries.pop(i)
        distances = [abs(entries[i] - entries[i + 1]) for i in range(len(entries) - 1)]
        if (entries == sorted(entries, reverse=False) or entries == sorted(entries, reverse=True)) and (max(distances) < 4 and min(distances) > 0):
            return True
    return False

total = 0
for line in data:
    entries = [*map(int, line.strip().split())]
    total += 1 if check_valid(entries) else 0

print(total)