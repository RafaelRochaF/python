lista = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(5):
    for j in range(5):
        lista[i][j] = int(input("Digite um número inteiro: "))

n1 = int(input("Digite um número inteiro para localizar na matriz: "))

encontrado = False


for i in range(5):
    for j in range(5):
        if lista[i][j] == n1:
            print("Número encontrado: ",n1, "na posição ",lista[1][j])
            encontrado = True

if encontrado is False:
    print("Não foi encontrado seu número!")