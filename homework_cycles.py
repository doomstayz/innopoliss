# 1

calories_per_100g = {
    'яблоки': 52,
    'бананы': 89,
    'помидоры': 24
}

n = int(input())
total = 0

for _ in range(n):
    while True:
        product = input().strip().lower()
        if product in calories_per_100g:
            break
        print('Неизвестный продукт!')
    weight_kg = float(input().strip())
    total += weight_kg * 10 * calories_per_100g[product]

print(int(total))

# 2

limit = 50
total_weight = 0
purchases = 0

while True:
    try:
        line = input().strip()
        if not line:
            continue
        weight = float(line)
    except EOFError:
        break

    if total_weight + weight <= limit:
        total_weight += weight
        purchases += 1
    else:
        break

print(int(total_weight), purchases, sep = '\n')


#3

n, k = int(input()), int(input())

players_list = ['Чижик', 'Пыжик', 'Ксюша']
weights_list = [list(map(int, input().split())) for _ in range(3)]
k_th_weights = [sorted(w)[k-1]for w in weights_list]
max_weight = max(k_th_weights)
winners = [players_list[i] for i, w in enumerate(k_th_weights) if w == max_weight]
print(winners[0] if len(winners) == 1 else 'Ничья!')