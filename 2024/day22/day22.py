with open('data.txt') as f:
    data = f.read().split()

mix_and_prune = lambda x, y: (x ^ y) % 16777216

def process_number(num):
    for _ in range(2000):
        num = mix_and_prune(num * 64, num)
        num = mix_and_prune(num // 32, num)
        num = mix_and_prune(num * 2048, num)
    return num

print(sum(map(process_number, map(int, data))))