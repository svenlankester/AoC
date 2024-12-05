with open('data.txt') as f:
    rules, updates = f.read().split('\n\n')

rules = [[*map(int,rule.split('|'))] for rule in rules.split('\n')]
rules_dict = {}
for key, value in rules:
    rules_dict[key] = [value] if not (key in rules_dict.keys()) else rules_dict[key] + [value]
updates = [[*map(int, update.split(','))] for update in updates.split('\n')]

def update_correct(update):
    for i, entry in enumerate(update):
        if i == (len(update) - 1): 
            return True
        for future in update[i + 1:]:
            if future in rules_dict.keys() and entry in rules_dict[future]:
                return False

total = 0
for update in updates:
    if update_correct(update):
        total += update[len(update)//2]
print(total)