file = open("2023/day1/data.txt", "r")
input = file.readlines()

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

sum = 0

for line in input:
    parsedline = ""
    for enum, char in enumerate(line):
        if char.isdigit():
            parsedline += str(char)
        else:
            for i, number in enumerate(numbers):
                if line[enum:].startswith(number):
                    parsedline += str(i + 1)
                    break
    # print(parsedline)
    sum += int(str(parsedline[0]) + str(parsedline[-1]))

print(sum)