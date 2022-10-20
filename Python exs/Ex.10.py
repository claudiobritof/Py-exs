#How many dollars?

# Consider R$ 3.27 = US$ 1
n = float(input("Valor em BRL: \nR$"))
dolar = 3.27
conversao = n / dolar
print("R${} compram US$ {:.2f}.".format(n, conversao))