numero = int(input("Digite um número entre 1000 e 9999 "))

while numero <1000 or numero > 9999:
    numero = int(input("Número inválido, digite um número entre 1000 e 9999: "))
    
print(f"Milhar: {numero // 1000}")
print(f"Centena: {(numero // 100) % 10}")
print(f"Dezena: {(numero // 10) % 10}")
print(f"Unidade: {numero % 10}")