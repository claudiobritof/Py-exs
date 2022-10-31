#Type errors (typo)


lista = [[], []]

for num in range(1, 8):
    numero = int(input((f"Digite um número ({num}/7): \n")))
    if numero % 2 == 0:
        lista[0].append(numero)  # números pares
    else:
        lista[1].append(numero)  # números ímpares

print(f"Números pares em ordem crescente: {sorted(lista[0])}")
print(f"Números ímpares em ordem crescente: {sorted(lista[1])}")