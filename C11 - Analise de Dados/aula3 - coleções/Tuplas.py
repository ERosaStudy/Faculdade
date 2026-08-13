##-----------------TUPLAS
##são coleções de elementos, que podem ser de tipos diferentes, são imutáveis


nomes_tupla = ("Goku", "Vegeta", "Gohan", "Trunks", "Piccolo","Raditz", "Kuririn", "Goten", "Freeza", "Cell", "Majin Boo")
print(nomes_tupla)

print(type(nomes_tupla))#retorna o tipo da variável

print(nomes_tupla[0])#retorna o elemento da posição desejada

print(nomes_tupla[1:4])#retorna os elementos da posição 1 a 3 da tupla

print(len(nomes_tupla))#retorna o tamanho da tupla


#Acessando elementos da tupla com loop for
for nome in nomes_tupla:
    print(nome)
    
for count in range(len(nomes_tupla)): ##acessando elementos da tupla com loop for e range
    print(f"Indice: {count}, Valor: {nomes_tupla[count]}")
    
for count in range (5):  ##acessando elementos até X posição da tupla com loop for e range
     print(f"Indice: {count}, Valor: {nomes_tupla[count]}")
     
