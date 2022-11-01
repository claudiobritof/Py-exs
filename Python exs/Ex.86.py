#3x3 Matrix

# Declarando variáveis
lista = list()
listb = list()


for i in range(0, 3):  # Para cada linha
    for j in range(0, 3):  # Para cada coluna em cada linha
        listb.append(int(input(f"Digite um valor para [{i}, {j}]: \n")))

    lista.append(listb[:]
    listb.clear()

for l in lista:
    print(l)