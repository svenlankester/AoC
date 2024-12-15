with open('data.txt') as f:
    data = f.read().split("\n\n")

board = [*map(lambda x: list(x.replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@.")), data[0].split())]
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
            
def can_move(box_edge, dir):
    edge = board[box_edge[0]][box_edge[1]]
    if edge == ".":
        return True
    box = (box_edge, add_tuple(box_edge, (0, 1))) if edge == "[" else (add_tuple(box_edge, (0, -1)), box_edge)

    match(dir):
        case (0, 1) | (0, -1):
            neighbour = add_tuple(box[1], dir) if dir == (0, 1) else add_tuple(box[0], dir)
            match(board[neighbour[0]][neighbour[1]]):
                case ".": return True
                case "#": return False
                case "[" | "]": return can_move(neighbour, dir)
        case (1, 0) | (-1, 0):
            neighbour1 = add_tuple(box[0], dir)
            neighbour2 = add_tuple(box[1], dir)
            if board[neighbour1[0]][neighbour1[1]] == "#" or board[neighbour2[0]][neighbour2[1]] == "#": return False
            if board[neighbour1[0]][neighbour1[1]] == "." and board[neighbour2[0]][neighbour2[1]] == ".": return True
            if board[neighbour1[0]][neighbour1[1]] == "[" or \
               board[neighbour2[0]][neighbour2[1]] == "[" or \
               board[neighbour1[0]][neighbour1[1]] == "]" or \
               board[neighbour2[0]][neighbour2[1]] == "]": return can_move(neighbour1, dir) and can_move(neighbour2, dir)

def move_boxes(box_edge, dir):
    edge = board[box_edge[0]][box_edge[1]]
    if edge == ".":
        return True
    box = (box_edge, add_tuple(box_edge, (0, 1))) if edge == "[" else (add_tuple(box_edge, (0, -1)), box_edge)

    match(dir):
        case (0, 1):
            neighbour = add_tuple(box[1], dir)
            if board[neighbour[0]][neighbour[1]] == ".":
                board[box[1][0]][box[1][1]] = "["
                board[neighbour[0]][neighbour[1]] = "]"
                return
            move_boxes(neighbour, dir)
            board[box[1][0]][box[1][1]] = "["
            board[neighbour[0]][neighbour[1]] = "]"

        case (0, -1):
            neighbour = add_tuple(box[0], dir)
            if board[neighbour[0]][neighbour[1]] == ".":
                board[box[0][0]][box[0][1]] = "]"
                board[neighbour[0]][neighbour[1]] = "["
                return
            move_boxes(neighbour, dir)
            board[box[0][0]][box[0][1]] = "]"
            board[neighbour[0]][neighbour[1]] = "["

        case (1, 0) | (-1, 0):
            neighbour1 = add_tuple(box[0], dir)
            neighbour2 = add_tuple(box[1], dir)
            if board[neighbour1[0]][neighbour1[1]] == "." and board[neighbour2[0]][neighbour2[1]] == ".":
                board[box[0][0]][box[0][1]] = "."
                board[box[1][0]][box[1][1]] = "."
                board[neighbour1[0]][neighbour1[1]] = "["
                board[neighbour2[0]][neighbour2[1]] = "]"
                return
            move_boxes(neighbour1, dir)
            move_boxes(neighbour2, dir)
            board[box[0][0]][box[0][1]] = "."
            board[box[1][0]][box[1][1]] = "."
            board[neighbour1[0]][neighbour1[1]] = "["
            board[neighbour2[0]][neighbour2[1]] = "]"

for instruction in instructions:
    dir = None
    match(instruction):
        case "^": dir = (-1, 0)
        case ">": dir = (0, 1)
        case "v": dir = (1, 0)
        case "<": dir = (0, -1)

    neighbour = add_tuple(dir, player)
    pushing_box = board[neighbour[0]][neighbour[1]] == "O"

    match(board[neighbour[0]][neighbour[1]]):
        case ".": 
            board[player[0]][player[1]] = "."
            player = add_tuple(player, dir)
            board[player[0]][player[1]] = "@"
        case "[" | "]":
            if can_move(neighbour, dir):
                move_boxes(neighbour, dir)
                board[player[0]][player[1]] = "."
                player = add_tuple(player, dir)
                board[player[0]][player[1]] = "@"

print_board()

total = 0
for y in range(len(board)):
    for x in range(len(board[0])):
        if board[y][x] == "[":
            total += 100 * y + x
print(total)