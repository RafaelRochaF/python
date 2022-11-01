

vetor = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    vetor[i] = str(input("preencha o a lista com 10 letras: "))

consoantes = 0

for i in(vetor):
    if i !="a" and i !="e" and i !="i" and i !="o" and i !="u":
        consoantes += 1
        print(i)

print("A quantidade de consoantes que você digitou foi de: ", consoantes, " consoantes.")