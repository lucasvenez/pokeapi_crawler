import requests 
import json
r = requests.get('https://pokeapi.co/api/v2/pokemon/2')

dr = r.json()
print("Nome: ", dr['name'])
print("Altura: ", dr['height'])
print("XP: ", dr['base_experience'])
print("Id: ", dr['id'])
