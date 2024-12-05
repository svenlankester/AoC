with open('data.txt') as f:
    rules, updates = f.read().split('\n\n')

rules = [[*map(int,rule.split('|'))] for rule in rules.split('\n')]
rules_dict = {}
for key, value in rules:
    rules_dict[key] = [value] if not (key in rules_dict.keys()) else rules_dict[key] + [value]
updates = [[*map(int, update.split(','))] for update in updates.split('\n')]

def fix_order(update, first=True):
    for i, entry in enumerate(update):
        if i == (len(update) - 1) and not first:
            return update
        for future in update[i + 1:]:
            if future in rules_dict.keys() and entry in rules_dict[future]:
                curr, prev = update.index(future), update.index(future) - 1
                update[curr], update[prev] = update[prev], update[curr]
                return fix_order(update, False)
    return [0]

total = 0
for update in updates:
    fixed = fix_order(update)
    total += fixed[len(fixed)//2]
print(total)