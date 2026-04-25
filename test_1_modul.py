# 1

def get_squares_sum(arr):
    total = 0
    for num in arr:
        total += num * num
        return total


# 2

n = int(input())
grades = list(map(int, input().split()))

even_grades = [x for x in grades if x % 2 == 0]
avg = sum(even_grades) // len(even_grades)

print(avg)

# 3

text = input().replace(' ', '')
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
sorted_letters = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
result = ''.join([x[0] for x in sorted_letters[:5]])
print(result)


# 4

class FunnyList(list):
    def append(self, item):
        # Вставка элемента в начало списка
        self.insert(0, item)


# 5

n = int(input())


def is_palindrome(x):
    s = str(x)
    return s == s[::-1]


if is_palindrome(n):
    print(n)
else:
    d = 1
    while True:
        if n - d >= 0 and is_palindrome(n - d):
            print(n - d)
            break
        if is_palindrome(n + d):
            print(n + d)
            break
        d += 1
