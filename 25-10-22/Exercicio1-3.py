#Atividade calculadora de dois valores

a = float(input("digite um numero:"))
b = float(input("digite um segundo número:"))

print("a soma dos números " +str(a)+ " + " +str(b)+ " é: ", a+b)
print("a subtração dos números " +str(a)+ " - " +str(b)+ " é: ", a-b)
print("a multiplicação dos números " +str(a)+ " * " +str(b)+ " é: ", a*b)
print("a divisão dos números " +str(a)+ " / " +str(b)+ " é: ", a/b)
print("a potência do número " +str(a)+ " pelo número " +str(b)+ " é: ", int(a)**int(b))
print("o resto da divisão dos números " +str(a)+ " / " +str(b)+ " é: ", a%b)