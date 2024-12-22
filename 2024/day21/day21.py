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
def get_path(code, is_numpad, depth):
    if depth == 0:
        return code

    path = ""
    pos = numpad['A'] if is_numpad else keypad['A']

    for char in code:
        end_pos = numpad[char] if is_numpad else keypad[char]
        dx, dy = end_pos[0] - pos[0], end_pos[1] - pos[1]

        corners = [(pos[0], pos[1] + dy), (pos[0] + dx, pos[1])]
        if is_numpad: check_both_corners = (0, 3) not in corners
        else: check_both_corners = (0, 0) not in corners

        if check_both_corners:
            path1, path2 = path, path
            for _ in range(abs(dy)):
                path1+= "^" if dy < 0 else "v"
            for _ in range(abs(dx)):
                path1 += "<" if dx < 0 else ">"

            for _ in range(abs(dx)):
                path2 += "<" if dx < 0 else ">"
            for _ in range(abs(dy)):
                path2 += "^" if dy < 0 else "v"

            if len(get_path(path1, False, depth - 1)) < len(get_path(path2, False, depth - 1)):
                path = path1
            else:
                path = path2
        # vertical first if possible
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

        path += "A"
        pos = end_pos

    return get_path(path, False, depth - 1)

total = 0
for code in data:
    total += len(get_path(code, True, 3)) * int(code[:-1])

print(total)