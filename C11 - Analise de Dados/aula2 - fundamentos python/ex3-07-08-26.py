sexo = str(input("Digite seu sexo (M/F): "))

while sexo != "M" and sexo != "F":
    print("Sexo inválido")
    sexo = str(input("Digite seu sexo (M/F): "))
else:
    if sexo == "M":
        print("Sexo Masculino")
    else:
        print("Sexo Feminino")