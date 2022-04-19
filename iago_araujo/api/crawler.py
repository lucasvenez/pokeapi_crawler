import requests

class PokeAPI():
    def get_basic_information(self, id_or_name):
        url = "https://pokeapi.co/api/v2/pokemon/" + str(id_or_name)
        return requests.get(url)