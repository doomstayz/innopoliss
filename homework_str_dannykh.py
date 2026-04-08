# 1

n = int(input())
result = []
for _ in range(n):
    x, y, z = map(int, input().split())
    result.append((x, y, z))
print(result)

# 2

replace_dict = {
    'к': 'т',
    'р': 'а',
    'и': 'к',
    'в': 'л',
    'о': 'у',
    'я': 'ч',
    'з': 'ш',
    'ы': 'е'
}
old_text = input()
new_text = ''
for char in old_text:
    if char in replace_dict:
        new_text += replace_dict[char]
    else:
        new_text += char
print(new_text)

# 3

n, k = int(input()), int(input())
common_set = set(input().split())

for _ in range(n - 1):
    student_works = set(input().split())
    common_set = common_set.intersection(student_works)

print(' '.join(sorted(common_set)))

# 4

n = int(input())
students = {}

for _ in range(n):
    x, y, z, k = map(int, input().split())
    coordinates = (x, y, z)
    if coordinates in students:
        students[coordinates].add(k)
    else:
        students[coordinates] = {k}

for coordinates, works in students.items():
    print(*coordinates, *works)
