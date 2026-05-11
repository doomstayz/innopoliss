import pandas as pd
import matplotlib.pyplot as plt

#1
animals = pd.read_csv('animals.csv', index_col='name')

#2
crocodile_price = animals.loc['crocodile', 'shop_price']
print("Цена крокодила:", crocodile_price)

#3
land_animals = animals[animals['habitat'] == 'land']
avg_land_price = land_animals['shop_price'].mean()
print("Средняя цена наземных животных:", avg_land_price)

#4
max_iq = animals['iq_score'].max()
animals_with_max_iq = animals[animals['iq_score'] == max_iq].index.tolist()
print("Животные с наибольшим IQ:", animals_with_max_iq)

#5
brown_animals = animals[animals['color'] == 'brown']
cheapest_brown = brown_animals.loc[brown_animals['shop_price'].idxmin()]
print("Коричневое животное с наименьшей ценой:")
print(cheapest_brown[['name', 'shop_price']] if 'name' in cheapest_brown else cheapest_brown)

#6
avg_iq_by_habitat = animals.groupby('habitat')['iq_score'].mean()
print("Среднее IQ по среде обитания:\n", avg_iq_by_habitat)

#7
height = pd.read_csv('height.csv', index_col='name')
df = animals.join(height, how='inner')   # или merge
# Результат в df

#8
flying_animals = df[df['habitat'] == 'air']
plt.hist(flying_animals['height'], bins=10, edgecolor='black')
plt.title('Гистограмма роста летающих животных')
plt.xlabel('Рост (см)')
plt.ylabel('Частота')
plt.show()