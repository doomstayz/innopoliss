# 1

print(*filter(lambda x: 10 < x < 20, map(int, input().split())))


# 2

def get_normalized_coordinates(Xs, Ys):
    points = list(zip(Xs, Ys))
    if not points:
        return []
    x0, y0 = points[0]
    return list(map(lambda p: (p[0] - x0, p[1] - y0), points))


if __name__ == "__main__":
    Xs = list(map(int, input().split()))
    Ys = list(map(int, input().split()))
    result = get_normalized_coordinates(Xs, Ys)
    print(result)

# 3

import sys

sys.setrecursionlimit(1000000)


def F(n):
    if n <= 5:
        return n
    if n % 3 == 0:
        return n + F(n // 3 + 2)
    else:
        return n + F(n + 3)


n = 1
while True:
    try:
        val = F(n)
        if val > 1000:
            print(n)
            break
    except RecursionError:
        pass
    n += 1  # Ответ 732


# 4

class IncorrectUserIdError(Exception):
    pass


def process_user_id(user_id):
    if not isinstance(user_id, int):
        raise TypeError("Идентификатор должен быть целым числом")
    if user_id < 100000 or user_id > 999999:
        raise IncorrectUserIdError("Идентификатор должен быть 6-значным числом")
    print("Добро пожаловать!")


# 5

import asyncio
import time


async def print_temp():
    await asyncio.sleep(2)
    print("Current temperature is 120C")


async def print_pressure():
    await asyncio.sleep(3)
    print("Current pressure is 100kPa")


async def print_uranium_level():
    await asyncio.sleep(1)
    print("Uranium level is OK")


async def main():
    task1 = asyncio.create_task(print_temp())
    task2 = asyncio.create_task(print_pressure())
    task3 = asyncio.create_task(print_uranium_level())
    await asyncio.wait([task1, task2, task3])


if __name__ == "__main__":
    print("Starting...")
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"Time consumed: {end - start:.1f} с.")
