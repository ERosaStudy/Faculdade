import pandas as pd

labels = ['a', 'b', 'c']  ## ---> indices de um vetor

dados = [10,20,30]  ## ---> dados de uma série

s = pd.Series(data=dados, index=labels)

print (s['a'])
print('')

s1 = pd.Series({'a':10, 'b':20, 'c':30})
s2 = pd.Series({'a':10, 'c':30, 'd':80})

print (s1 + s2)  ## faz a operação de soma entre as séries apenas nos indices que existems em ambas
print('')

print(s1.add(s2,fill_value=0)) ## faz a operação entre as séries e coloca 0 nos indices vazios
