import numpy


##array unidimensional


arr = numpy.array([1,2,3])
print (arr)


##array bidimensional

matriz = numpy.array([[1,2,3], [4,5,6],[7,8,9]])
print (matriz)

##array de zero e um 

arr = numpy.zeros(10)   ## printa o numero que esta dentro dos parantese em zeros
print (arr)

matriz = numpy.zeros([3,5])  #----> numero de linhas e numero de colunas com zero, no caso uma matriz 3x5
print (matriz)

matriz1 = numpy.ones([5,3]) # --> numero de linhas e numero de colunas com um, matriz 3x5
print(matriz1)

