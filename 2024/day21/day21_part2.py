from functools import cache
with open('data.txt') as f:
    data = f.read().split()

get_dist = lambda a, b: (b[0] - a[0], b[1] - a[1])

numpad = {
    '9': (2, 0),
    '8': (1, 0),
    '7': (0, 0),
    '6': (2, 1),
    '5': (1, 1),
    '4': (0, 1),
    '3': (2, 2),
    '2': (1, 2),
    '1': (0, 2),
    '0': (1, 3),
    'A': (2, 3)
}

keypad = {
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1) 
}

@cache
def get_path(start, end, is_numpad):
    start = numpad[start] if is_numpad else keypad[start]
    end = numpad[end] if is_numpad else keypad[end]
    path = ""
    dx, dy = end[0] - start[0], end[1] - start[1]

    corners = [(start[0], start[1] + dy), (start[0] + dx, start[1])]
    if is_numpad: check_both_corners = (0, 3) not in corners
    else: check_both_corners = (0, 0) not in corners

    if check_both_corners:
        if dx < 0:
            for _ in range(abs(dx)):
                path += "<" if dx < 0 else ">"
            for _ in range(abs(dy)):
                path += "^" if dy < 0 else "v"
        else:   
            for _ in range(abs(dy)):
                path += "^" if dy < 0 else "v"
            for _ in range(abs(dx)):
                path += "<" if dx < 0 else ">"
    else:
        if (dx < 0):
            for _ in range(abs(dy)):
                path += "^" if dy < 0 else "v"
            for _ in range(abs(dx)):
                path += "<" if dx < 0 else ">"
        else:
            for _ in range(abs(dx)):
                path += "<" if dx < 0 else ">"
            for _ in range(abs(dy)):
                path += "^" if dy < 0 else "v"
    return path + "A"

@cache
def get_length(code, depth, total):
    if depth == 0:
        return len(code)
    for i, char in enumerate(code):
        total += get_length(get_path(code[i - 1], char, True if depth == 26 else False), depth - 1, 0)
    return total
        

total = 0
for code in data:
    total += get_length(code, 26, 0) * int(code[:-1])

print(total)