import numpy as np
import math 

dataset = np.loadtxt('space.csv', delimiter=';', dtype = str, encoding ='utf-8')

##exercicio 1 

print('EXERCICIO 1')
header = dataset[0]
body = dataset[1:]

filter = body[:,7] == 'Success'

total_missoes = len(body)
total_sucesso = np.sum(filter)
porcentagem_sucesso = (total_sucesso / total_missoes) * 100

print(f'Porcentagem de missões que deram certo: {porcentagem_sucesso:.2f}%')

##exercicio 2

print('')
print('EXERCICIO 2')

filter2 = body[:,6].astype(float)
gastos = filter2[filter2 > 0]
media_gastos = np.mean(gastos)
print(f'Média de gastos das missões: U$ {media_gastos:.2f}')

## exercicio 3

print('')
print('EXERCICIO 3')
filter_locais = body[:, 2]
missoes_eua = np.sum(np.char.find(filter_locais, 'USA') != -1)
print(f'Missões pelos EUA: {missoes_eua}')

## exercicio 4

print('')
print('EXERCICIO 4')

filter_empresas = body[:, 1]
gastos_completos = body[:, 6].astype(float) 
filtro_spacex = (filter_empresas == 'SpaceX')
gastos_spacex = gastos_completos[filtro_spacex] 
missao_cara = np.max(gastos_spacex)
print(f'Missão mais cara da SpaceX: {missao_cara}')

## exercicio 5

print('')
print('EXERCÍCIO 5')
empresas_unicas, contagens = np.unique(filter_empresas, return_counts=True)
print('Empresas e quantidades de missões:')
for empresa, contagem in zip(empresas_unicas, contagens):
    print(f'- {empresa}: {contagem}')

## exercicio 6

print('')
print('EXERCÍCIO 6')

status = body[:, 5]
total_foguetes = len(status)
total_retired = np.sum(status == 'StatusRetired')
porcentagem_retired = (total_retired / total_foguetes) * 100
print(f'Porcentagem de foguetes com StatusRetired: {porcentagem_retired:.2f}%')