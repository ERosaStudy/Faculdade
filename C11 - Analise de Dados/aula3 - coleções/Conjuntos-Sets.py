##-----------------CONJUNTOS (SETS)
##Só aceita valores únicos, não aceita valores duplicados, não é ordenado e não é indexado.

nomes_set = {"Goku", "Vegeta", "Gohan", "Trunks", "Piccolo"}
print(nomes_set)

print(type(nomes_set))#retorna o tipo da variável

nomes_set.add("Kuririn")#adiciona um elemento ao conjunto
print(nomes_set)

nomes_set.remove("Kuririn")#remove um elemento do conjunto
print(nomes_set)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a,b)

z = a.union(b)#união de conjuntos removendo os elementos duplicados
print(z)

z = a | b #segunda forma de união de conjuntos removendo os elementos duplicados
print(f"União: {z}")

z = a-b #diferença de conjuntos removendo os elementos duplicados
print(f"Diferença: {z}")
z1 = b-a #diferença de conjuntos removendo os elementos duplicados
print(f"Diferença: {z1}")

z = a & b #interseção de conjuntos deixando os elementos duplicados
print(f"Interseção: {z}")

