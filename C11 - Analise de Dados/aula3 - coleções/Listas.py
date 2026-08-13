#listas
##são coleções de elementos, que podem ser de tipos diferentes, são mutáveis e ordenadas.
nomes = ["Goku", "Vegeta", "Gohan", "Trunks", "Piccolo"]

print(nomes)

#inserindo elementos na lista
nomes.append("Goten")#insere no final da lista

nomes.insert(1, "Kuririn")#insere na posição desejada

print(nomes)

#remover elementos da lista
del nomes[4]#remove o elemento da posição desejada

print(nomes)

nomes.pop(3) #remove o elemento da posição desejada e retorna o elemento removido

nomes.remove("Goten")#remove o elemento desejado

print(nomes)

if "Goku" in nomes:
    nomes.remove("Goku")#remove o elemento desejado
    print("Goku foi removido da lista.")
else:
    print("Goku não está na lista.")
    

print(len(nomes))#retorna o tamanho da lista

tamanho_lista = len(nomes)

##tratamento de erro para remover elemento de uma lista muito pequena

if tamanho_lista > 4:
    nomes.pop(4) #remove o elemento da posição desejada e retorna o elemento removido
    print("O elemento da posição 4 foi removido da lista.")
else:
    print("A lista é muito pequena")
    