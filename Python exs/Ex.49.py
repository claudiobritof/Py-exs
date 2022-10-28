#Multiplication table

num = int(input("Digite um número: \n"))
for i in range(1, 11):
    print("{} x {} = {}".format(num, i, (num * i)))