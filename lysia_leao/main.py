import requests 

def get_pokemon(*list):

  result = []

  for id in list:

    request = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(id))
    response= request.json()

    name = response['name']
    height = response['height']
    weight = response['weight']
    ability = response['abilities']
    
    result.append(('Nome do pokémon: ', name))
    result.append(('Altura', height))
    result.append(('Peso', weight))
  
    result.append('Habilides: ')
    
    for s in ability:
      abilitys = s['ability']['name']
      result.append((abilitys))
      
    result.append('------------------------------------------------------------------')

  return result

get_pokemon(1,2,3,4,5,6)