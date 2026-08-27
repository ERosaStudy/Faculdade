import numpy as np
import math 

mtz = np.array ([[1,2,3],[4,5,6],[7,8,9]])

print(mtz)
print('')

##PRINTANDO APENAS UMA LINHA
print(mtz[1])
print('')
##PRITANDO MAIS DE UMA LINHA

print(mtz[0:2])  ##--> vai printar da linha 0 até a linha 1, como se fosse um < que

#buscando colunas

print('')
print(mtz[:,:2])
print('')


## printando para ver quais numeros são maiores que 5

print(mtz>5)
print('')

