import numpy
import math

##operações básicas

arr = numpy.array([1,2,3,4])
arr2 = numpy.array ([5,6,7,8])

print(f'valor minimo : {arr.min()},indice: {arr.argmin()}')
print(f'valor máximo : {arr.max()},indice: {arr.argmax()}')
print("")

x = arr
y = arr2

distancia_cm = numpy.hypot(x,y) * 100
angulo_graus = numpy.degrees(numpy.arctan2(y,x))
print (distancia_cm)
print (angulo_graus)
print("")
##soma
print(f'Soma:{arr.sum()}, média: {arr.mean()}')
print("")

print(arr,arr2)
##soma de indices

print(f'Soma de indices: {arr + arr2}')

##Multiplicação de indices

print(f'Multiplicação de indices: {arr * arr2}')

##concatenação
print(f"Concatenação: {numpy.concatenate((arr,arr2))}")
print('')
##OS VETORES PRECISAM TER O MESMO TAMANHO PARA REALIZAR AS OPERAÇÕES


##TRANSFORMAR VETOR UNIDIMENSIONAL EM MATRIZ, PRECISAM TER O MESMO NUMERO DE ELEMENTOS

arr3 = numpy.arange(9)  # --> cria até o numero de 9 indices

#print(f'tamamho do array: {arr3.size}')
#print(f'Quantidade de dimensões: {arr3.ndim}')
#print(f'Modelo do array: {arr3.shape}')

matriz = arr3.reshape([3,3])

print(matriz)
print('')

print(f'tamamho do array: {matriz.size}')
print(f'Quantidade de dimensões: {matriz.ndim}')
print(f'Modelo do array: {matriz.shape}')
print('')
print(f'Soma das colunas: {matriz.sum(axis=0)}')
print(f'Soma das linhas: {matriz.sum(axis=1)}')
print('')
print(f'Operação entre matriz e escalar(Broadcast)')
print(matriz*5)
print('')
print(matriz/2)
