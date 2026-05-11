import numpy as np

#1
arr1 = np.zeros(5)
arr2 = np.zeros((5, 4))
arr3 = np.zeros((5, 10, 2))

print("Задание 1:")
print(arr1.shape, arr2.shape, arr3.shape)

#2
a = np.arange(0, 11)
b = np.arange(5, 16)
scalar = np.dot(a, b)
print("\nЗадание 2:")
print("Скалярное произведение:", scalar)

#3
c = np.arange(15, 106, 2)
mean_val = np.mean(c)
print("\nЗадание 3:")
print("Среднее значение:", mean_val)

#4
d = np.array([2, 5, 3, 6, 8, 11, 13])
d = d * 5
d = d ** 0.25
median_val = np.median(d)
print("\nЗадание 4:")
print("Медиана:", median_val)