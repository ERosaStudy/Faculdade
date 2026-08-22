import numpy as np
import math 

np.random.seed()

## Exercicio 1
arr = np.ones(8)
arr2 = np.random.randint(0,10,8)

print(arr,arr2)
arrSoma = arr + arr2
##print(f'Soma de indices: {arr + arr2}')

if arrSoma.sum() >= 40:
    mtz = arrSoma.reshape(4,2)
else:
    mtz = arrSoma.reshape(2,4)

print("--- Exercício 1 ---")
print(f"Matriz resultante: \n", mtz)
print('')
print('')

## Exercicio 2

# print("\n--- Exercício 2 ---")
# tabuleiro = np.zeros([2, 2])

# bomba_lin = np.random.randint(0, 2)
# bomba_col = np.random.randint(0, 2)
# tabuleiro[bomba_lin, bomba_col] = 1

# jogadas_feitas = set()
# venceu = True

# for jogada in range(3):
#     print(f"\nJogada {jogada + 1}/3:")
#     lin = int(input("Escolha a linha (0 ou 1): "))
#     col = int(input("Escolha a coluna (0 ou 1): "))
    
    
#     if tabuleiro[lin, col] == 1:
#         print("Game Over!: (Try Again!")
#         venceu = False
#         break

# if venceu:
#     print("Congratulations! You beat the game! :)")

## Exercicio 3

print("\n--- Exercício 3 ---")

num_lin = np.random.randint(0, 7)
num_col = np.random.randint(0, 7)

mtz_ex3 = np.random.randint(1, 10, (num_lin, num_col))

linhas, colunas = mtz_ex3.shape
total_elementos = linhas * colunas

if total_elementos % 2 == 0:
    tipo = "par" 
else: 
    tipo = "ímpar"

print(f"Dimensões: {linhas}x{colunas} | Total: {total_elementos} elementos")
print(f"Poderia se tornar um vetor unidimensional com número {tipo} de elementos.")

## Exercicio 4
print("\n--- Exercício 4 ---")

mtz_ex4 = np.random.randint(1, 51, (4, 4))  
print("Matriz:\n", mtz_ex4)

media_linhas = mtz_ex4.mean(axis=1)
media_colunas = mtz_ex4.mean(axis=0)
print("a) Média das linhas:", media_linhas)
print("   Média das colunas:", media_colunas)

print(f"b) Maior média de linha: {media_linhas.max():.2f}")
print(f"   Maior média de coluna: {media_colunas.max():.2f}")


valores, contagens = np.unique(mtz_ex4, return_counts=True)
print("c) Aparições de cada número:")
for val, count in zip(valores, contagens):
    print(f"   Número {val}: {count} vez(es)")

duplicados = valores[contagens == 2]
print("   Números que aparecem exatamente 2 vezes:", duplicados)

## Exercicio 5

print("\n--- Exercício 5 ---")
mtz_zeros = np.zeros((3, 3))
mtz_uns = np.ones((3, 3))
escalar = 5

resultado_ex5 = (mtz_zeros + mtz_uns) * escalar
vetor_ex5 = resultado_ex5.reshape(9)

print("Vetor resultante de 9 elementos:\n", vetor_ex5)

## Exercicio 6



## Exercicio 7

