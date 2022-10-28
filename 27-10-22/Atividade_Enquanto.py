# Atividade Calculadora

resposta = ("s" or "n")
while resposta == "s":
   v1 = int(input("Digite um valor inteiro: "))
   sinal = input("Digite =, - ,* ou /: ")
   v2 = int(input("Digite um segundo valor inteiro para a conta: "))

   if sinal == "+" :
       print("A soma de " ,v1, "+", v2, "é: ", v1+v2)
   elif sinal == "-" :
       print("A subtração de " ,v1, "-", v2, "é: ", v1-v2)
   elif sinal == "*" :
       print("A multiplicação de " ,v1, "*", v2, "é: ", v1*v2)
   elif sinal == "/":
       print("A divisão de ", v1, "/", v2, "é: ", v1/v2)
   else:
       print("valor invalido")

   resposta = input("Deseja continuar a usar a calculadora? s/n: ")

print("Fim")