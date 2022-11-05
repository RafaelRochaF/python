vetor1 = []
print("Digite 10 números inteiros para a primeira lista ")
for i in range(10):
    vetor1.append(int(input("Número: ")))

print("")

vetor2 = []
print("Digite 10 números inteiros para a segunda lista ")
for i in range(10):
    vetor2.append(int(input("Número: ")))
res = vetor1 + vetor2
res[::2] = vetor1
res[1::2] = vetor2
print("")
print("A terceira lisata com os valores intercalados: ", res)