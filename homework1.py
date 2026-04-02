# Задача 1

name, surname = input(), input()
print('Привет, ' + name + ' ' + surname, '!')

#или

name, surname = input(), input()
print(f" Привет, {name} {surname}!")

# Задача 2

name_1, name_2 = input(), input()
if name_2 == name_1*4:
    print('True')
else:
    print("False")

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

#не вспомнил как сделать интеррапт, если вводится что то кроме условных данных ><, давно проходил


