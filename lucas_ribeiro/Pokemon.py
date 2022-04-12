import requests


class Pokemon:
    def __init__(self, id):
        self.id = id
        x = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(self.id)).json()
        self.name = x['name']
        self.type = x['types']
        self.base_exp = x['base_experience']
        if x['id'] < 152:
            self.generation = "1ª Geração"
        elif x['id'] < 252:
            self.generation = "2ª Geração"
        elif x['id'] < 387:
            self.generation = "3ª Geração"
        elif x['id'] < 494:
            self.generation = "4ª Geração"
        elif x['id'] < 650:
            self.generation = "5ª Geração"
        elif x['id'] < 722:
            self.generation = "6ª Geração"
        elif x['id'] < 810:
            self.generation = "7ª Geração"
        else:
            self.generation = "8ª Geração"

    def print_info(self):
        tipos = '/'.join([t['type']['name'] for t in self.type])

        resposta = "ID: " + str(self.id) + "\nEspécie: " + self.name + "\nTipo: " + tipos + "\nEXP Base: " + str(
            self.base_exp) + "\nGeração: " + self.generation
        print(resposta)
