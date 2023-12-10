data = open("2023/day4/data.txt").readlines()

total = 0

for entry in data:
    current_card = 0
    entry = entry.split(": ")[1]
    entry = entry.split(" | ")
    winning = entry[0].strip().replace("  ", " ").split(" ")
    pulls = entry[1].strip().replace("  ", " ").split(" ")
    for number in pulls:
        if number in winning:
            current_card = 1 if current_card == 0 else current_card * 2
    total += current_card

print(total)
