import requests
import json

class Pokemon:

    api_url = "https://pokeapi.co/api/v2/"
    verbose = True

    #menu_header = "###########################"

    # Realiza requisição a API
    # Retorna o JSON da resposta
    def makeApiRequest(self, arg: str):

        api_url = self.api_url

        request_result = requests.get(api_url+arg)

        # Verifica se a requisição foi bem sucedida
        if request_result.status_code != 200:
            return None

        json_response = json.loads(request_result.text) 

        return json_response  

    # Imprime o resultado da requisição
    def printResponse(self, ids, json_response):
        
        try:
            print("----------------------------------------------------")
            if self.verbose:
                for id in ids:
                    print("\t" + id + ": " + str(json_response[id]))
            print("----------------------------------------------------")
                    
        except:
            print("\tNão foi possível obter o resultado da requisição")
            print("\tVerifique se o ID é válido")

    # Obtem pokemons por nome ou ID
    def getPokemonsByNameID(self, arg):

        verbose_ids = ['id', 'name', 'base_experience', 'height', 'is_default']

        json_response = self.makeApiRequest("pokemon/"+str(arg))
        self.printResponse(verbose_ids, json_response)

    
    # Obtem movimentos por nome ou ID
    def getMovesByNameID(self, arg):

        verbose_ids = ['id', 'name', 'accuracy', 'power', 'pp']

        json_response = self.makeApiRequest("move/"+str(arg))
        self.printResponse(verbose_ids, json_response)
    
    # Obtem itens por nome ou ID
    def getItemsByNameID(self, arg):

        verbose_ids = ['id', 'name', 'cost']

        json_response = self.makeApiRequest("item/"+str(arg))
        self.printResponse(verbose_ids, json_response)
    
    # Obtem localização por nome ou ID
    def getLocationsByNameID(self, arg):
        
        verbose_ids = ['id', 'name', 'region']

        json_response = self.makeApiRequest("location/"+str(arg))
        self.printResponse(verbose_ids, json_response)

# Interface de usuário
class GUI:
    def start(self):
        print("Selecione uma opção:")
        print("1 - Obter pokemons por nome ou ID")
        print("2 - Obter movimentos por nome ou ID")
        print("3 - Obter itens por nome ou ID")
        print("4 - Obter localizações por nome ou ID")
        print("0 - Sair")
        choice = input("Digite a opção desejada: ")
        self.handleChoice(choice)
    

    # Trata a escolha do usuário
    # Pergunta pelo ID ou nome dos pokemons, e recebe como uma lista de inteiros e strings
    def handleChoice(self, choice):
        pokemon = Pokemon()
        if choice == "1":
            ids = input("Digite o ID ou nome do(s) pokemon(s): ").split()
            for id in ids:
                pokemon.getPokemonsByNameID(id)
        elif choice == "2":
            ids = input("Digite o ID ou nome do(s) movimento(s): ").split()
            for id in ids:    
                pokemon.getMovesByNameID(id)
        elif choice == "3":
            ids = input("Digite o ID ou nome do(s) item(s): ").split()
            for id in ids:    
                pokemon.getItemsByNameID(id)
        elif choice == "4":
            ids = input("Digite o ID ou nome do(s) localização(ões): ").split()
            for id in ids:  
                pokemon.getLocationsByNameID(id)
        elif choice == "0":
            print("Saindo...")
            exit(0)
        else:
            print("Opção inválida")
        self.start()


# Apenas para organizar o código
def main():
    gui = GUI()
    gui.start()

if __name__ == "__main__":
    main()