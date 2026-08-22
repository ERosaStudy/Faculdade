import numpy as np
import math 

np.random.seed()

## Exercicio 1
arr = np.ones(8)
arr2 = np.random.randint(0,10,8)

arrSoma = arr + arr2
##print(f'Soma de indices: {arr + arr2}')

if arrSoma.sum() >= 40:
    mtz = arrSoma.reshape(4,2)
else:
    mtz = arrSoma.reshape(2,4)

print(mtz)


## Exercicio 2


## Exercicio 3


## Exercicio 4


## Exercicio 5


## Exercicio 6



## Exercicio 7

