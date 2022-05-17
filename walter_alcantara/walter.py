# Walter Moura Alcantara - JC3003213

import requests

def getPokemon(*pokemonIds):
  result = []
  url = 'https://pokeapi.co/api/v2/pokemon/'

  for pokemonId in pokemonIds:
    response = requests.get(url + str(pokemonId))
    data = response.json()

    result.append(data['name'])

  return result

pokemonIdList = [1, 72, 3, 44, 9, 36]

getPokemon(*pokemonIdList)
