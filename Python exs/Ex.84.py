#People listing (improved)


lista = list()
listb = list()
counter = 0

# Atribuição dos dados nas listas:
while True:
    lista.append(str(input("Nome: \n")))
    lista.append(float(input("Peso (em kg): \n")))

    listb.append(lista[:])
    lista.clear()
    counter += 1

    pergunta = str(input("Continuar? [Sim/Não] \n")).upper()
    if pergunta[0] == "N":
        break


# Resposta a):
print(f"a) pessoas cadastradas: {counter}.")

# Tratamento dos dados contidos nas listas:

pesos = list()  # Lista onde estarão apenas os pesos

for i in listb:
    pesos.append(i[1])

pesos = sorted(pesos)  # Maior e o menor valor.

menor = pesos[0]
maior = pesos[-1]

# a) pessoas mais pesadas:
mais_pesados = list()
menos_pesados = list()


for k in listb:  # Para cada lista dentro de listb:
    if k[1] == maior:  # Se o peso for igual a maior
        mais_pesados.append(k[0])  # Adicione seu nome à lista
    if k[1] == menor:  # Se o peso for igual a menor,
        menos_pesados.append(k[0])  # Adicione seu nome à lista

# Respostas b) e c):
print(f" b) O maior peso foi de {maior}kg. Peso de {mais_pesados}")
print(f" c) O menor peso foi de {menor}kg. Peso de {menos_pesados}.")