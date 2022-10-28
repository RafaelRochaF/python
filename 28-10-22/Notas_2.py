prova1 = float(input("Digite o nota da prova do 1º bimestre: "))
trabalho1 = float(input("Digite o nota do trabalho do 1º bimestre: "))
prova2 = float(input("Digite o nota da prova do 2º bimestre: "))
trabalho2 = float(input("Digite o nota do trabalho do 2º bimestre: "))
prova3 = float(input("Digite o nota da prova do 3º bimestre: "))
trabalho3 = float(input("Digite o nota do trabalho do 3º bimestre: "))
prova4 = float(input("Digite o nota da prova do 4º bimestre: "))
trabalho4 = float(input("Digite o nota do trabalho do 4º bimestre: "))

media1 = prova1+trabalho1
media2 = prova2+trabalho2
media3 = prova3+trabalho3
media4 =prova4+trabalho4

print("A nota do aluno no 1º Bimestre foi: ", media1)
print("A nota do aluno no 2º Bimestre foi: ", media2)
print("A nota do aluno no 3º Bimestre foi: ", media3)
print("A nota do aluno no 4º Bimestre foi: ", media4)

resultadoprova = prova1+prova2+prova3+prova4
resultadotrabalho = trabalho1+trabalho2+trabalho3+trabalho4
resultadofinal = resultadoprova+resultadotrabalho

print("A média de pontos do aluno por bimestre foi de :", resultadofinal/4)


if resultadofinal >= 60:
    print("O aluno foi APROVADO com ", resultadofinal, " pontos")

elif resultadofinal >=40 and 60:
    print("O aluno está de recuperação com ", resultadofinal, " pontos")

else:
    print("O aluno foi reprovado com ", resultadofinal, " pontos")