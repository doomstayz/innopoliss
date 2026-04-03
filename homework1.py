# Задача 1

print('Привет, ' + input(), input() + '!')

#или

name, surname = input(), input()
print(f" Привет, {name} {surname}!")

# Задача 2

name_1, name_2 = input(), input()
if name_2 == name_1*4:
    print('True')
else:
    print("False")

#или

print(input() == input()*4)

# Задача 3


product = input()
weight = int(input())*10

apple_calories = 52
banana_calories = 89
tomato_calories = 24

if product == "яблоки":
    print(weight * apple_calories)
elif product=="бананы":
    print( weight * banana_calories)
elif product== "помидоры":
    print (weight * tomato_calories)
else:
    print ("Неизвестный продукт")


#или так


while True:
    product = input().strip().lower()
    if product in ('яблоки', 'бананы','помидоры'):
        break
    print('Неверный продукт! Попробуйте еще раз.')

weight = int(input())*10

calories_per_kg = {
    'яблоки': 52,
    'бананы':89,
    'помидоры':24
}

total = weight * calories_per_kg[product]
print(total)


