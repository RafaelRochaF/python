def fatorial(n):
    if n== 0:
        return 1
    else:
        return n*fatorial(n-1)

n = int(input("Digite um número para ser fatorado: "))

#print(n,"! = ",fatorial(n))
for i in range(1):
    print(f"{n:1d}! = {fatorial(n)}")