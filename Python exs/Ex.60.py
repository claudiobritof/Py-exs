#Factorial

num = int(input("Descubra o fatorial de um número: \n"))
counter = num
fat = 1

print("Calculando {}! = ".format(num), end="")
while counter > 0:
    print("{}".format(counter), end="")
    fat *= counter
    counter -= 1
    print(" x " if counter > 1 else " = ", end="")
print("{}".format(fat))