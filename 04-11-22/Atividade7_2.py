valpao = float(input("Preço do pão: "))
print("")
print("Tabela de preços:")
for i in range(1, 51):
    print(f"{i:1d} - R$ {valpao*i:3.2f}")