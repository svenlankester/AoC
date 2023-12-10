data = open("2023/day4/data.txt").readlines()

total = len(data)
multipliers = [1 for i in range(len(data))]

for i, entry in enumerate(data):
    current_card_wins = 0
    card = entry.split(": ")[1]
    card_split = card.split(" | ")
    winning = card_split[0].strip().replace("  ", " ").split(" ")
    pulls = card_split[1].strip().replace("  ", " ").split(" ")
    for number in pulls:
        if number in winning and i + current_card_wins < len(data):
            total += multipliers[i]
            current_card_wins += 1
    for j in range(i + 1, i + current_card_wins + 1):
        multipliers[j] += multipliers[i]
    
print(total)