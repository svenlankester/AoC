with open('data.txt') as f:
    data = f.read().split("\n\n")

board = [*map(list, data[0].split())]
instructions = data[1].replace('\n', '')

player = None

add_tuple = lambda a, b: tuple(map(lambda x, y: x + y, a, b))
in_bounds = lambda x: 0 < x[0] < len(board) - 1 and 0 < x[1] < len(board[0]) - 1

def print_board():
    for y in range(len(board)):
        for x in range(len(board[0])):
            print(board[y][x], end='')
        print()            
        
for y in range(len(board)):
    for x in range(len(board[0])):
        if board[y][x] == "@":
            player = (y, x)

for instruction in instructions:
    dir = None
    match(instruction):
        case "^": dir = (-1, 0)
        case ">": dir = (0, 1)
        case "v": dir = (1, 0)
        case "<": dir = (0, -1)

    neighbour = add_tuple(dir, player)
    pushing_box = board[neighbour[0]][neighbour[1]] == "O"

    while in_bounds(neighbour):
        match(board[neighbour[0]][neighbour[1]]):
            case "#": break
            case ".": 
                if pushing_box: board[neighbour[0]][neighbour[1]] = "O"
                board[player[0]][player[1]] = "."
                player = add_tuple(player, dir)
                board[player[0]][player[1]] = "@"
                break
        neighbour = add_tuple(neighbour, dir)

total = 0
for y in range(len(board)):
    for x in range(len(board[0])):
        if board[y][x] == "O":
            total += 100 * y + x
print(total)