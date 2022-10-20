#Metrics convert

n = int(input("Digite um valor em metros: \n"))

print("{} metros são {} quilômetros.".format(n, n * 1000))
print("{} metros são {} hectômetros.".format(n, n * 100))
print("{} metros são {} decâmetros.".format(n, n * 10))

print("{} metros são {} metros.".format(n, n * 1))

print("{} metros são {} decímetros.".format(n, n / 10))
print("{} metros são {} centímetros.".format(n, n / 100))
print("{} metros são {} milímetros.".format(n, n / 1000))