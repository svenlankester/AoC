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
    
    if 5 in freqs.values():
        return 7
    elif 4 in freqs.values():
        return 6
    elif 3 in freqs.values() and 2 in freqs.values():
        return 5
    elif 3 in freqs.values():
        return 4
    elif list(freqs.values()).count(2) == 2:
        return 3
    elif 2 in freqs.values():
        return 2
    else:
        return 1

def card_is_higher(card1, card2):
    card_order = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "T", "J", 
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

