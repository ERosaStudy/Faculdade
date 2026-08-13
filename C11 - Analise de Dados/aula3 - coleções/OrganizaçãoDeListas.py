
    
#----------------------------------------ORDENAÇÃO DE LISTAS

nomes = ["Goku", "Vegeta", "Gohan", "Trunks", "Piccolo"]


nomes.sort()#ordena a lista em ordem alfabética
print(nomes)

nomes.sort(reverse=True)#ordena a lista em ordem alfabética inversa
print(nomes)

sorted_nomes = sorted(nomes)#ordena a lista em ordem alfabética e cria uma nova lista
print(sorted_nomes)

nomes.append("True")#insere no final da lista
nomes.append("47")#insere no final da lista

print(nomes)

print(nomes[0])
nomes[0] = "Goku" #altera o elemento da posição desejada
print(nomes)

