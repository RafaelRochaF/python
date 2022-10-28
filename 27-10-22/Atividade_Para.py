# Atividade Tabuada

num = int(input("Digite um número inteiro para a tabuada: "))
inicio = int(input("Digite um número inteiro para a  o intervalo de início da tabuada: "))
fim = int(input("Digite um número inteiro para a  o intervalo final da tabuada: "))

for i in range(inicio, fim+1):
    resultado = int((i)*(num))
    print(resultado)