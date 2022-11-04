def ordenar(vetor):
    for i in range(len(vetor)):
        for j in range(i+1, len(vetor)):
            if vetor[i] > vetor[j]:
                x = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = x
    return vetor

vetor = []
for i in range(20):
    vetor.append(input("Digite um nome do aluno do enem: ").capitalize())


vetorOrdenado = ordenar(vetor)
print(vetorOrdenado)