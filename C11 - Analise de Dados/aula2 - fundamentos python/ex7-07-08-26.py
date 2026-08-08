palavra = input("Digite uma palavra: ")
vogais = 0
a = 0

print("Fatiamento da palavra em maiúsculo:")
for letra in palavra.upper():
    print(letra)
    if letra.lower() in "aeiou":
        vogais += 1
    if letra.lower() == "a":
        a += 1

print("Quantidade de vogais:", vogais)

print ("Quantidade de letras 'A':", a)