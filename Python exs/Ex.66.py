#Listing numbers (w/ flag)

acc = counter = 0
while True:
    n = int(input("Digite inteiros [999 para parar] \n"))
    if n == 999:
        break
    else:
        counter += 1
        acc += n
print(f"Foram digitados {counter} números")
print(f"A soma entre eles é: {acc}")