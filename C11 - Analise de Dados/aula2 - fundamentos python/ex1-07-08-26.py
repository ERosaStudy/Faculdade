nome = input("Digite seu nome completo: ")

print (nome.upper())
print (nome.lower())
print(len(nome))

first_name = nome.split()[0]
nome_alt = f"{first_name} do inatel"
print(nome_alt)