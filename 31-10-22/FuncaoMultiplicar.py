#Função de multiplicação

def multiplicacao(n1,n2):
    resultado = n1*n2

    return resultado


n1 = float(input("Digite um valor real ou inteiro: "))
n2 = float(input("Digite um valor real ou inteiro para ser multiplicado pelo primeiro: "))
resultado = multiplicacao(n1, n2)
print("A multiplicação dos números ",n1,"*",n2,"=",resultado)