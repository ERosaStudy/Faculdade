distancia = float(input("Digite a distância em quilometros: "))
if distancia <= 200 and distancia > 0:
    preco = distancia * 0.50
    print(f"O preço da passagem é: R${preco:.2f}")
elif distancia > 200:
    preco = distancia * 0.45
    print(f"O preço da passagem é: R${preco:.2f}")