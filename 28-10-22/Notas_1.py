bim1 = float(input("Digite a nota do primeiro bimestre: "))
bim2 = float(input("Digite a nota do segundo bimestre: "))
bim3 = float(input("Digite a nota do terceiro bimestre: "))
bim4 = float(input("Digite a nota do quarto bimestre: "))

resultado = bim1+bim2+bim3+bim4

if resultado >= 60:
    print("O aluno foi APROVADO com ", resultado, " pontos")

elif resultado >=40 and 60:
    print("O aluno está de recuperação com ", resultado, " pontos")

else:
    print("O aluno foi reprovado com ", resultado, " pontos")