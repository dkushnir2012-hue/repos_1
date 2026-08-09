import requests
from pprint import pprint

url = 'https://dummyjson.com/recipes'

params = {
    'limit': 0,
    'skip': 0
}

response = requests.get(url=url, params=params)

response_json = response.json()

recipes = response_json['recipes']


pizza_recipes = []
italian_count = 0

max_calories = 0
max_calories_recipe = ''

recipes_190 = []

total_reviews = 0


for recipe in recipes:
    if 'pizza' in recipe['name'].lower():
        pizza_recipes.append(recipe['name'])
    if recipe['cuisine'] == 'Italian':
        italian_count += 1
    if recipe['caloriesPerServing'] > max_calories:
        max_calories = recipe['caloriesPerServing']
        max_calories_recipe = recipe['name']
    if '190' in recipe['instructions'][0]:
        recipes_190.append(recipe['name'])

    total_reviews += recipe['reviewCount']

print('Рецепти піцци:')
pprint(pizza_recipes)

print('Кількість італійських страв:')
print(italian_count)

print('Найбільш калорійна страва:')
print(max_calories_recipe)
print(max_calories)

print('Страви при 190°C:')
pprint(recipes_190)

print('Всі перегляди:')
print(total_reviews)