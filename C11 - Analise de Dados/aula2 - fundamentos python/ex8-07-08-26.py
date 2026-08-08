numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("Escolha a operação desejada:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Exponenciação")
escolha = int(input("Digite o número correspondente à operação desejada: "))




def adição (numero1, numero2):
    numero_final = numero1 + numero2
    return print("Resultado:", numero_final)

def subtração (numero1, numero2):
    numero_final = numero1 - numero2
    return print("Resultado:", numero_final)

def multiplicação (numero1, numero2):
    numero_final = numero1 * numero2
    return print("Resultado:", numero_final)

def divisão (numero1, numero2):
    if numero2 == 0:
        return print("Erro: Divisão por zero não é permitida.")
    numero_final = numero1 / numero2
    resto = numero1 % numero2
    return print("Resultado:", numero_final), print("Resto:", resto)

def exponenciacao (numero1, numero2):
    numero_final = numero1 ** numero2
    return print("Resultado:", numero_final)


if escolha == 1:
    adição(numero1, numero2)
elif escolha == 2:
    subtração(numero1, numero2)
elif escolha == 3:
    multiplicação(numero1, numero2)
elif escolha == 4:
    divisão(numero1, numero2)
elif escolha == 5:
    exponenciacao(numero1, numero2)
else:
    print("Operação inválida. Por favor, escolha uma opção válida.")
    