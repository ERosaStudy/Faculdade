##---------------------DICIONÁRIOS---------------------
##são vários elementos adicionados em uma mesma lista


dicionario = {
    "nome": "Goku", 
    "idade": 37, 
    "poder": 9000}

print(dicionario) ## printa toda o dicionário
print(dicionario['idade']) ## printa somente a idade

dicionario['sexo'] = "M" ##adiciona o dado 

print (dicionario)

dicionario2 = {
    "nome": "Gohan",
    "idade": 14,
    "Poder":1200}

##criando um banco para salvar os dicionarios

banco = []
banco.append(dicionario)
banco.append(dicionario2)

for dicts in banco:
    print (dicts)

