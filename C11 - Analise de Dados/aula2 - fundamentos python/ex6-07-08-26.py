import math
numero = float(input("Digite um número decimal: "))

#printar raiz quadrada do número
while numero < 0:
    print("Não é possível calcular a raiz quadrada de um número negativo")
    numero = float(input("Digite um número positivo: "))
else:
    print (f"A raiz quadrada de {numero} é {math.sqrt(numero)}")

#printar função teto
print (f"O teto de {numero} é {math.ceil(numero)}")

#print função chão
print (f"O chão de {numero} é {math.floor(numero)}")

#printar função parte inteira
print (f"A parte inteira de {numero} é {math.trunc(numero)}")