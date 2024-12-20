from functools import cache
with open('data.txt') as f:
    data = f.read().split('\n\n')

available, to_make = data[0].split(', '), data[1].split('\n')

get_valid_options = lambda possibilities, todo: list(filter(lambda poss: len(poss) <= len(todo) and todo.startswith(poss), possibilities))

options = {
    'w': [],
    'u': [],
    'b': [],
    'r': [],
    'g': []
}

for option in available:
    options[option[0]].append(option)

@cache
def dfs(to_check, todo):
    if not options: return 0
    count = 0

    if len(to_check) == len(todo):
        return 1
    else:
        new_todo = todo[len(to_check):]
        valid_options = get_valid_options(options[new_todo[0]], new_todo)
        for option in valid_options:
            count += dfs(option, new_todo)
        return count

total = 0
for pattern in to_make:
    for option in get_valid_options(options[pattern[0]], pattern):
        total += dfs(option, pattern)
print(total)