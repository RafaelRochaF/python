#Variaveis
iphone = float(2980)
sansung = float(2540)
tablet = float(1950)
notebook = float(2350)
ps5 = float(2100)

#Quantidade dos produtos
qtdiphone = int(input("Você deseja comprar quantos Iphones? "))
qtdsansumg = int(input("Você deseja comprar quantos Sansumgs? "))
qtdtablet = int(input("Você deseja comprar quantos Tablets? "))
qtdnotebook = int(input("Você deseja comprar quantos Notebooks? "))
qtdps5 = int(input("Você deseja comprar quantos PS5? "))

#Valor total da compra
total = float((qtdiphone*iphone)+(qtdsansumg*sansung)+(qtdtablet*tablet)+(qtdnotebook*notebook)+(qtdps5*ps5))
print("O valor total das compras é: ", total)

#Valor total da compra dividido em 3x
parcela3 = total/3
print("o valor da parcela dividido em 3x é: ", parcela3)

#Valor total da compra dividido em 6x com 5% de Juros
parcela6 = (total*1.05)/6
print("o valor da parcela dividido em 6x é: ", parcela6)

#Valor total da compra com 10% de desconto
totaldesconto = total-(total*0.1)
print("O valor total com desconto para o pagamento a vista é: ", totaldesconto)