import requests
from pprint import pprint

url = 'https://dummyjson.com/products'
# url = 'https://www.ukr.net/'

response = requests.get(url=url)
# print(response.content)
# print(response.text)
response_json = response.json()
pprint(response_json)