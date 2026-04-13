# 1

def get_initials(surname, name, patronymic=''):
    if patronymic:
        return f'{surname}.{name[0]}.{patronymic[0]}'
    else:
        return f'{surname} {name[0]}'


full_name = input().split()
print(get_initials(*full_name))


# 2

def get_initials(*args):
    surname = args[0]
    initials = ''.join([f'{name[0]}.' for name in args[1:]])
    return f'{surname}{initials}'


full_name = input().split()
print(get_initials(*full_name))

# 3

students = [
    {"id": 367673, "full_name": "Ярцев Валерий Рустэмович"},
    {"id": 563234, "full_name": "Шиптенко Виталий Программирович"},
    {"id": 982123, "full_name": "Датабейзов Иван Джетлагович"},
]


def give_license(student_id):
    global students
    for student in students:
        if student["id"] == student_id:
            return True
    return False


print(give_license(int(input())))


# 4

def fib(k, cache={}):
    if k in cache:
        return cache[k]
    if k == 1:
        return 0
    if k == 2:
        return 1
    cache[k] = fib(k - 1) + fib(k - 2)
    return cache[k]


n = int(input())
results = []
for _ in range(n):
    k = int(input())
    results.append(str(fib(k)))
print('\n'.join(results))


# 5

def cache_decorator(func):
    cache = {}

    def wrapper(k):
        if k not in cache:
            cache[k] = func(k)
        return cache[k]

    return wrapper


@cache_decorator
def fib(k):
    if k == 1:
        return 0
    if k == 2:
        return 1
    return fib(k - 1) + fib(k - 2)


n = int(input())
results = []
for _ in range(n):
    k = int(input())
    results.append(str(fib(k)))
print('\n'.join(results))
