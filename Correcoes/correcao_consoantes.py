vetor = []

for i in range(10):
    consoante = input("Digite uma letra de A-Z: ").lower()
    if consoante not in ["a","e","i","o","u"]:
        vetor.append(consoante)

print("O vetor possui: ",(len(vetor), " posições de consoantes."))
print("As consoantes digitadas foram: ", vetor)

