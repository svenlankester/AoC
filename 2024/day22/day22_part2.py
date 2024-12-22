with open('data.txt') as f:
    data = f.read().split()

mix_and_prune = lambda x, y: (x ^ y) % 16777216

price_changes = {}

def process_number(num):
    seen = set()
    last_price = num % 10
    last_four_changes = (None, None, None, None)
    for _ in range(2000):
        num = mix_and_prune(num * 64, num)
        num = mix_and_prune(num // 32, num)
        num = mix_and_prune(num * 2048, num)
        last_four_changes = (last_four_changes[1], last_four_changes[2], last_four_changes[3], (num % 10) - last_price)
        last_price = num % 10

        if None not in last_four_changes and last_four_changes not in seen:
            seen.add(last_four_changes)
            if last_four_changes not in price_changes:
                price_changes[last_four_changes] = last_price
            else:
                price_changes[last_four_changes] += last_price

for secret in data:
    process_number(int(secret))
print(max(price_changes.values()))