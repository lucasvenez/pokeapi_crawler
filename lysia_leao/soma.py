numero = int(input("Digite um número: "))

def soma(n:int):
  result = 0
  for i in range(1, n+1):
    result += i
  return result
   
soma(numero)