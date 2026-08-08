number = int(input("Digite um número para a tabuada: "))
number2 = int(input("Digite outro número para a tabuada: "))
#tabuada

for i in range(1, number2+1):
    result = int(number) * i
    print(f"{number} x {i} = {result}")