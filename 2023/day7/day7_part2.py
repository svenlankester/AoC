data = open("2023/day7/data.txt").readlines()

#tuples of (hand, bid)
ranks = []

def get_hand_value(hand):
    freqs = {}
    for card in hand:
        if card not in freqs.keys():
            freqs[card] = 1
        else:
            freqs[card] += 1

    if "J" not in freqs.keys():
        freqs["J"] = 0

    vals = list(freqs.values())

    if 5 in vals or freqs["J"] > 4:
        return 7
    elif 4 in vals or freqs["J"] > 3 or (freqs["J"] > 0 and (4 - freqs["J"]) in vals):
        return 6
    elif (3 in vals and 2 in vals) or (freqs["J"] > 0 and vals.count(2) == 2) or (freqs["J"] == 1 and 3 in vals and vals.count(1) == 2):
        return 5
    elif 3 in vals or freqs["J"] > 2 or (freqs["J"] > 0 and (3 - freqs["J"]) in vals):
        return 4
    elif vals.count(2) == 2 or (freqs["J"] == 2) or (freqs["J"] == 1 and vals.count(2) == 1):
        return 3
    elif 2 in vals or freqs["J"] == 1:
        return 2
    else:
        return 1

def card_is_higher(card1, card2):
    card_order = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "10", "T", 
                  "Q", "K", "A"]
    return card_order.index(card1) > card_order.index(card2)


def is_higher_rank(entry1, entry2):
    hand1 = entry1[0]
    hand2 = entry2[0]
    if get_hand_value(hand1) > get_hand_value(hand2):
        return True
    elif get_hand_value(hand1) == get_hand_value(hand2):
        for card1, card2 in zip(hand1, hand2):
            if card1 == card2:
                continue
            else:
                return card_is_higher(card1, card2)

for line in data:
    hand = line.split(" ")[0] 
    bid = int(line.split(" ")[1])
    if ranks == []:
        ranks.append((hand, bid))
        continue

    for enum, entry in enumerate(ranks):
        if enum == len(ranks) - 1 and is_higher_rank((hand, bid), entry):
            ranks.append((hand, bid))
            break
        if not is_higher_rank((hand, bid), entry):
            ranks.insert(enum, (hand, bid))
            break

result = 0
for enum, entry in enumerate(ranks):
    result += (enum + 1) * entry[1]

print(result)

