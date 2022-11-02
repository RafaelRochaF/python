vlhr = float(input("quanto você ganha por hora? "))
hrtr = float(input("Digite quantas horas você trabalhou no mês: "))
bruto = vlhr*hrtr

print("seu salario BRUTO é de: ", bruto)

ipr = bruto*0.11
inss = bruto*0.08
sdct = bruto*0.05
desctotal = bruto*0.24

print("Do seu salário descontado: ",desctotal)
print("Foi descontado do Salário: ")
print("Imposto de Renda: ", ipr)
print("Imposto ao Sindicato: ", sdct)
print("Imposto ao INSS: ", inss)
print(" Seu salário LÍQUIDO é de:", bruto-desctotal)
