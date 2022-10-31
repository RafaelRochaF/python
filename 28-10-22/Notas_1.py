bim1 = float(input("Digite a nota do primeiro bimestre (Valor máximo de 25pts) : "))
bim2 = float(input("Digite a nota do segundo bimestre (Valor máximo de 25pts) : "))
bim3 = float(input("Digite a nota do terceiro bimestre (Valor máximo de 25pts) : "))
bim4 = float(input("Digite a nota do quarto bimestre (Valor máximo de 25pts) : "))

resultado = bim1+bim2+bim3+bim4

if resultado >=60 and resultado<=100:
    print("O aluno foi APROVADO com ", resultado, " pontos")

elif resultado >=40 and resultado <=60:
    print("O aluno está de recuperação com ", resultado, " pontos")

elif resultado <40 and resultado >=0:
    print("O aluno foi reprovado com ", resultado, " pontos")

else:
    print("Valor invalido, confirme os valores digitados!!!")