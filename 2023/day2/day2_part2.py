with open("2023/day2/data.txt", "r") as f:
    data = f.readlines()

sum = 0

for line in data:
    id = line.split(":")[0].strip("Game ")
    red = 0
    blue = 0
    green = 0
    grabs = line.strip("\n").split(": ")[1].split("; ")
    for grab in grabs:
        for entry in grab.split(", "):
            entry = entry.split(" ")
            number = entry[0]
            color = entry[1]
            if color == "red" and int(number) > red:
                red = int(number)
            elif color == "blue" and int(number) > blue:
                blue = int(number)
            elif color == "green" and int(number) > green:
                green = int(number)
    sum += (red * blue * green)
print(sum)

    