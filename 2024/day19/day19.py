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

def dfs(to_check, todo):
    if not options: return False

    for item in to_check:
        if len(item) == len(todo): return True
        new_todo = todo[len(item):]
        ret = dfs(get_valid_options(options[new_todo[0]], new_todo), new_todo)
        if ret: return True

    return False

total = 0
for pattern in to_make:
    total += bool(dfs(get_valid_options(options[pattern[0]], pattern), pattern))

print(total)