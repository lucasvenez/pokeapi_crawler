import requests 

r = requests.get('https://pokeapi.co/api/v2/pokemon/2')



class pokeClass():
    def __init__(self, vl):
        self.value = vl
    def a(self):
        print(self.value)

i = pokeClass(10)
i2 = pokeClass(5)
i3 = pokeClass(1)

i.a()
i2.a()
i3.a()