num =int(input("Digite um número: "))
for i in range(1, num+1):
    for j in range(1, i+1):
        print(i, end="")
    num = num+1
