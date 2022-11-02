n = int(input("Digite o número do mês que deseja saber a quantidade de casais: "))
ultimo = 1
penultimo = 1

if n==1 or n==2:
    print("Número total de casais no mês ", n ," é: 1")
else:
    for count in range(2, n):
        termo = ultimo+penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print("Número total de casais no mês ", n ," é: ", termo)