#---------------------Questão 01 -----------------------

# Criando a lista com os 5 primeiros colocados (exemplo)
times = ["Real Madrid", "Barcelona", "Bayern de Munique", "Manchester City", "Arsenal"]

print("Os 3 primeiros colocados:", times[:3])
print("Os 2 últimos colocados:", times[-2:])

# Lista em ordem alfabética (usando sorted para não alterar a lista original)
print("Ordem alfabética:", sorted(times))

# Encontrando a posição do Barcelona
# O índice começa em 0, então somamos 1 para a posição real na tabela
posicao_barcelona = times.index("Barcelona") + 1
print(f"O Barcelona se encontra na {posicao_barcelona}ª posição.")

#---------------------Questão 02 -----------------------

# Conjuntos de modelos de smartphones de cada loja
loja_a = {"iPhone 13", "Galaxy S22", "Moto G60"}
loja_b = {"Galaxy S22", "iPhone 14", "Poco X4"}

# União (modelos totais disponíveis se visitar as duas)
total_modelos = loja_a | loja_b
print("Modelos no total (opções de compra):", total_modelos)

# Interseção (modelos disponíveis em ambas as lojas)
modelos_em_ambas = loja_a & loja_b
print("Modelos disponíveis em ambas as lojas:", modelos_em_ambas)

#---------------------Questão 03 -----------------------

aluno = {}

aluno['nome'] = input("Digite o nome do aluno: ")
aluno['media'] = float(input("Digite a média do aluno: "))

# Verificando a aprovação
if aluno['media'] >= 50:
    aluno['situacao'] = 'AP'
else:
    aluno['situacao'] = 'RP'

print("\nConteúdo do dicionário do aluno:")
print(aluno)

#---------------------Questão 04 -----------------------

pessoas = []

# Lendo os dados de 3 pessoas
for i in range(3):
    nome = input(f"Nome da {i+1}ª pessoa: ")
    peso = float(input(f"Peso de {nome} (kg): "))
    pessoas.append({'nome': nome, 'peso': peso})

# Inicializando variáveis para comparação
mais_pesada = pessoas[0]
mais_leve = pessoas[0]

# Percorrendo a lista para encontrar os extremos
for pessoa in pessoas:
    if pessoa['peso'] > mais_pesada['peso']:
        mais_pesada = pessoa
    if pessoa['peso'] < mais_leve['peso']:
        mais_leve = pessoa

print(f"\nPessoa mais pesada: {mais_pesada['nome']} ({mais_pesada['peso']}kg)")
print(f"Pessoa mais leve: {mais_leve['nome']} ({mais_leve['peso']}kg)")


#---------------------Questão 05 -----------------------


n = int(input("Quantas pessoas deseja registrar? "))

soma_idades = 0
mulheres_sub20 = 0

for i in range(n):
    print(f"\n--- {i+1}ª Pessoa ---")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()
    
    soma_idades += idade
    
    # Verificando se é mulher E tem menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres_sub20 += 1

# Evitando divisão por zero caso n seja 0
media_idade = soma_idades / n if n > 0 else 0

print(f"\nMédia de idade do grupo: {media_idade:.2f} anos")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_sub20}")

#---------------------Questão 06 -----------------------

# Lista inicial
ingredientes = ["Farinha", "Ovos", "Açúcar", "Leite"]
print("Lista original:", ingredientes)

# Adicionando um novo ingrediente ao final
ingredientes.append("Fermento")
print("Após adicionar ao final:", ingredientes)

# Inserindo em uma posição específica (ex: índice 1)
ingredientes.insert(1, "Manteiga")
print("Após inserir na posição 1:", ingredientes)

# Removendo um ingrediente pelo valor
ingredientes.remove("Leite")
print("Após remover o leite:", ingredientes)


#---------------------Questão 07 -----------------------

# Lista convertida em conjunto para facilitar a operação
receita = {"Farinha", "Ovos", "Açúcar", "Leite", "Fermento", "Manteiga"}

# O que cada pessoa já tem em casa
pessoa1 = {"Farinha", "Açúcar"}
pessoa2 = {"Ovos", "Leite"}

# União do que as duas pessoas têm
ingredientes_em_casa = pessoa1 | pessoa2

# Diferença: O que tem na receita mas NÃO tem em casa
falta_comprar = receita - ingredientes_em_casa

print("Ingredientes que ainda faltam comprar:", falta_comprar)

produtos = []

# Lendo dados de 3 produtos
for i in range(3):
    print(f"\n--- Produto {i+1} ---")
    nome = input("Nome do produto: ")
    preco = float(input("Preço unitário: R$ "))
    quantidade = int(input("Quantidade em estoque: "))
    
    produto = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }
    produtos.append(produto)

print("\n--- Relatório de Estoque ---")
# Percorrendo a lista e calculando o valor total
for p in produtos:
    valor_total = p['preco'] * p['quantidade']
    print(f"Produto: {p['nome']} | Valor Total em Estoque: R$ {valor_total:.2f}")
    
    