#Atividade calculadora de dois valores

a = input("digite um numero:")
b = input("digite um segundo número:")
soma = (float(a)+float(b))
print("a soma dos números" +str(a)+ "+" +str(b)+ "é:")
print(soma)

subtracao = (float(a)-float(b))
print("a subtração dos números" +str(a)+ "-9" +str(b)+ "é:")
print(subtracao)

multiplicacao = (float(a)*float(b))
print("a multiplicação dos números" +str(a)+ "*" +str(b)+ "é:")
print(multiplicacao)

divisao = (float(a)/float(b))
print("a divisão dos números" +str(a)+ "/" +str(b)+ "é:")
print(divisao)

exponencia = (float(a)**float(b))
print("a exponenciação dos números" +str(a)+ "**" +str(b)+ "é:")
print(exponencia)