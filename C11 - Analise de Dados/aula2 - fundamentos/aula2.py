import math

print("Ola, mundo!")
print("17" + " anos")
print(2+3)


##formas de concatenação

print(True,False)   ##---> BOLEANOS
print("PI=",3.14159)
print("PI=" + "3.14159")  ##---> USO RESTRITO DE + NA MESMA VARIAVEL
print(f"PI={3.14159}")  
print("PI={0} e Euler = {1}".format(3.14159, 2.71828))
print("PI={} e Euler = {}".format(3.14159, 2.71828))
print("\nPI={1} e Euler = {0}".format(3.14159, 2.71828))


##-----------------------------TIPOS DE DADOS----------------------------------------------------------------

A=3
b = 2.71
c= True
d = "Inatel"


## printando o tipo das variaveis

print(type(A))        
print(type(b))  
print(type(c))
print(type(d))

idade1 = math.sqrt(16)
print(idade1)

##ENTRADA DE DADOS


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

print(f"Nome: {nome} \nIdade: {idade} \nPeso: {peso}")
