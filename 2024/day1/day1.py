print(sum(map(lambda x, y: abs(x - y), sorted([*map(int, open('data.txt').read().split())][0::2]), sorted([*map(int, open('data.txt').read().split())][1::2]))))
    

