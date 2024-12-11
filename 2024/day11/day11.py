from copy import copy
with open("data.txt") as f:
    data = [*map(int, f.read().strip().split(' '))]
prev_data = copy(data)


for i in range(25):
    new_list = []
    for entry in prev_data:
        str_entry = str(entry)
        if entry == 0:
            new_list.append(1)
        elif len(str(entry)) % 2 == 0:
            new_list.append(int(str_entry[:len(str_entry)//2]))
            new_list.append(int(str_entry[len(str_entry)//2:]))
        else:
            new_list.append(entry * 2024)
    prev_data = new_list

print(len(prev_data))