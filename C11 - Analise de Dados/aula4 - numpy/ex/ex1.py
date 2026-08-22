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

print("\n--- Exercício 2 ---")
tabuleiro = np.zeros([2, 2])

bomba_lin = np.random.randint(0, 2)
bomba_col = np.random.randint(0, 2)
tabuleiro[bomba_lin, bomba_col] = 1

jogadas_feitas = set()
venceu = True

for jogada in range(3):
    print(f"\nJogada {jogada + 1}/3:")
    lin = int(input("Escolha a linha (0 ou 1): "))
    col = int(input("Escolha a coluna (0 ou 1): "))
    
    
    if tabuleiro[lin, col] == 1:
        print("Game Over!: (Try Again!")
        venceu = False
        break

if venceu:
    print("Congratulations! You beat the game! :)")

## Exercicio 3


## Exercicio 4


## Exercicio 5


## Exercicio 6



## Exercicio 7

