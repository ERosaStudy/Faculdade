import numpy as np
##ALEATORIEDADE

np.random.seed(129) ## tem que ser maior que 0 e menor que 2^32 - 1
matrizR = np.random.randint(0,10,10)
print (matrizR)


##bidimensional
bidimensional = np.random.randint(0,10,[5,5])
print (bidimensional)

##contando unicos e recorrencia de repetições

arr = np.array([1,2,3,4,5,6,3,3]) ## printando sem repetir os valores 
print (np.unique(arr))

##printando contando o numero de repetiçoes

print (np.unique(arr,return_counts=True))
