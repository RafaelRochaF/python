vlhr = float(input("Quanto você ganha por hora? "))
hrtr = float(input("Digite quantas horas você trabalhou no mês: "))
bruto = vlhr*hrtr

print("\nSeu salario BRUTO é de: R${}" .format(bruto))

ipr = bruto*0.11
inss = bruto*0.08
sdct = bruto*0.05
desctotal = bruto*0.24

print("Foi descontado do Salário ao todo: ",desctotal)
print("Imposto de Renda: ", ipr)
print("Imposto ao Sindicato: ", sdct)
print("Imposto ao INSS: ", inss)
print("Seu salário LÍQUIDO é de: ", bruto-desctotal)
