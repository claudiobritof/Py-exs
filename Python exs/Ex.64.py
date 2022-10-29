#Listing numbers

flag = False
somador = 0
counter = 0

while flag == False:
    num = int(input("Digite um número [999 para parar]: \n"))
    if num == 999:
        flag = True
    else:
        somador += num
        counter += 1
print("Soma: {}.".format(somador))
print("Números digitados: {}.".format(counter))