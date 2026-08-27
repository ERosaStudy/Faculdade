import numpy as np

##Importando arquivos de teste

dataset = np.loadtxt('numpy.txt', delimiter=',',dtype=str)

print(f'TXT:{dataset}')
print('')

##criando arquivos puxando informações de outro

##np.savetxt('numpy2.txt',dataset, fmt='%s')

np.save('Arquivo.npy', dataset)

dataset1 = np.load('Arquivo.npy')

print(f'NPY:{dataset}')

##importando um arquivo csv

dataset = np.loadtxt('space.csv',delimiter = ';', dtype=str, encoding='utf-8')

header = dataset[0]
body = dataset[1:]

filter = dataset[:, 1] == 'SpaceX'
SpaceX = dataset[filter]

print(SpaceX)