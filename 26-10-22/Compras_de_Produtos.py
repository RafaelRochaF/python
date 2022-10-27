#Variaveis
iphone = float(2980)
sansung = float(2540)
tablet = float(1950)
notebook = float(2350)
ps5 = float(2100)
#Quantidade dos produtos
print("o valor do Iphone é: R$", iphone)
qtdiphone = int(input("Você deseja comprar quantos Iphones? "))
print("o valor do Sansumg é: R$", sansung)
qtdsansumg = int(input("Você deseja comprar quantos Sansumgs? "))
print("o valor do Tablet é: R$", tablet)
qtdtablet = int(input("Você deseja comprar quantos Tablets? "))
print("o valor do Notebook é: R$", notebook)
qtdnotebook = int(input("Você deseja comprar quantos Notebooks? "))
print("o valor do PS5 é: R$", ps5)
qtdps5 = int(input("Você deseja comprar quantos PS5? "))
#Valor total da compra
total = float((qtdiphone*iphone)+(qtdsansumg*sansung)+(qtdtablet*tablet)+(qtdnotebook*notebook)+(qtdps5*ps5))
print("O valor total das compras é: R$", total)
#Valor total da compra dividido em 3x
print("o valor da parcela dividido em 3x sem juros é: R$", total/3)
#Valor total da compra dividido em 6x com 5% de Juros
print("o valor da parcela dividido em 6x com 5% de juros é: R$", (total*1.05)/6)
#Valor total da compra com 10% de desconto
print("O valor total com desconto de 10% para o pagamento a vista é: R$", total-(total*0.1))