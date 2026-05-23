import requests

response = requests.get('https://dummyjson.com/recipes')
data = response.json()
recipes = data['recipes']

pizza_list = []
italian_count = 0
max_recipe = recipes[0]
recipes_190 = []
all_reviews = 0

for recipe in recipes:

    if 'Pizza' in recipe['name']:
        pizza_list.append(recipe['name'])

    if recipe['cuisine'] == 'Italian':
        italian_count += 1

    if recipe['caloriesPerServing'] > max_recipe['caloriesPerServing']:
        max_recipe = recipe

    first_instruction = recipe['instructions'][0]

    if '190' in first_instruction:
        recipes_190.append(recipe['name'])

    all_reviews += recipe['reviewCount']

print('Піци:')
print(pizza_list)

print('Італійських страв:')
print(italian_count)

print('Найкалорійніша страва:')
print(max_recipe['name'])

print('Страви з 190°C:')
print(recipes_190)

print('Загальна кількість reviewCount:')
print(all_reviews)