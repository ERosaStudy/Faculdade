import numpy as np
import pandas as pd

print("QUESTÃO 1: Criando as Series")
seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

print("QUESTÃO 2: Porcentagem total no mercado por ano")
total_ano1 = seriesAno1.sum()
total_ano2 = seriesAno2.sum()
print(f"Porcentagem total no Ano 1: {total_ano1:.2f}%")
print(f"Porcentagem total no Ano 2: {total_ano2:.2f}%")
print('')

print("QUESTÃO 3: Crescimento/declínio de cada linguagem")
crescimento = seriesAno2 - seriesAno1
print(crescimento.to_string())
print('')

print("QUESTÃO 4: Linguagens que tiveram crescimento")
crescimento_positivo = crescimento[crescimento > 0]
print(crescimento_positivo.to_string())
print('')

print("QUESTÃO 5: Projeção para os próximos 2 anos")
projecao = seriesAno2 + (crescimento * 2)
mais_popular = projecao.nlargest(1)
print(projecao.to_string())
print("\nLinguagem mais popular projetada:")
print(mais_popular.to_string())
print('')

print("QUESTÃO 6: DataFrame e média da coluna X (< 30)")
np.random.seed(42)  # Definindo semente para reprodutibilidade dos dados aleatórios
df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [5, 4])
)
print("DataFrame gerado:")
print(df.to_string())
media_x_menor_30 = df.loc[df['X'] < 30, 'X'].mean()
print(f"\nMédia dos elementos da coluna X menores que 30: {media_x_menor_30:.2f}")
print('')


print("QUESTÃO 7: Média da linha D (loc) e Soma da linha E (iloc)")
media_linha_d = df.loc['D'].mean()
soma_linha_e = df.iloc[4].sum()

print(f"Média da linha D: {media_linha_d:.2f}")
print(f"Soma da linha E: {soma_linha_e}")
print('')


print("QUESTÃO 8: Slicing (linhas A, C, E e colunas X, Y) e somas")
sub_df = df.loc[['A', 'C', 'E'], ['X', 'Y']]
print("Sub-DataFrame resultante:")
print(sub_df.to_string())

soma_linhas = sub_df.sum(axis=1)
soma_colunas = sub_df.sum(axis=0)

print("\nSoma de cada uma destas linhas:")
print(soma_linhas.to_string())
print("\nSoma de cada uma destas colunas:")
print(soma_colunas.to_string())
print('')