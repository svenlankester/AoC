with open('data.txt', 'r') as f:
    data = f.read().split()

list1 = sorted([*map(int, data[0::2])])
list2 = sorted([*map(int, data[1::2])])

res = 0
for item in list1:
    res += (list2.count(item) * item)

print(res)
