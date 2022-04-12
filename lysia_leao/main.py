
class PokeAPI():
	def __init__(self, value):
		self.value = value
	
	def imprimir(self): 
		print(self.value)
		

poke1 = PokeAPI(10)
poke2 = PokeAPI(5)
poke3 = PokeAPI(1)

poke1.imprimir()
poke2.imprimir()
poke3.imprimir()

