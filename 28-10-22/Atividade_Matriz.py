matriz = [[0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4]]
msg = False

for l in range(5):
    for c in range(5):
        matriz [l][c] = int(input(f"Digite um valor para, [{l}, {c}]: "))

num = int(input("Digite um numero para verificar: "))

for l in range(5):
    for c in range(5):
        if matriz [l][c] == num:
            msg = True

if msg == False:
    print("Numero não encontrado!")
else:
    print("Número encontrado foi: ", matriz[l][c])