numero = int(input("Digite um número: "))

def soma(n:int):
  result = n  * (n + 1)/2
  # for i in range(1, n+1):
    # result += i
  return result
   
soma(numero)