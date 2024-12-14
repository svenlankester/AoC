with open ('data.txt') as f:
    data = [*map(lambda x: (tuple(map(int, x.split(' ')[0][2:].split(',')))), f.read().split())]

width = 101
height = 103

robot_velocities = data[1::2]
robot_positions = data[::2]

open('output.txt', 'w')

def write_board(curr_time):
    with open('output.txt', 'a') as f:
        f.write(str(curr_time))
        f.write('\n')
        for y in range(height):
            for x in range(width):
                if (x, y) in robot_positions:
                    f.write("X")
                else:
                    f.write("_")
            f.write("\n")
        f.write("\n\n")

def find_line(min_acceptable):
    to_check = set(robot_positions)
    for y in range(height):
        curr_line = 0
        for x in range(1, width):
            if (x, y) in to_check:
                curr_line += 1
            else:
                curr_line = 0
            if curr_line > min_acceptable:
                return True
    return False

quadrants = [(0, width//2 - 1, 0, height//2 - 1), (width // 2 + 1, width - 1, 0, height//2 - 1), (0, width//2 - 1, height//2 + 1, height - 1), (width // 2 + 1, width - 1, height//2 + 1, height - 1)]

curr_time = 0
lowest_security = float('inf')
while True:
    curr_time += 1
    for i in range(len(robot_positions)):
        robot_positions[i] = ((robot_positions[i][0] + robot_velocities[i][0]) % width, (robot_positions[i][1] + robot_velocities[i][1]) % height)

    if find_line(10):
        write_board(curr_time)
        exit()