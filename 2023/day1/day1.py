file = open("2023/day1/data.txt", "r")
input = file.readlines()

sum = 0
for line in input:
    curr = ""
    last = ""
    first = True
    for char in line:
        if char.isdigit() and first:
            curr += str(char)
            last = str(char)
            first = False
        elif char.isdigit():
            last = str(char)
    curr += str(last)
    sum += int(curr)

print(sum)
